from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from boss_test.apps.authentification.views import EmailTokenObtainPairView, RegisterView

router = DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    path("authentification/register/", RegisterView.as_view(), name="register"),
    path("authentification/login/", EmailTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("authentification/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
