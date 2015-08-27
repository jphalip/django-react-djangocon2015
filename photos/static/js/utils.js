/**
 * Returns true if the photo with the given `photoId` is a favorite.
 */
export function isFavorite(favorites, photoId) {
  for (var favorite of favorites) {
    if (favorite.photo.id === photoId)
      return true;
  }
  return false;
}

/**
 * Return the favorite object corresponding to the given `photoId`
 */
export function getFavorite(favorites, photoId) {
  for (var favorite of favorites) {
    if (favorite.photo.id === photoId)
      return favorite;
  }
}
