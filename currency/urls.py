from django.urls import path

from currency import views

urlpatterns = [
    path('currency/convert/', views.convert_currency, name='convert_currency'),
]