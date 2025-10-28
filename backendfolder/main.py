from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for testing (change in production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Load the trained model and vectorizer
model = joblib.load('logistic_regression_model.pkl')  # Replace with your model file
vectorizer = joblib.load('vectorizer.pkl')  # Replace with your vectorizer file

# Define the input structure using Pydantic
class TextInput(BaseModel):
    text: str

# Preprocessing function (wordopt)
def wordopt(text):
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r"\\W", "", text)
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'<.*?>+', '', text)
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub(r'\n', '', text)
    text = re.sub(r'\w*\d\w*', '', text)
    return text

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello! Your FastAPI server is working 🎉"}

# Define a route for prediction
@app.post("/predict/")
def predict(input_data: TextInput):
    processed_text = wordopt(input_data.text)
    vectorized_text = vectorizer.transform([processed_text])
    
    # Get the prediction and probability
    prediction = model.predict(vectorized_text)
    probability = model.predict_proba(vectorized_text).max()  # Get highest confidence score
    
    # Format confidence as a percentage
    confidence_percentage = f"{round(probability * 100, 2)}%"

    # Format the response
    label = "Fake News" if prediction[0] == 0 else "Not a Fake News"
    return {"prediction": label, "confidence": confidence_percentage}

