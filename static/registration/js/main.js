var url_name = '{{ request.resolver_match.url_name }}';
var app_name = '{{ request.resolver_match.app_names.0 }}';
var csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;




function get_likes(link, id) {
        $.ajax({
                    url: link,
                    success: function(s) {
                        $("#likes-count-" + id).html(s.like_count)
                        $("#retweet-count-" + id).html(s.retweet_count)
                    },
                    error: function(error) {
                        console.log('err')
                    }

                });
}


$("#like-button").click(function (e) {
    event.preventDefault();
    var id = $(this).attr("data-pk");
    var link =  '/rest-api/twits/' + id;
    var url = $(this).attr('href')
    $.ajax({
        url: url,
        type: 'POST',
        headers: { 'X-CSRFToken': csrftoken }
        data: {
            twits: id,
            users: '{{ request.user.pk }}',
            url_name: url_name,
            app_name: app_name
        },
        success: function(success) {
            get_likes(link, id)
            console.log('from success')
        },
        error: function(error) {
            console.log(error)
        }

    })
});