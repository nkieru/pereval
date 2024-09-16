from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


api_info = openapi.Info(
        title="API_pereval",
        default_version='v1',
    )

schema_view = get_schema_view(
    api_info,
    public=True,
    permission_classes=(permissions.AllowAny,),
)
