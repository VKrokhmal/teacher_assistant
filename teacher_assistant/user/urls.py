from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from user import views
from user.views import AllUsers, UserView

app_name = "user"

urlpatterns = [
    path("", AllUsers.as_view(), name="index"),
    path("<int:pk>/", UserView.as_view(), name="detail"),
]
