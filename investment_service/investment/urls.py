from django.urls import path

from . import views

urlpatterns = [
    path("", views.InvetmentView.as_view(), name="investment_view"),
]
