"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, re_path
from first_app import views
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    url(r'^first_app/',include('first_app.urls')),
    path('admin/', admin.site.urls),

    re_path(r'^$',views.index,name='index'),
    path('index/season',views.index_season,name='index_season'),
    path('index/clean',views.index_clean,name='index_clean'),
    path('europa/',views.europa,name='europa'),
    path('eliminacje_LM',views.eliminacje_LM,name='eliminacje_LM'),
    path('eliminacje_LE',views.eliminacje_LE,name='eliminacje_LE'),
    path('eliminacje_ECL',views.eliminacje_ECL,name='eliminacje_ECL'),
    path('europa/eliminacje_season',views.eliminacje_season,name='eliminacje_season'),
    path('europa/season',views.europa_season,name='europa_season'),
    path('LM/',views.LM,name='LM'),
    path('LE/',views.LE,name='LE'),
    path('ECL/',views.ECL,name='ECL'),

    path('index/spadek',views.spadek,name='spadek'),
    path('ekstraklasa/',views.ekstraklasa,name='ekstraklasa'),
    path('puchar/',views.puchar_polski,name='puchar_polski'),
    path('pier_liga/',views.pier_liga,name='pier_liga'),
    path('druga_liga/',views.drug_liga,name='druga_liga'),

    #path('niemcy/',views.niemcy,name='niemcy'),
#    path('hiszpania/',views.hiszpania,name='hiszpania'),
    #path('francja/',views.francja,name='francja'),
    #path('wlochy/',views.wlochy,name='wlochy'),
    #path('anglia/',views.anglia,name='anglia'),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
