import streamlit as st
import pickle 
import numpy as np

def load_model():
    with open('svm_model.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()


def show_predict_page():
    st.title("Cyberbullying Detection")
    