(function($) {

    var AjaxView = function() {
        this.defaults = {
            afterLoad: $.noop,         // Triggered after Ajax content is loaded
        };
        this.container = $('#wizard-container');
    };

    AjaxView.prototype = {

        loadContent: function(url) {
            var self = this;
            var contentLoaded = function(response, status, xhr) {
                if ($.isFunction(self.options.afterLoad)) {
                    self.options.afterLoad.apply(self, [response, status, xhr]);
                };
                return self.ajaxifyForms();
            };
            this.container.load(url, contentLoaded)
        },

        ajaxifyForms: function() {
            var self = this;
            this.container.find('form').ajaxForm({
                target: self.container,
                success: function(response, status, xhr) {
                    self.ajaxifyForms();
                    if ($.isFunction(self.options.afterLoad)) {
                        self.options.afterLoad.apply(self, [response, status, xhr]);
                    }
                }
            });
        },

        open: function(url, options) {
            this.options = $.extend({}, this.defaults, options); // Set options every time it's called
            this.loadContent(url);
        }
    };

    $.ModalView = new AjaxView();

})(jQuery);
