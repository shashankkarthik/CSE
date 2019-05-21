/*! DO NOT EDIT ajaxnoir 2018-04-24 */
function Login(sel) {
    console.log("Login constructed");
    var form = $(sel);
    form.submit(function(event) {
        event.preventDefault();

        console.log("Submitted");

        $.ajax({
            url: "post/login.php",
            data: form.serialize(),
            method: "POST",
            success: function(data) {
                var json = parse_json(data);
                console.log(json);
                if(json.ok) {
                    // Login was successful
                    window.location.assign("./")
                } else {
                    // Login failed, a message is in json.message
                    $(sel + " .message").html("<p>" + json.message + "</p>");
                }
            },
            error: function(xhr, status, error) {
                console.log(error);
                // An error!
                $(sel + " .message").html("<p>Error: " + error + "</p>");
            }
        });
    });



}
function MovieInfo(sel, title, year) {
    console.log("MovieInfo: " + title + "/" + year);
    var that = this;
    $.ajax({
        url:"https://api.themoviedb.org/3/search/movie",
        data: {api_key: "a5ce7b8695030eee28fb599aba8b1eeb", query: title, year: year},
        method: "GET",
        dataType: "text",
        success: function(data) {
            var json = parse_json(data);
            if(json.total_results == 0) {
                $('.paper').html("<p>No information available</p>");
            }
            else {
                that.printResult(sel, json.results[0]);
            }
            console.log(json);
        },
        error: function(xhr, status, error) {
            console.log(error);
            $('.paper').html("<p>Unable to communicate<br>with themoviedb.org</p>");
        }

    });
}

MovieInfo.prototype.printResult = function(sel, movie) {
    var html = "<ul>";

    html += "<li id = 'info'><a href=\"\"><img src=\"images/info.png\"></a>";
    html += "<div>";
    html += "<p>Title: " + movie['title'] + "</p>";
    html += "<p>Release Date: " + movie['release_date'] + "</p>";
    html += "<p>Vote Average: " + movie['vote_average'] + "</p>";
    html += "<p>Vote Count: " + movie['vote_count'] + "</p>";
    html += "</div></li>"

    html+= "<li id = 'plot'><a href=\"\"><img src=\"images/plot.png\"></a>";
    html += "<div>";
    html += "<p>" + movie['overview'] + "</p>";
    html += "</div></li>";


    html += "<li id='poster'><a href='#'><img src='images/poster.png'></a>";
    html += "<div>";
    html += "<p class='poster'><img src='http://image.tmdb.org/t/p/w500/" + movie['poster_path'] +"'></p>";
    html += "</div></li>";

    html += "</ul>";



    

    $(sel).html(html);



};
function parse_json(json) {
    try {
        var data = $.parseJSON(json);
    } catch(err) {
        throw "JSON parse error: " + json;
    }

    return data;
}
function Stars(sel) {

    console.log("Stars constructor");

    var table = $(sel + " table");  // The table tag

    // Loop over the table rows
    var rows = table.find("tr");    // All of the table rows
    for(var r=1; r<rows.length; r++) {
        // Get a row
        var row = $(rows.get(r));

        // Determine the row ID
        var id = row.find('input[name="id"]').val();

        // Find and loop over the stars, installing a listener for each
        var stars = row.find("img");
        for(var s=0; s<stars.length; s++) {
            var star = $(stars.get(s));

            // We are at a star
            this.installListener(row, star, id, s+1);
        }
    }
}

Stars.prototype.installListener = function(row, star, id, rating) {
    var that = this;

    star.click(function() {

        console.log("Click on " + id + " rating: " + rating);
        $.ajax({
            url: "post/stars.php",
            data: {id: id, rating: rating},
            method: "POST",
            success: function(data) {
                var json = parse_json(data);
                if(json.ok) {
                    // Successfully updated
                    that.update(row, rating);
                    that.updateTable(json.table);
                    that.message("<p>Successfully updated</p>");
                    new Stars("form");


                } else {
                    // Update failed
                    that.message("<p>Update failed</p>");


                }
            },
            error: function(xhr, status, error) {
                // Error
                that.message("<p>Error: " + error + "</p>");
            }
        });

    });
}

Stars.prototype.update = function(row, rating) {
    // Loop over the stars, setting the correct image
    var stars = row.find("img");
    for(var s=0; s<stars.length; s++) {
        var star = $(stars.get(s));

        if(s < rating) {
            star.attr("src", "images/star-green.png")
        } else {
            star.attr("src", "images/star-gray.png");
        }

    }

    var num = row.find("span.num");
    num.text("" + rating + "/10");

}

Stars.prototype.message = function(message) {
    // do something...
    $('.message').html(message).show().delay(2000).fadeOut(1000);
}

Stars.prototype.updateTable = function(table) {
    $('table').html(table);

}