from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views.generic.base import RedirectView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework import routers

schema_view = get_schema_view(
    openapi.Info(
        title="Todo API",
        default_version="v1",
        description="A todo list API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()

urlpatterns = [
    path("docs.yaml", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("docs.json", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("api-auth/", include("rest_framework.urls")),
    path("", RedirectView.as_view(url="redoc/", permanent=False), name="index"),
    path("api/", include("core.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.ENABLE_ADMIN:
    urlpatterns.insert(0, path("admin/", admin.site.urls))
