from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import routers, serializers, viewsets


from photos.models import Photo, Favorite


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class FavoriteSerializer(serializers.ModelSerializer):
    photo = PhotoSerializer()

    class Meta:
        model = Favorite


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    def create(self, request, *args, **kwargs):
        """
        Customize `create` to return all favorite objects instead of just the
        newly created one.
        """
        # Create the new favorite object
        photo = get_object_or_404(Photo, id=request.data['photo_id'])
        Favorite.objects.create(id=request.data['id'], photo=photo)

        # Return all favorite objects
        serializer = self.get_serializer(Favorite.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        """
        Customize `destroy` to also return all favorite objects.
        """
        # Delete the favorite object
        super(FavoriteViewSet, self).destroy(request, *args, **kwargs)

        # Return all favorite objects
        serializer = self.get_serializer(Favorite.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


router = routers.DefaultRouter()
router.register(r'photos', PhotoViewSet)
router.register(r'favorites', FavoriteViewSet)