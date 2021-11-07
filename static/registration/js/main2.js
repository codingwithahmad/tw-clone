function get_likes(link, id) {
    $.ajax({
            url: link,
            success: function(s) {
                $("#likes-count-" + id).html(s.likes)
                $("#retweet-count-" + id).html(s.retweet)
            },
            error: function(error) {
                console.log('err')
            }

    })
}

$(".like-btn").click(function(e) {
    e.preventDefault()
    var id = $(this).attr("data-pk")
    var link = "/api/" + id
    var url = $(this).attr("href")
    $.ajax({
        url: url,
        success: function(success) {
            get_likes(link,id)
        },
        error: function(error) {
            console.log(error)
        }
    })
})






$(".retweet-btn").click(function(e) {
    e.preventDefault()
    var id = $(this).attr("data-pk")
    var link = "/api/" + id
    var url = $(this).attr("href")
    $.ajax({
        url: url,
        success: function(success) {
            get_likes(link,id)
        },
        error: function(error) {
            console.log(error)
        }
    })
})