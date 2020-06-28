import json
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from wordcloud import WordCloud
from PIL import Image

# Creating a Title
st.title("Personality Cloud")

# Create Personality Options
with open("apps/personality_adjectives.json", "r") as p_adj:
    p_adjectives = json.load(p_adj)['adjectives']

adjective_options = st.multiselect(f"How do you describe your personality?: ", p_adjectives)

if len(adjective_options) != 0:
    personality_cloud = WordCloud(background_color='lightblue').generate(" ".join(adjective_options))
    plt.figure(figsize=(20,20))
    plt.imshow(personality_cloud, interpolation='bilinear')
    plt.axis("off")
    st.pyplot()
