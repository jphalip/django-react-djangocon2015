from django.conf import settings
from django.conf.urls import include, url


from photos.api import router


urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'', include('photos.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', 'django.contrib.staticfiles.views.serve'),
    ]