from django.test import TestCase
from react.render import render_component
from pyquery import PyQuery

from photos.api import FavoriteSerializer
from photos.models import Photo, Favorite


class ReactComponentsTests(TestCase):

    def setUp(self):
        # Create some photos
        photo1 = Photo.objects.create(url='photo1.jpg')
        photo2 = Photo.objects.create(url='photo2.jpg')
        photo3 = Photo.objects.create(url='photo3.jpg')

        # Favorite some photos
        Favorite.objects.create(photo=photo2)
        Favorite.objects.create(photo=photo3)

    def test_favorite_panel(self):
        favorites = FavoriteSerializer(Favorite.objects.all(), many=True)

        html = str(render_component(
            'js/components/favorite-panel.js',
             to_static_markup=True,  # Don't output the react-id attributes
             props = {
               'favorites': favorites.data,
             }
        ))

        # Check presence of certain strings
        self.assertFalse('photo1.jpg' in html)
        self.assertTrue('photo2.jpg' in html)
        self.assertTrue('photo3.jpg' in html)

        # Check a specific text value
        pq = PyQuery(html)
        self.assertEqual(pq('.badge').text(), '2')

        # Compare HTML blocks
        self.assertHTMLEqual(
            pq('h4').outerHtml(),
            '<h4>Favorites <span class="badge">2</span></h4>'
        )