from django.urls import path

from urls.views import UrlView

urlpatterns = [
    path("url/", UrlView.as_view()),
]
