(function($) {
    function appendTimeStamp(filename) {
        return filename + '?' + Math.round(new Date().getTime() / 1000);
    }

    $.loadAjaxAssets = function(ajaxRequest) {
        // Retrieve a list of files from Ajax-Assets header
        if (ajaxRequest.getResponseHeader('Ajax-Assets')) {
            var ajaxAssets = ajaxRequest.getResponseHeader('Ajax-Assets').split('; ');

            $.each(ajaxAssets, function(key, value) {
                ajaxAssets[key] = appendTimeStamp(value); // Apply a timestamp to avoid caching
            });
        }

        // Retrieve a list of files from Ajax-Assets-Completed header
        if (ajaxRequest.getResponseHeader('Ajax-Assets-OnComplete')) {
            var ajaxAssetsCompleted = ajaxRequest.getResponseHeader('Ajax-Assets-OnComplete').split('; ');

            $.each(ajaxAssetsCompleted, function(key, value) {
                ajaxAssetsCompleted[key] = appendTimeStamp(value);
            });
        }

        // Load the resources with Modernizr
        Modernizr.load([{
            load: ajaxAssets,
            complete: function() {
                Modernizr.load([{load: ajaxAssetsCompleted}]);
            }
        }]);
    };
})(jQuery);
