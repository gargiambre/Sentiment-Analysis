import streamlit as st
import pickle
import time

# Set page configuration
st.set_page_config(
    page_title='Twitter Sentiment Analysis',
    page_icon=':bar_chart:',
    layout='wide',
    initial_sidebar_state='auto',
)

# Load the model
model = pickle.load(open('twitter_sentiment.pkl', 'rb'))

# Apply external CSS file for styles
css = """
<link rel="stylesheet" href="styles.css">
"""
st.markdown(css, unsafe_allow_html=True)

# Add some effects
st.title('Twitter Sentiment Analysis')
st.markdown('## Analyze the sentiment of your tweets!')

tweet = st.text_input('Enter your tweet')

# Add prediction button
submit = st.button('Predict', key='predict_button')

if submit:
    with st.spinner('Predicting...'):
        time.sleep(2)  # Simulating prediction time
        prediction = model.predict([tweet])
    st.success('Prediction time taken: 2 seconds')
    st.write('Prediction:', prediction[0])

