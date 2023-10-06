"""
URL configuration for gameserver project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("characters/", include("api.v1.character.urls")),  # Tiene 1 view
    path("clan/", include("api.v1.clan.urls")),
    path("items/", include("api.v1.item.urls")),
    path("inventory/", include("api.v1.inventory.urls")),
    path("location/", include("api.v1.location.urls")),
    path("npc/", include("api.v1.npc.urls")),
    path("auth/", include("api.v1.auth.urls")),
]
