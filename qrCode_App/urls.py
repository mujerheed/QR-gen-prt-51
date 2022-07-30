
from django.urls import path
from .views import HomePageView, LoginPageView
urlpatterns = [
    path('', HomePageView.as_view(), name='Index'),
]
