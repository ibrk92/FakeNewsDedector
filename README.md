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

4. **Install Required Packages**
   ```bash
   pip install -r requirements.txt

6. **Run Migrations**
   ```bash
   python manage.py migrate

7. **Run the Development Server**
   ```bash
   python manage.py runserver

### Notes
Make sure to set up the correct environment variables if needed.
You can access the application by navigating to http://127.0.0.1:8000/ in your web browser.

## Screenshots

### Real News Screenshot
![Real News](screenshots/dedector_real.png)

### Fake News Screenshot
![Fake News](screenshots/dedector_fake.png)

## Model Development

In the development of the machine learning model, I explored various feature engineering techniques to optimize performance. The following methods were utilized:

- **Count Vectors**
- **TF-IDF**
  - **Word Level**
    - Achieved the highest accuracy of **77.47%**
  - **n-gram Level**
  - **Character Level**
I initially considered using Apache Spark for processing the dataset but encountered challenges with implementing lemmatization. Consequently, I opted for **Pandas** for data manipulation, and selected **Logistic Regression** as my final model due to its superior accuracy compared to other methods.

By applying these techniques and approaches, I aimed to enhance the model's capability to accurately identify fake news, while remaining open to future improvements and refinements.

## Model Accuracy

The model's performance was assessed using cross-validation scores, providing a reliable measure of its accuracy and ensuring that the results are consistent across different subsets of the dataset. 

The accuracy of our model using **Word Level TF-IDF** is approximately **0.7747**. This accuracy is derived from a text dataset consisting of **66,301 entries** and a total of **7,674,275 words**. 

This means that the model may not always accurately distinguish between fake and real news, as its performance relies on the word groups learned from this specific dataset. However, the model can be improved. Therefore, it is crucial to consider this aspect when working with natural language processing models.

## Model Performance

### Confusion Matrix
![Confusion Matrix](path/to/confusion_matrix.png)

### Classification Report
![Classification Report](path/to/classification_report.png)
 
