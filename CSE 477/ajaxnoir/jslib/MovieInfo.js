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