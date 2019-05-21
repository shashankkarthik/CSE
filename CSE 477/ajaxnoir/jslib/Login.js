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