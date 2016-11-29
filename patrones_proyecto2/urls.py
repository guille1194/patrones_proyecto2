from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'patrones_proyecto2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    ]
