"""
URL configuration for djangoapils project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# Importa los módulos necesarios
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

# Define las rutas de tu aplicación
urlpatterns = [
    # Esta ruta lleva al panel de administración de Django
    path('admin/', admin.site.urls),

    # Esta ruta incluye todas las rutas definidas en el archivo urls.py de la aplicación 'api'
    path('api/v1/', include('api.urls')),

    # Esta ruta lleva a la documentación generada automáticamente para tu API
    path('docs/', include_docs_urls(title='API_Documentation'))
]
