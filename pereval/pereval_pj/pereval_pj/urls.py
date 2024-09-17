"""
URL configuration for pereval_pj project.

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
from django.urls import path, include
from rest_framework import routers
from pereval_app import views
from django.urls import path
from pereval_app.swagger import schema_view

from pereval_app.views import AddedFromEmailView



router = routers.DefaultRouter()
# router.register(r'level', views.LevelViewSet)
# router.register(r'users', views.UsersViewSet)
# router.register(r'coords', views.CoordsViewSet)
router.register(r'images', views.ImagesViewSet)
router.register(r'added', views.AddedViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/submitData/', include(router.urls)),
    path('api/submitData/user__email=<str:email>', AddedFromEmailView.as_view(), name='user__email'),
    path('swagger/', schema_view.with_ui('swagger',
                                         cache_timeout=0), name='schema-swagger-ui'),
]
