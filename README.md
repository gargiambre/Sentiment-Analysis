# Sentiment-Analysis of Twitter Dataset
In this project, we delve into understanding the sentiment expressed in tweets through the lens of machine learning. Our goal is to effectively classify tweets into positive, negative, or neutral sentiments utilizing a combination of Random Forest classification and TF-IDF (Term Frequency-Inverse Document Frequency) vectorization techniques.

# Methodology
Key steps of the system design are:
1) Data Collection: The data is collected from twitter such as comments, hashtags, and tweets and then this collected data is converted into CSV file format for model to work with it.
2) Data Preprocessing: We perform thorough data cleaning and preprocessing on the Twitter dataset to ensure quality and consistency in our analysis. In this step the dataset is pre-processed as in the dataset gets cleaned which is it removes the null/missing values to get the most accurate prediction of the sentiments.
3) Classification of text: In this step natural language processing (NLP) unravels the text structure, and then system matches the words with the lexicon dictionary of pre-scored emotions which classifies the text sentiment with the matching scores.
4) Classified text: In this step predicted sentiments gets weights assigned to words based on their importance by TF-IDF and then Random Forest uses these weights to analyze the text features. This combine approch helps to predict the final sentiment which is positive, negative and neutral
4) Feature Extraction: Using TF-IDF vectorization, we extract relevant features from the text data, transforming it into numerical representations suitable for machine learning algorithms.
5) Model Training: Leveraging Random Forest classification, we train a robust model capable of accurately predicting sentiment labels for tweets.
6) Model Evaluation: We assess the performance of our trained model using appropriate evaluation metrics to ensure its effectiveness in sentiment classification.

# Repository Contents
In this repository, you'll find:

Jupyter Notebook: Contains the code for data preprocessing, feature extraction, model training, and evaluation.
Datasets: The Twitter dataset used for sentiment analysis.
README: Provides an overview of the project and instructions for running the code.
app.py: Python file for deploying the trained model into a Streamlit web application.
