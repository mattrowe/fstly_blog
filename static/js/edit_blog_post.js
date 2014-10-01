$( document ).ready(function() {

    $('form#edit-blog-post').submit(function( event ) {
        event.preventDefault();

        $.ajax({
            beforeSend: function(xhr) {
                xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
            },
            type : $(this).attr('method'),
            data : $(this).serialize(),
            url: $(this).attr('action'),
            success : function(e){
                window.location.href = e.redirect_to;
            },
            error: function(e){
                console.log(e.responseJSON);
            }
        });

    });

    $('#edit-blog-post input:button').click(function(event){
        $.ajax({
            type : 'DELETE',
            beforeSend: function(xhr) {
                xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
            },
            success : function(e){
                window.location.href = e.redirect_to;
            },
            error: function(e){
                console.log(e.responseJSON);
            }
        });
    });
});


var getCookie = function(name) {
    var value = "; " + document.cookie;
    var parts = value.split("; " + name + "=");
    if (parts.length == 2) return parts.pop().split(";").shift();
}
