from django.urls import path
from apart_menago.views import MyFormView
from . import views

urlpatterns = [
    path("", MyFormView.as_view()),
]
