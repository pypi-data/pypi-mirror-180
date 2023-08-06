from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sb
import os
import warnings
warnings.filterwarnings('ignore')
import tensorflow as tf
from tensorflow.keras.layers.experimental.preprocessing import RandomFlip
import tensorflow.keras.layers as tfl
from tensorflow.keras.preprocessing import image_dataset_from_directory

import glob as gb
import cv2
import keras

from keras import backend as K
from keras.models import Sequential, Model,load_model
from keras.callbacks import EarlyStopping,ModelCheckpoint
from keras.layers import Dropout,ReLU,Layer, Input, add, Dense, concatenate,Activation, ZeroPadding2D, BatchNormalization, Flatten, Conv2D, AveragePooling2D, MaxPooling2D, GlobalMaxPooling2D,MaxPool2D,GlobalAveragePooling2D
from keras.preprocessing import image
from keras.initializers import glorot_uniform

# Model Checks
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score


import matplotlib.pyplot as plt 
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import roc_curve, auc, roc_auc_score
from itertools import cycle

#Model Graphs
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from collections import OrderedDict

#########################################################


from tensorflow.keras.layers import Layer, Embedding, Dense
import tensorflow as tf


class Patches(Layer):
    def __init__(self, patch_size):
        """ Patches
            Parameters
            ----------
            patch_size: int
                size of a patch (P)
        """
        super(Patches, self).__init__()
        self.patch_size = patch_size

    def call(self, images):
        """ Pass images to get patches
            Parameters
            ----------
            images: tensor,
                images from dataset
                shape: (..., W, H, C). Example: (64, 32, 32, 3)
            Returns
            -------
            patches: tensor,
                patches extracted from images
                shape: (..., S, P^2 x C) with S = (HW)/(P^2) Example: (64, 64, 48)
        """
        batch_size = tf.shape(images)[0]

        patches = tf.image.extract_patches(
            images=images,
            sizes=[1, self.patch_size, self.patch_size, 1],
            strides=[1, self.patch_size, self.patch_size, 1],
            rates=[1, 1, 1, 1],
            padding='VALID',
        )

        dim = patches.shape[-1]

        patches = tf.reshape(patches, (batch_size, -1, dim))
        return patches


class PatchEmbedding(Layer):
    def __init__(self, patch_size, image_size, projection_dim):
        """ PatchEmbedding
            Parameters
            ----------
            patch_size: int
                size of a patch (P)
            image_size: int
                size of a image (H or W)
            projection_dim: D
                size of project dimension before passing patches through transformer
        """
        super(PatchEmbedding, self).__init__()

        # S = self.num_patches: Number of patches
        self.num_patches = (image_size // patch_size) ** 2

        # cls token used for last mlp network
        self.cls_token = self.add_weight(
            "cls_token",
            shape=[1, 1, projection_dim],
            initializer=tf.keras.initializers.RandomNormal(),
            dtype=tf.float32
        )
        self.patches = Patches(patch_size)

        self.projection = Dense(units=projection_dim)

        # self.position_embedding shape: (..., S + 1, D)
        self.position_embedding = self.add_weight(
            "position_embeddings",
            shape=[self.num_patches + 1, projection_dim],
            initializer=tf.keras.initializers.RandomNormal(),
            dtype=tf.float32
        )

    def call(self, images):
        """ Pass images to embed position information 
            Parameters
            ----------
                        images: tensor,
                images from dataset
                shape: (..., W, H, C). Example: (64, 32, 32, 3)
            Returns
            -------
            encoded_patches: tensor,
                embed patches with position information and concat with cls token
                shape: (..., S + 1, D) with S = (HW)/(P^2) Example: (64, 65, 768)
        """

        # Get patches from images
        # patch shape: (..., S, NEW_C)
        patch = self.patches(images)

        # encoded_patches shape: (..., S, D)
        encoded_patches = self.projection(patch)

        batch_size = tf.shape(images)[0]

        hidden_size = tf.shape(encoded_patches)[-1]

        # cls_broadcasted shape: (..., 1, D)
        cls_broadcasted = tf.cast(
            tf.broadcast_to(self.cls_token, [batch_size, 1, hidden_size]),
            dtype=images.dtype,
        )

        # encoded_patches shape: (..., S + 1, D)
        encoded_patches = tf.concat([cls_broadcasted, encoded_patches], axis=1)

        # encoded_patches shape: (..., S + 1, D)
        encoded_patches = encoded_patches + self.position_embedding

        return encoded_patches
    
#######################################################################
        
from tensorflow.keras.layers import Layer, LayerNormalization, MultiHeadAttention, Dense, Dropout, Flatten
from tensorflow.keras import Sequential


class MLPBlock(Layer):
    def __init__(self, hidden_layers, dropout=0.1, activation='gelu'):
        """ MLP Block in Transformer Encoder
            Parameters
            ----------
            hidden_layers: Python array
                list of layers for mlp block
            dropout: float,
                dropout rate of mlp block
            activation: string
                activation of mlp layer
        """
        super(MLPBlock, self).__init__()

        layers = []
        for num_units in hidden_layers:
            layers.extend([
                Dense(num_units, activation=activation),
                Dropout(dropout)
            ])

        self.mlp = Sequential(layers)

    def call(self, inputs, *args, **kwargs):
        """ Pass output of multi-head attention to mlp block
            Parameters
            ----------
            inputs: tensor,
                multi-head attention outputs
                shape: (..., S, D). Example: (64, 100, 768)
            Returns
            -------
            outputs: tensor,
                attention + mlp outputs
                shape: (..., S, D). Example: (64, 100, 768)
        """

        outputs = self.mlp(inputs, *args, **kwargs)
        return outputs


class TransformerBlock(Layer):
    def __init__(self, num_heads, D, hidden_layers, dropout=0.1, norm_eps=1e-12):
        """ Transformer blocks which includes multi-head attention layer and mlp block
            Parameters
            ----------
            num_heads: int,
                number of heads of multi-head attention layer
            D: int, 
                size of each attention head for value
                        hidden_layers: Python array
                list of layers for mlp block
            dropout: float,
                dropout rate of mlp block
            norm_eps: float,
                eps of layer norm
        """
        super(TransformerBlock, self).__init__()
        # Attention
        self.attention = MultiHeadAttention(
            num_heads=num_heads, key_dim=D, dropout=dropout
        )
        self.norm_attention = LayerNormalization(epsilon=norm_eps)

        # MLP
        self.mlp = MLPBlock(hidden_layers, dropout)
        self.norm_mlp = LayerNormalization(epsilon=norm_eps)

    def call(self, inputs):
        """
            Pass Embedded Patches through the layers
            Parameters
            ----------
            inputs: tensor,
                Embedded Patches
                shape: (..., S, D). Example: (64, 100, 768)
            Returns
            -------
            outputs: tensor,
                attention + mlp outputs
                shape: (..., S, D). Example: (64, 100, 768)
        """
        # Feed attention
        norm_attention = self.norm_attention(inputs)

        attention = self.attention(query=norm_attention, value=norm_attention)

        # Skip Connection
        attention += inputs

        # Feed MLP
        outputs = self.mlp(self.norm_mlp(attention))

        # Skip Connection
        outputs += attention

        return outputs


class TransformerEncoder(Layer):
    def __init__(self, num_layers, num_heads, D, mlp_dim, dropout=0.1, norm_eps=1e-12):
        """
            Transformer Encoder which comprises several transformer layers
            Parameters
            ----------
            num_layers: int,
                number of transformer layers
                Example: 12
            num_heads: int,
                number of heads of multi-head attention layer
            D: int
                size of each attention head for value
            mlp_dim: 
                mlp size or dimension of hidden layer of mlp block
            dropout: float,
                dropout rate of mlp block
            norm_eps: float,
                eps of layer norm
        """
        super(TransformerEncoder, self).__init__()

        # Create num_layers of TransformerBlock
        self.encoder = Sequential(
            [
                TransformerBlock(num_heads=num_heads,
                                 D=D,
                                 hidden_layers=[mlp_dim, D],
                                 dropout=dropout,
                                 norm_eps=norm_eps)
                for _ in range(num_layers)
            ]
        )

    def call(self, inputs, *args, **kwargs):
        """
            Pass Embedded Patches through the layers
            Parameters
            ----------
            inputs: tensor,
                Embedded Patches
                shape: (..., S, D). Example: (64, 100, 768)
            Returns
            -------
            outputs: tensor,
                attention + mlp outputs
                shape: (..., S, D). Example: (64, 100, 768)
        """
        outputs = self.encoder(inputs, *args, **kwargs)
        return outputs

########################################################################
        
    
    
from tensorflow.python.keras.layers.core import Dropout
from tensorflow.keras.layers import Dense, LayerNormalization
from tensorflow.keras.layers.experimental.preprocessing import Resizing, RandomFlip, RandomRotation, RandomZoom, Rescaling
from tensorflow.keras import Sequential
from tensorflow.keras.models import Model


class ViT(Model):
    def __init__(self, num_layers=12, num_heads=12, D=768, mlp_dim=3072, num_classes=10, patch_size=16, image_size=224, dropout=0.1, norm_eps=1e-12):
        """
            VIT Model
            Parameters
            ----------
            num_layers: int,
                number of transformer layers
                Example: 12
            num_heads: int,
                number of heads of multi-head attention layer
            D: int
                size of each attention head for value
            mlp_dim: 
                mlp size or dimension of hidden layer of mlp block
            num_classes:
                number of classes
            patch_size: int
                size of a patch (P)
            image_size: int
                size of a image (H or W)
            dropout: float,
                dropout rate of mlp block
            norm_eps: float,
                eps of layer norm
        """
        super(ViT, self).__init__()
        # Data augmentation
        '''self.data_augmentation = Sequential([
            Rescaling(scale=1./255),
            Resizing(image_size, image_size),
            RandomFlip("horizontal"),
            RandomRotation(factor=0.02),
            RandomZoom(
                height_factor=0.2, width_factor=0.2
            ),
        ])
        '''
        
        self.resize = Resizing(height = image_size,width = image_size)

        # Patch embedding
        self.embedding = PatchEmbedding(patch_size, image_size, D)

        # Encoder with transformer
        self.encoder = TransformerEncoder(
            num_heads=num_heads,
            num_layers=num_layers,
            D=D,
            mlp_dim=mlp_dim,
            dropout=dropout,
            norm_eps=norm_eps,
        )

        # MLP head
        self.mlp_head = Sequential([
            LayerNormalization(epsilon=norm_eps),
            Dense(mlp_dim),
            Dropout(dropout),
            Dense(num_classes, activation='softmax'),
        ])

        self.last_layer_norm = LayerNormalization(epsilon=norm_eps)

    def call(self, inputs):
        # Create augmented data
        # resized shape: (..., image_size, image_size, c)
        resized = self.resize(inputs)

        # Create position embedding + CLS Token
        # embedded shape: (..., S + 1, D)
        embedded = self.embedding(resized)

        # Encode patchs with transformer
        # embedded shape: (..., S + 1, D)
        encoded = self.encoder(embedded)

        # Embedded CLS
        # embedded_cls shape: (..., D)
        embedded_cls = encoded[:, 0]
        
        # Last layer norm
        y = self.last_layer_norm(embedded_cls)
        
        # Feed MLP head
        # output shape: (..., num_classes)

        output = self.mlp_head(y)

        return output

class ViTTinyClass(ViT):
    def __init__(self, num_classes=10, patch_size=16, image_size=224, dropout=0.1, norm_eps=1e-12):
        super().__init__(num_layers=12, #depth
                         num_heads=3,
                         D=192, #embed_dim 
                         mlp_dim=768,#embed_dim*4
                         ## 4
                         num_classes=num_classes,
                         patch_size=patch_size,
                         image_size=image_size,
                         dropout=dropout,
                         norm_eps=norm_eps)    
        
class ViTSmall_8Class(ViT):
    def __init__(self, num_classes=10, patch_size=8, image_size=224, dropout=0.1, norm_eps=1e-12):
        super().__init__(num_layers=12, #depth
                         num_heads=6,
                         D=384, #embed_dim 
                         mlp_dim=1536,#embed_dim * mlp-ratio(= 4)
                         num_classes=num_classes,
                         patch_size=patch_size,
                         image_size=image_size,
                         dropout=dropout,
                         norm_eps=norm_eps) 
        
        
class ViTSmall_16Class(ViT):
    def __init__(self, num_classes=10, patch_size=16, image_size=224, dropout=0.1, norm_eps=1e-12):
        super().__init__(num_layers=12, #depth
                         num_heads=6,
                         D=384, #embed_dim 
                         mlp_dim=1536,#embed_dim * mlp-ratio(= 4)
                         num_classes=num_classes,
                         patch_size=patch_size,
                         image_size=image_size,
                         dropout=dropout,
                         norm_eps=norm_eps) 
        
class ViTSmall_32Class(ViT):
    def __init__(self, num_classes=10, patch_size=32, image_size=224, dropout=0.1, norm_eps=1e-12):
        super().__init__(num_layers=12, #depth
                         num_heads=6,
                         D=384, #embed_dim 
                         mlp_dim=1536,#embed_dim * mlp-ratio(= 4)
                         num_classes=num_classes,
                         patch_size=patch_size,
                         image_size=image_size,
                         dropout=dropout,
                         norm_eps=norm_eps) 
        
    
class ViTBase_8Class(ViT):
    def __init__(self, num_classes=10, patch_size=8, image_size=224, dropout=0.1, norm_eps=1e-12):
        super().__init__(num_layers=12, #depth
                         num_heads=12,
                         D=768, #embed_dim 
                         mlp_dim=3072,
                         ## 4
                         num_classes=num_classes,
                         patch_size=patch_size,
                         image_size=image_size,
                         dropout=dropout,
                         norm_eps=norm_eps)
        
class ViTBase_16Class(ViT):
    def __init__(self, num_classes=10, patch_size=16, image_size=224, dropout=0.1, norm_eps=1e-12):
        super().__init__(num_layers=12,
                         num_heads=12,
                         D=768, 
                         mlp_dim=3072,
                         num_classes=num_classes,
                         patch_size=patch_size,
                         image_size=image_size,
                         dropout=dropout,
                         norm_eps=norm_eps)
        
class ViTBase_32Class(ViT):
    def __init__(self, num_classes=10, patch_size=32, image_size=224, dropout=0.1, norm_eps=1e-12):
        super().__init__(num_layers=12, #depth
                         num_heads=12,
                         D=768, #embed_dim 
                         mlp_dim=3072,
                         ## 4
                         num_classes=num_classes,
                         patch_size=patch_size,
                         image_size=image_size,
                         dropout=dropout,
                         norm_eps=norm_eps)

class ViTLarge_14Class(ViT):
    def __init__(self, num_classes=10, patch_size=14, image_size=224, dropout=0.1, norm_eps=1e-12):
        super().__init__(num_layers=24,
                         num_heads=16,
                         D=1024,
                         mlp_dim=4096,
                         num_classes=num_classes,
                         patch_size=patch_size,
                         image_size=image_size,
                         dropout=dropout,
                         norm_eps=norm_eps)        
        

class ViTLarge_16Class(ViT):
    def __init__(self, num_classes=10, patch_size=16, image_size=224, dropout=0.1, norm_eps=1e-12):
        super().__init__(num_layers=24,
                         num_heads=16,
                         D=1024,
                         mlp_dim=4096,
                         num_classes=num_classes,
                         patch_size=patch_size,
                         image_size=image_size,
                         dropout=dropout,
                         norm_eps=norm_eps)
        
class ViTLarge_32Class(ViT):
    def __init__(self, num_classes=10, patch_size=32, image_size=224, dropout=0.1, norm_eps=1e-12):
        super().__init__(num_layers=24,
                         num_heads=16,
                         D=1024,
                         mlp_dim=4096,
                         num_classes=num_classes,
                         patch_size=patch_size,
                         image_size=image_size,
                         dropout=dropout,
                         norm_eps=norm_eps)

class ViTHuge_14Class(ViT):
    def __init__(self, num_classes=10, patch_size=14, image_size=224, dropout=0.1, norm_eps=1e-12):
        super().__init__(num_layers=32,
                         num_heads=16,
                         D=1280,
                         mlp_dim=5120,
                         num_classes=num_classes,
                         patch_size=patch_size,
                         image_size=image_size,
                         dropout=dropout,
                         norm_eps=norm_eps)
        

class ViTHuge_16Class(ViT):
    def __init__(self, num_classes=10, patch_size=16, image_size=224, dropout=0.1, norm_eps=1e-12):
        super().__init__(num_layers=32,
                         num_heads=16,
                         D=1280,
                         mlp_dim=5120,
                         num_classes=num_classes,
                         patch_size=patch_size,
                         image_size=image_size,
                         dropout=dropout,
                         norm_eps=norm_eps)
        
class ViTGaint_14Class(ViT):
    def __init__(self, num_classes=10, patch_size=14, image_size=224, dropout=0.1, norm_eps=1e-12):
        super().__init__(num_layers=40,
                         num_heads=16,
                         D=1408,
                         mlp_dim=6144,
                         num_classes=num_classes,
                         patch_size=patch_size,
                         image_size=image_size,
                         dropout=dropout,
                         norm_eps=norm_eps)
        
class ViTGaint_16Class(ViT):
    def __init__(self, num_classes=10, patch_size=16, image_size=224, dropout=0.1, norm_eps=1e-12):
        super().__init__(num_layers=40,
                         num_heads=16,
                         D=1408,
                         mlp_dim=6144,
                         num_classes=num_classes,
                         patch_size=patch_size,
                         image_size=image_size,
                         dropout=dropout,
                         norm_eps=norm_eps)
        

def ViTTiny(num_classes=10, input_shape=(None, 224, 224, 3)):
    model = ViTTinyClass(num_classes=num_classes)
    model.build(input_shape = input_shape)
    return model

def ViTSmall_8(num_classes=10, input_shape=(None, 224, 224, 3)):
    model = ViTSmall_8Class(num_classes=num_classes)
    model.build(input_shape=input_shape)
    return model

def ViTSmall_16(num_classes=10, input_shape=(None, 224, 224, 3)):
    model = ViTSmall_16Class(num_classes=num_classes)
    model.build(input_shape=input_shape)
    return model

def ViTSmall_32(num_classes=10, input_shape=(None, 224, 224, 3)):
    model = ViTSmall_32Class(num_classes=num_classes)
    model.build(input_shape=input_shape)
    return model

def ViTBase_8(num_classes=10, input_shape=(None, 224, 224, 3)):
    model = ViTBase_8Class(num_classes=num_classes)
    model.build(input_shape=input_shape)
    return model

def ViTBase_16(num_classes=10, input_shape=(None, 224, 224, 3)):
    model = ViTBase_16Class(num_classes=num_classes)
    model.build(input_shape=input_shape)
    return model

def ViTBase_32(num_classes=10, input_shape=(None, 224, 224, 3)):
    model = ViTBase_32Class(num_classes=num_classes)
    model.build(input_shape=input_shape)
    return model

def ViTLarge_14(num_classes=10, input_shape=(None, 224, 224, 3)):
    model = ViTLarge_14Class(num_classes=num_classes)
    model.build(input_shape=input_shape)
    return model

def ViTLarge_16(num_classes=10, input_shape=(None, 224, 224, 3)):
    model = ViTLarge_16Class(num_classes=num_classes)
    model.build(input_shape=input_shape)
    return model

def ViTLarge_32(num_classes=10, input_shape=(None, 224, 224, 3)):
    model = ViTLarge_32Class(num_classes=num_classes)
    model.build(input_shape=input_shape)
    return model

def ViTHuge_14(num_classes=10, input_shape=(None, 224, 224, 3)):
    model = ViTHuge_14Class(num_classes=num_classes)
    model.build(input_shape=input_shape)
    return model

def ViTHuge_16(num_classes=10, input_shape=(None, 224, 224, 3)):
    model = ViTHuge_16Class(num_classes=num_classes)
    model.build(input_shape=input_shape)
    return model

def ViTGaint_14(num_classes=10, input_shape=(None, 224, 224, 3)):
    model = ViTGaint_14Class(num_classes=num_classes)
    model.build(input_shape=input_shape)
    return model

def ViTGaint_16(num_classes=10, input_shape=(None, 224, 224, 3)):
    model = ViTGaint_16Class(num_classes=num_classes)
    model.build(input_shape=input_shape)
    return model

vesions=['ViTTiny',
        'ViTSmall_8', 'ViTSmall_16', 'ViTSmall_32',
        'ViTBase_8', 'ViTBase_16', 'ViTBase_32',
        'ViTLarge_14', 'ViTLarge_16', 'ViTLarge_32',
        'ViTHuge_14', 'ViTHuge_16',
        'ViTGaint_14', 'ViTGaint_16']
    
    

    