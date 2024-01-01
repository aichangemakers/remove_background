from PIL import Image
from rembg import remove
import streamlit as st

"""
## Removal background by [AIChangeMakers](https://www.linkedin.com/company/ai-changemakers/)
"""
st.markdown('---')
image = st.file_uploader('Chargez votre image ici', type=['jpeg', 'jpg', 'png'])
if image is not None:
    st.image(image, caption='Image avec background')
    choix_modifier = st.sidebar.checkbox(
        'Cochez cette case si vous voulez modifier la taille de l\'image sans background')
    if choix_modifier:
        max = st.sidebar.slider('Choisissez une valeur pour la largeur', max_value=1024, min_value=640, value=None)
        min = st.sidebar.slider('Choisissez une valeur pour la hauteur', max_value=1024, min_value=640, value=None)
        input_img = Image.open(image)
        input_img = input_img.resize((max, min))
        output_img = remove(input_img)
        output_img.save('Resultat.png')
        st.image(output_img, caption='Image sans background avec la taille modifiée')
        with open("Resultat.png", "rb") as file:
            btn = st.download_button(label="Download image", data=file, file_name="Result.png", mime="image/png")
    else:
        input_img = Image.open(image)
        output_img = remove(input_img)
        output_img.save('Resultat.png')
        st.image(output_img, caption='Image sans background avec la taille originale')
        with open("Resultat.png", "rb") as file:
            btn = st.download_button(label="Download image", data=file, file_name="Result.png", mime="image/png")

