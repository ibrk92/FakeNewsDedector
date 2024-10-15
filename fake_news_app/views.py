from django.shortcuts import render
import joblib
from .forms import NewsArticleForm  # Formu import etmeyi unutmayın

# Model ve vektörleştiriciyi yükleyin
model = joblib.load(r'C:\Users\ibrah\fakeNewsWeb\fake_news_app\model_files\model.joblib')  # Model dosyasının yolu
vectorizer = joblib.load(r'C:\Users\ibrah\fakeNewsWeb\fake_news_app\model_files\vectorizer.joblib')  # Vectorizer dosyasının yolu

def submit_article(request):
    result = None  # Başlangıç değeri None olacak
    form = NewsArticleForm()  # Formu GET isteği için oluşturun

    if request.method == 'POST':
        form = NewsArticleForm(request.POST)
        if form.is_valid():
            # Kullanıcıdan gelen text'i al
            text = form.cleaned_data['text']

            # Text'i TF-IDF ile dönüştür
            text_transformed = vectorizer.transform([text])

            # Prediction işlemi
            prediction = model.predict(text_transformed)

            #print(f'Transformed Text: {text_transformed}')  # Dönüştürülen metni yazdır
            #print(f'Prediction: {prediction}')  # Tahmin sonucunu yazdır

            # Tahmin sonucunu belirle
            result = "Real" if prediction[0] == 1 else "Fake"

    return render(request, 'submit_article.html', {'form': form, 'result': result})
