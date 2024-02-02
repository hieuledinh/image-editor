import streamlit as st # for creating webapp 
import cv2 as cv 
from PIL import Image, ImageEnhance
import numpy as np 
import os 

def main():
  
  activities = ['Detection', 'About']
  choices = st.sidebar.selectbox('Select Activity', activities)

  if choices == 'Detection':
    st.title('Image Editing App')
    st.text('Edit your images in a fast and simple way')
    st.subheader('Face Detection')
    image_file = st.file_uploader('Upload Image', type=(['png', 'jpeg', 'jpg']))
    
    if image_file is not None:
      our_image = Image.open(image_file)
      st.text('Original Image')
      st.image(our_image)

      enhance_type = st.sidebar.radio('Enahance Type', ['Original','Gray-scale', 'Contrast', 'Brightness'])

      # if enhance_type == 'Original':
      #   st.text('Original Image')
      #   st.image(our_image)

      if enhance_type == 'Gray-scale':
        img = np.array(our_image.convert('RGB'))
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        st.text('Grey Scale Image')
        st.image(gray)

      elif enhance_type == 'Contrast':
        rate = st.sidebar.slider('Contrast Level', 0.0, 6.0)
        enhancer = ImageEnhance.Contrast(our_image)
        enhanced_image = enhancer.enhance(rate)
        st.image(enhanced_image)

      elif enhance_type == 'Brightness':
        rate = st.sidebar.slider('Brightness Level', 0.0, 8.0)
        enhancer = ImageEnhance.Brightness(our_image)
        enhanced_image = enhancer.enhance(rate)
        st.image(enhanced_image)

        
      
         
  elif choices == 'About':
    st.subheader('About Information Developer')
    st.markdown('Build with Streamlit by [HieuLeDinh](https://linktr.ee/hieulee.tnc)')
    st.text('My name is Hieu I am a student at HCMUT')

if __name__ == "__main__":
  main()