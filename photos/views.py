import json

from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
from react.render import render_component

from photos.models import Photo, Favorite
from photos.api import PhotoSerializer, FavoriteSerializer


def ajax_hydration(request):
    return render(request, 'ajax.html')


def serialized_hydration(request):
    photos = PhotoSerializer(Photo.objects.all(), many=True)
    favorites = FavoriteSerializer(Favorite.objects.all(), many=True)
    return render(request, 'serialized.html', {
        'data': json.dumps({
            'photos': photos.data,
            'favorites': favorites.data,
        }, cls=DjangoJSONEncoder)
    })


def pre_rendered(request):
    photos = PhotoSerializer(Photo.objects.all(), many=True)
    favorites = FavoriteSerializer(Favorite.objects.all(), many=True)

    # Render HTML output by React server
    rendered_html = render_component(
        'js/components/album.js',
         props = {
           'photos': photos.data,
           'favorites': favorites.data,
         }
    )

    return render(request, 'pre-rendered.html', {'rendered_html': rendered_html})