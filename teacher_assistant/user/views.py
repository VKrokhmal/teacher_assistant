from django.http import (
    HttpResponse,
    HttpRequest,
)
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *


def index(request: HttpRequest) -> HttpResponse:
    users = User.objects.filter(first_name="Vitalii")
    out = [i.__dict__ for i in users]

    return render(
        request,
        "user/index.html",
        context={"user": out},
    )


class AllUsers(ListView):
    model = User
    template_name = "user/index.html"
    context_object_name = "user"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total"] = User.objects.count()
        return context


class UserView(DetailView):
    model = User
    template_name = "user/user_detail.html"
    context_object_name = "user"
