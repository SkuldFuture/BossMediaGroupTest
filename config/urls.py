from django.contrib import admin
from django.http.response import JsonResponse
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("boss_media_group.apps.authentification.urls")),
    path('api/', include('boss_media_group.apps.tasks.urls')),
    path('api/', include('boss_media_group.apps.parser.urls')),
    # path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('', lambda request: JsonResponse({'message': 'API is working, go to /api/docs/ for documentation and /admin for admin panel.'})),
]
