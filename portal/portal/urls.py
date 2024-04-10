from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='inicio'),
    path('ingreso/', views.ingreso, name="ingreso"),
    path('', include('portal_app.urls'))
]