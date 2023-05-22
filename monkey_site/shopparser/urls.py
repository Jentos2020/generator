from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [ 
    path('', views.shopParse, name='display-data'),
    path('stat/', views.statView),
]  + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)