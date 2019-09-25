from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app import views
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register('post', views.PostView, 'post')


class HomeTemplateView(TemplateView):
    template_name = 'index.html'


urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]