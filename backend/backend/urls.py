"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


urlpatterns = [
    path("", include("demo_app.urls")),
    # Django
    path("admin/", admin.site.urls),
    path("api/", include("rest_framework.urls", namespace="rest_framework")),
    # Documentation
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"
    ),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    # Apps
    path("authx/", include("authx.urls", namespace="authx")),
    path("trip/", include("trip.urls", namespace="trip")),
    path("locations/", include("locations.urls", namespace="locations")),
    path("services/", include("services.urls", namespace="services")),
    path("journal/", include("journal.urls", namespace="journal")),
    path("expense/", include("expense.urls", namespace="expense")),
    path("analytics/", include("analytics.urls", namespace="analytics")),
    path("contacts/", include("contacts.urls", namespace="contacts")),
]
