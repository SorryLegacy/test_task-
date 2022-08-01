from django.urls import path
from .views import UserUrl, UrlShotener, RedirectUrl


urlpatterns = [
    path("profile", UserUrl.as_view(), name="profile"),
    path("", UrlShotener.as_view(), name="shotener"),
    path("app/<str:short>", RedirectUrl.as_view(), name="redirect")
]