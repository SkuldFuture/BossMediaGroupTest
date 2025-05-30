from django.urls import path
from rest_framework.routers import DefaultRouter

from boss_test.apps.parser.views import get_tech_companies, run_astana_hub_parser

router = DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    path("tech-companies/parser", run_astana_hub_parser, name='run_astana_hub_parser'),
    path("tech-companies/", get_tech_companies, name='tech_companies'),
]
