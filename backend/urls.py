"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)


def home(request):
    return HttpResponse(
        """
                        <style>*{font-size:2rem;padding:0.5rem 1.2rem;font-weight:700;cursor: pointer;}</style>
                        <div style='text-align:center;'>
                        <p>Server is Runing!</p>
                        <a href='/api/docs/swagger/'><button>Swagger</button></a>
                        <a href='/api/docs/redoc/'><button>Redoc</button></a>
                        </div>
        """
    )


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("orders/", include("orders.urls")),
    path("products/", include("products.urls")),
    path("users/", include("users.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/swagger/", SpectacularSwaggerView.as_view(), name="swagger-ui"),
    path("api/docs/redoc/", SpectacularRedocView.as_view(), name="redoc"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
