from django.http import (
    HttpResponse,
    HttpRequest,
)
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    lessons = ["Math", "English", "Geometry"]
    return render(
        request,
        "lessons/index.html",
        context={"lessons": lessons},
    )
