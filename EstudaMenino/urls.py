"""EstudaMenino URL Configuration
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # para url vazia - executar a home - da pasta core - arq view
    url(r'', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
