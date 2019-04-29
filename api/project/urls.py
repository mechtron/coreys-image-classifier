"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import (
    include,
    url,
)
from django.contrib import admin

from classifier.views import CreateClassification
from healthcheck.views import HealthCheck
from report.views import CreateReport
from secret.views import Secret


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.authtoken')),
    url(
        r'^classify-image',
        CreateClassification.as_view(),
        name='classify-image',
    ),
    url(r'^health', HealthCheck.as_view(), name='healthcheck'),
    url(r'^report', CreateReport.as_view(), name='report'),
    url(r'^secret', Secret.as_view(), name='secret'),
]
