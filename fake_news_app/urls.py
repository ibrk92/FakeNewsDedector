from django.urls import path
from .views import submit_article

urlpatterns = [
    path('', submit_article, name='home'),  # Ana sayfa
]
