define('templates/helpers/video', ['handlebars'], 
        function ( Handlebars ) {
    function video ( context, options ) {
        // Simple function for example
        return Math.round( context );
    }
    Handlebars.registerHelper( 'roundNumber', roundNumber );
    return video;
});