from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from boss_media_group.apps.parser.astana_hub_parser import astana_hub_parser
from boss_media_group.apps.parser.models import TechCompany
from boss_media_group.apps.parser.serializers import TechCompanySerializer


@extend_schema(
    summary="Получить данные с парсера Astana Hub",
    description="Запрашивает страницу технопарка, извлекает первые 10 компаний, "
                "сохраняет их в БД и возвращает список названий.",
    tags=["Astana Hub"],
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def run_astana_hub_parser(request):
    company_names = astana_hub_parser()
    for company_name in company_names:
        name, created = TechCompany.objects.get_or_create(name=company_name)
    return Response({'company_names': company_names})

@extend_schema(
    summary="Получить сохранённые имена компании",
    description="Возвращает все компании, собранные парсером Astana Hub.",
    tags=["Astana Hub"],
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_tech_companies(request):
    tech_companies = TechCompany.objects.all()
    serializer = TechCompanySerializer(tech_companies, many=True)
    return Response(serializer.data)

