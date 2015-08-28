import _ from 'lodash'
import uuid from 'uuid';
import {getFavorite} from './utils'
import Reflux from 'reflux'
import Actions from './actions'
import request from 'axios';


const photoStore = Reflux.createStore({
  listenables: [Actions],

  getInitialState() {
    // We keep an internal data-structure for photos and favorites so we can do
    // optimistic updates.
    return {
      photos: this.photos || [],
      favorites: this.favorites || [],
      isHydrated: this.isHydrated || false,
      error: this.isHydrated || false
    }
  },

  /**
   * Send current state down to the UI.
   */
  propagateState() {
    this.trigger({
      photos: this.photos,
      favorites: this.favorites,
      isHydrated: this.isHydrated,
      error: this.error
    });
  },

  /**
   * Fetch current data from the server and rehydrate the store.
   */
  fetchData() {
    return new Promise((resolve, reject) => {
      request.all([
        request.get('/api/photos/?format=json'),
        request.get('/api/favorites/?format=json')
      ])
      .then(([photos, favorites]) => {
        this.hydrate(photos.data, favorites.data);
        resolve();
      })
      .catch(reject);
    });
  },

  /**
   * Hydrates internal state data-structure.
   */
  hydrate(photos, favorites) {
    this.photos = photos;
    this.favorites = favorites;
    this.isHydrated = true;
    this.propagateState();
  },


/**************************************************************
 *
 * ACTION HANDLERS
 *
 **************************************************************/

  /**
   * When the UI wants to favorite a photo.
   */
  onAddToFavorites(photo) {
    // Optimistically add the favorite to the local data-structure
    let favoriteId = uuid.v4();
    this.favorites.unshift({id: favoriteId, photo: photo});
    this.propagateState();

    // Post change to the server
    request.post('/api/favorites/', {
        id: favoriteId,
        photo_id: photo.id
    })
    .then((favorites) => {
        // Update store with server's authoritative data
        this.favorites = favorites;
        this.propagateState();
    })
    .catch(() => {
        // Roll back with fresh data from the server
        this.fetchData();
    })
  },

  /**
   * When the UI wants to un-favorite a photo.
   */
  onRemoveFromFavorites(favorite) {
    // Optimistically remove the favorite from the local data-structure
    _.remove(this.favorites, (item)=>{
      return item.photo.id === favorite.photo.id
    });
    this.propagateState();

    // Post change to the server
    request.delete('/api/favorites/' + favorite.id)
    .then((favorites) => {
        // Update store with server's authoritative data
        this.favorites = favorites.data;
        this.propagateState();
    })
    .catch(() => {
        // Roll back with fresh data from the server
        this.fetchData();
    });
  },

  /**
   * When the UI wants to toggle favorite/un-favorite a photo.
   */
  onToggleFavorite(photo) {
    let alreadyFavorite = getFavorite(this.favorites, photo.id);
    if (alreadyFavorite) {
      this.onRemoveFromFavorites(alreadyFavorite);
    }
    else {
      this.onAddToFavorites(photo);
    }
  }
});


export default photoStore;