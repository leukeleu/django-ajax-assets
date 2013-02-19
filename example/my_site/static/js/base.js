$(function() {
    $('a.wizard').on('click', function(event) {
        event.preventDefault();
        $.ModalView.open('/wizard/', {
            afterLoad: function(response, status, xhr) {
                var self = this;

                $('#main-content').find('.wizard').on('click', function(event) {
                    event.preventDefault();
                    self.loadContent($(this).attr('href'));
                });
                // load additional form media
                $.loadAjaxAssets(xhr);
            }
        });
    });
});
