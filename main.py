import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from skimage.io import imread


# download the image
img_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Mount_Fuji_from_Mount_Aino.jpg/640px-Mount_Fuji_from_Mount_Aino.jpg'

im = imread(img_url)

st.image(im, caption='image from wikimedia commons',
         use_column_width=True)


# show histgram of all colors
hist_red, _ = np.histogram(im[:, :, 0], bins=64)
hist_green, _ = np.histogram(im[:, :, 1], bins=64)
hist_blue, _ = np.histogram(im[:, :, 2], bins=64)
# hist = np.stack((hist_red, hist_green, hist_blue), axis=1)

# df_hist = pd.DataFrame(hist, columns=['R', 'G', 'B'])
# st.bar_chart(df_hist)

colors = ['red', 'green', 'blue']
labels = ['R', 'G', 'B']
hist_data = [hist_red, hist_green, hist_blue]

fig, ax = plt.subplots()
for i, data in enumerate(hist_data):
    ax.bar(np.arange(len(data)), data, color=colors[i], label=labels[i])


# choose one color
color = st.radio(
    "choose R, G, or B",
    ('R', 'G', 'B'))
if color == 'R':
    fig, ax = plt.subplots()
    ax.bar(np.arange(len(hist_red)), hist_red, color='red')
    ax.set_title('Histogram of Red Color')
    st.pyplot(fig)
if color == 'G':
    fig, ax = plt.subplots()
    ax.bar(np.arange(len(hist_green)), hist_green, color='green')
    ax.set_title('Histogram of Green Color')
    st.pyplot(fig)
if color == 'B':
    fig, ax = plt.subplots()
    ax.bar(np.arange(len(hist_blue)), hist_blue, color='blue')
    ax.set_title('Histogram of Blue Color')
    st.pyplot(fig)

