"""
Definition of urls for DjangoWebProject27.
"""

from datetime import datetime
from app import views
from django.conf.urls import url, include
import django.contrib.auth.views
from django.conf.urls.static import static

#import app.forms
import app.views
from app.views import *

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
from django.contrib import admin
from django.conf.urls import include, url
admin.autodiscover()

urlpatterns = [
    # Examples:
    #url(r'^$', app.views.post, name='post'),
    #url(r'^admin$', admin.site.urls),
   # url(r'^Post$', include("Post.urls", namespace='Post')),
    url(r'^$', app.views.index, name='index'),
    url(r'^(?P<id>\d+)$', app.views.post_detail, name='post_detail'),
     #url(r'^form_detail$', app.views.form_detail, name='form_detail'),
    #url(r'^home$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about$', app.views.about, name='about'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
           # 'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
      url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
      url(r'^admin/', include(admin.site.urls)),
]
