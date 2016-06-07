define([
  'underscore',
  'backbone',
  'models/artist'
], function(_, Backbone, ArtistModel){
  var ArtistsCollection = Backbone.Collection.extend({
    model: ArtistModel,
    url: '/api/v1/pages/?type=artists.ArtistProfilePage&fields=title,first_name,last_name',
    urlRoot: '/api/v1/pages/',

    parse: function(response) {
        return response.pages;
    },

    maybeFetch: function(options){
        // Helper function to fetch only if this collection has not been fetched before.
        if(this._fetched){
            // If this has already been fetched, call the success, if it exists
            options.success && options.success();
            return;
        }

        // when the original success function completes mark this collection as fetched
        var self = this,
            successWrapper = function(success){
                return function(){
                    self._fetched = true;
                    success && success.apply(this, arguments);
                };
            };
        options.success = successWrapper(options.success);
        this.fetch(options);
    },

    getOrFetch: function(id, options){
        // Helper function to use this collection as a cache for models on the server
        var model = this.get(id);


        if(model){
            options.success && options.success(model);
            return;
        }

        model = new ArtistModel({
            artist_id: id
        });

        model.fetch(options);
    }
  });
  // You don't usually return a collection instantiated
  return ArtistsCollection;
});