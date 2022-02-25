import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.image import load_img
import pathlib
import zipfile


with zipfile.ZipFile("object.zip","r") as zip_ref:
    zip_ref.extractall("")

data_dir = pathlib.Path("object")
image_count = len(list(data_dir.glob('*/*.*')))
print(image_count)
circle = list(data_dir.glob('circle/*'))
PIL.Image.open(str(circle[0]))

shadedcircle = list(data_dir.glob('shadedcircle/*'))
PIL.Image.open(str(shadedcircle[0]))
