"""ktcdata URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from ktc_profile_site import views
from Taiwanese_PERM import views as tw_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^tw_perm/$', tw_views.index, name='tw_index'),
    url(r'^tw_perm/QA/$', tw_views.qa_page, name='qa_page'),
    url(r'^tw_perm/working/$', tw_views.working, name='working'),
    url(r'^test/', views.test, name='test'),
    url(r'^test2/', views.test2, name='test2'),
]
