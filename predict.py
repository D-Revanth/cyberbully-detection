import streamlit as st
import pickle 
from sklearn.feature_extraction.text import TfidfVectorizer
from PIL import Image


def load_model():
    with open('D:/College/Mini Project/svm.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

def show_predict_page():
    st.title("Cyberbullying Detection")
    
    user_input = st.text_input("Enter some text:", "")
    ok = st.button("Check")
    
    if ok and user_input: 

        model = load_model()
        

        with open('D:/College/Mini Project/tfidf_vectorizer.pkl', 'rb') as file:
            tfidf_vectorizer = pickle.load(file)
        

        X_test_tfidf = tfidf_vectorizer.transform([user_input])  # Note: Pass user input as a list
        

        prediction = model.predict(X_test_tfidf)
        

        if prediction == 'Offensive' :
            st.write("You are being Offensive ☹️")
            image = Image.open("D:\College\Mini Project\offensive1.jpg")
            st.image(image, use_column_width=True)

        else:
            st.write("You are not being Offensive 😊")
            image2 = Image.open("D:/College/Mini Project/nonoffensive1.jpg")
            st.image(image2, use_column_width=True)
