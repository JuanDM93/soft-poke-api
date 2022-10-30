from django.contrib import admin
from django.urls import path, include, re_path

# Docs
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Soft-PokeTeams API",
        default_version='v1',
        description="Technical Rest API test",
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

docs_patterns = [
    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'
    ),
    re_path(
        r'^swagger/$',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    re_path(
        r'^redoc/$',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    ),
]

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/trainers/', include('trainers.urls')),
    path('api/teams/', include('teams.urls')),

    path('api/docs/', include(docs_patterns)),
]
