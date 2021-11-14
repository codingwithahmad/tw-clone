const url_name = JSON.parse(document.getElementById('url').textContent);
const app_name = JSON.parse(document.getElementById('app').textContent);
const username = JSON.parse(document.getElementById('username').textContent);
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
const uid = JSON.parse(document.getElementById('user_id').textContent)
const url = $(".like-btn").attr('href')



$(".like-btn").click(function (e) {
    event.preventDefault();
    let id = $(this).attr("data-pk");
    let link =  '/rest-api/twits/' + id;
    check(link, id);
});

function check(link, id) {
        $.ajax({
            url: link,
            success: function(success) {
                if (success.is_liked) {
                    send_delete(success.like_pk.pk, link, id)
                } else {
                    send_post(id, url, url_name, app_name, link);
                }
            }
        })
}


function send_delete(like_id, link, id) {
        $.ajax({
            url: '/rest-api/likes/delete/' + like_id,
            type: 'DELETE',
            headers: {'X-CSRFToken': csrftoken },
            success: function(s) {
                get_removed_likes(link, id);
            },
            error: function(e) {
                console.log(e)
            }

        })
}



function send_post(id, url, url_name, app_name, link) {
        $.ajax({
            url: url,
            type: 'POST',
            headers: {'X-CSRFToken': csrftoken },
            data: { twits: id, users: uid , url_name: url_name, app_name: app_name, username: username},
            success: function(success) {
                get_likes(link, id)
            },
            error: function(error) {
                console.log(error)
            }
        });
}

function get_likes(link, id) {
        $.ajax({
                    url: link,
                    success: function(s) {
                        $(".like-btn").children('#icon-' + id).removeClass('far').addClass('fas')
                        $("#likes-count-" + id).html(s.like_count)
                        $("#retweet-count-" + id).html(s.retweet_count)
                    },
                    error: function(error) {
                        console.log('err')
                    }

                });
}

function get_removed_likes(link, id) {
        $.ajax({
                    url: link,
                    success: function(s) {
                        $(".like-btn").children('#icon-' + id).removeClass('fas').addClass('far')
                        $("#likes-count-" + id).html(s.like_count)
                        $("#retweet-count-" + id).html(s.retweet_count)
                    },
                    error: function(error) {
                        console.log('err')
                    }

                });
}