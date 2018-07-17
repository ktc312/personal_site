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
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^data/$', views.data, name='data'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^stock_project/$', views.stock_project, name='stock_project'),
    url(r'^regression_for_dummies/$', views.regression_for_dummies, name='regression_for_dummies'),
    url(r'^tw_perm/$', tw_views.index, name='tw_index'),
    url(r'^tw_perm/QA/$', tw_views.qa_page, name='qa_page'),
    url(r'^tw_perm/working/$', tw_views.working, name='working'),

    url(r'^resume/$', views.resume, name='resume')
]
