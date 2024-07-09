from django.http import (
    HttpResponse,
    HttpRequest,
)
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    users = {"John": {"age": 23}, "Nancy": {"age": 24}}
    return render(
        request,
        "user/index.html",
        context={"user": users},
    )
