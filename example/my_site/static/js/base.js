$(function() {

    $('a.wizard').on('click', function(event) {
        event.preventDefault();
        $.AjaxView.open('/wizard/');
    });

});
