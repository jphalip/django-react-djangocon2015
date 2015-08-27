from django.conf.urls import url
from django.views.generic import RedirectView

from photos.views import ajax_hydration, serialized_hydration, pre_rendered


urlpatterns = (
    url(r'^$', RedirectView.as_view(url='/ajax/', permanent=False)),
    url(r'^ajax/$', ajax_hydration),
    url(r'^serialized/$', serialized_hydration),
    url(r'^pre-rendered/$', pre_rendered),
)
