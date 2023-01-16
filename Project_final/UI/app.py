#Imports
import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie


#JSON method for animation
def lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


#Assets
img = Image.open("icon.png")
AntiRumour = Image.open('images/machine-learning.jpg')
lottie_animation = lottie_url('https://assets4.lottiefiles.com/packages/lf20_l0segmbm.json')
lottie_Fake = lottie_url('https://assets1.lottiefiles.com/private_files/lf30_cbizhsdy.json')
lottie_happy = lottie_url('https://assets8.lottiefiles.com/packages/lf20_ggw4qc1o.json')

#Config
st.set_page_config(page_title = 'AntiRumour', page_icon = img)

#Header
st.subheader('AntiRumour')
st.title('Introduction')

#Body
intro = 'This website is designed for Deep Learning course given by Dr.Mürsel Taşgin\
    where I aim to showcase all the related projects in the website\n\
    _Deep learning_ received a lot of success in many research areas from image processing to\
    voice recognition. Nowadays, the knowledge in deep learning has become the number one skill\
    to deal with artificial intelligence related tasks. Our aim with this course is to make our \n\
    students earn the ability to deal with modern problems in machine learning.'
st.image(AntiRumour)
st.write(intro)

#Container
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Projects")
        st.write("##")
        st.write(''' 
                 - Fake news detection: ML that aims to limit the spread of fake news by grading the\
                     trustwothiness of the news articles
                 - Sentiment Analysis: ML that aims to grade the positivity of the news
                 - News Summary: if you're like me and you're lazy to read lengthy news articles then this\
                     ML will summarize it for you!
                 - MyNews: is a platform that will show your daily news and uses filtering and user behavior to filter\
                 the news based on your intrest by including all the following ML above and more 
                 ''')

    with right_column:
        st_lottie(lottie_animation, height=300, key='Fake_news')
        

# Projects
with st.container():
    st.write('---')
    st.header('Showcase')
    st.write('##')
    image_column, text_column = st.columns((1,2))
    with image_column:
        st_lottie(lottie_Fake, height=300, key='Coding')
    
    with text_column:
        st.subheader('Fake News Detection')
        st.write('''
                 Machine Learning To grade Trustworthiness of news articles\n
                 [Github Repository :computer:>] (https://github.com/ayman-codes/Deep_Learning)\n
                 [Try it out yourself! :fire:>] (https://820aef56-fe45-4df7.gradio.live)   
                 ''')
        
with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st_lottie(lottie_happy, height=200, key='Happy')
        
    with text_column:    
        st.subheader('Sentiment Anlysis')
        st.write('''
                 Check the positivity of the news article\n
                 [Github Repository :computer:>] (https://github.com/ayman-codes/Deep_Learning)\n
                 [Try it out yourself! :fire:>] (https://820aef56-fe45-4df7.gradio.live)   
                 ''')
