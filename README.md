# Fake News Detector 


## Project Description
Fake News Detector is a web application that helps users evaluate the authenticity of news articles. It utilizes machine learning techniques to detect fake news using a trained model.

## Features
- User-friendly interface
- Ability to distinguish between real and fake news
- Supported by an advanced machine learning model using **Logistic Regression**
- Utilizes advanced **Word-level TF-IDF** vectorization method for feature extraction


## Installation

### Requirements
- Python 3.x
- Django
- Scikit-learn
- Joblib

### Steps

1. **Clone the Repository**
   ```bash
   git clone [https://github.com/ibrk92/FakeNewsDedector.git](https://github.com/ibrk92/FakeNewsDedector.git)
   cd FakeNewsDedector

2. **Create a Virtual Environment (Optional)**
 ```bash
 python -m venv venv
 source venv/bin/activate  # On macOS/Linux
 venv\Scripts\activate     # On Windows

3. **Install Required Packages**
 ```bash
 pip install -r requirements.txt

4. **Run Migrations**
 ```bash
 python manage.py migrate

5. **Run the Development Server**
 ```bash
 python manage.py runserver

### Notes
Make sure to set up the correct environment variables if needed.
You can access the application by navigating to http://127.0.0.1:8000/ in your web browser.

## Screenshots

### Real News Screenshot
![Real News](screenshots/detector_real.png)

### Fake News Screenshot
![Fake News](screenshots/detector_fake.png)

## Model Accuracy

The accuracy of our model using Word Level TF-IDF is approximately **0.7747**. This accuracy is derived from a text dataset consisting of **66,301 entries** and is dependent on the words used in that dataset. 

This means that the model may not always accurately distinguish between fake and real news, as its performance relies on the word groups learned from this specific dataset. However, the model can be improved. Therefore, it is crucial to consider this aspect when working with natural language processing models.

