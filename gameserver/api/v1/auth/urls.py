from django.urls import path

from api.v1.auth.views import TokenObtainView


urlpatterns = [
    path("token/", TokenObtainView.as_view(), name="token_obtain_pair"),
]
