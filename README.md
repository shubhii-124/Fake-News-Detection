# Fake-News-Detection


## Overview
This project is a **Fake News Detection** system that uses **Machine Learning** models to classify news as *Fake* or *Not Fake*. It takes a news article as input, processes the text, vectorizes it, and then predicts whether the news is real or fake using multiple classification models.

## Features
- Preprocesses text data for analysis
- Uses **TF-IDF Vectorization** for feature extraction
- Implements multiple **Machine Learning models**:
  - Logistic Regression (LR)
  - Decision Tree (DT)
  - Gradient Boosting Classifier (GBC)
  - Random Forest Classifier (RFC)
- Provides predictions from multiple models for comparison

## Dataset
The dataset consists of two categories:
- `Fake News` dataset containing false articles
- `Real News` dataset containing authentic articles

## Installation
### Prerequisites
Make sure you have Python installed. You can install the required dependencies using:
```bash
pip install -r requirements.txt
```

### Required Libraries
- `pandas`
- `numpy`
- `sklearn`

## How to Run the Project
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/fake-news-detection.git
   cd fake-news-detection
   ```
2. Run the Jupyter Notebook:
   ```bash
   jupyter notebook "FAKE NEWS DETECTION.ipynb"
   ```
3. Alternatively, run the script in the terminal:
   ```bash
   python fake_news_detection.py
   ```
4. Enter a news article when prompted to test the model.

## Usage Example
```python
news = "Breaking: Scientists discover a new planet!"
manual_testing(news)
```
**Output:**
```
LR Prediction: Not a Fake News
DT Prediction: Not a Fake News
GBC Prediction: Not a Fake News
RFC Prediction: Not a Fake News
```

## Contributing
Feel free to contribute to this project! If you find any bugs or have feature requests, open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

## Acknowledgments
- Kaggle dataset on Fake News
- Scikit-Learn for Machine Learning models

