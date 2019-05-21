/*! DO NOT EDIT step10 2018-04-17 */
function Buttons() {
    this.on = 1;
    var that = this;

    this.update(1);

    for(var b=1;  b<=3;  b++) {
        this.configButton(b);
    }
}

Buttons.prototype.configButton = function(b) {
    var c = (b == 3 ? 1 : b + 1);
    var that = this;

    $("#b" + b).click(function() {
        if(that.on == b) {
            that.update(c);
        }
    });
}

Buttons.prototype.update = function(a) {
    this.on = a;
    $("#b1").css("background-color", this.on == 1 ? "red" : "green");
    $("#b2").css("background-color", this.on == 2 ? "red" : "green");
    $("#b3").css("background-color", this.on == 3 ? "red" : "green");
    $("#b1").html(this.on == 1 ? "Press Me" : "&nbsp;");
    $("#b2").html(this.on == 2 ? "Press Me" : "&nbsp;");
    $("#b3").html(this.on == 3 ? "Press Me" : "&nbsp;");
}
function Simon(sel) {
    // Get a reference to the form object
    this.form = $(sel);
    var that = this;

    this.state = "initial";
    this.sequence = [];
    this.sequence.push(Math.floor(Math.random() * 4));
    this.current = 0;

    console.log('Simon started');

    this.configureButton(0, "red");
    this.configureButton(1, "green");
    this.configureButton(2, "blue");
    this.configureButton(3, "yellow");



    this.play();
}

Simon.prototype.configureButton = function(ndx, color) {
    var button = $(this.form.find("input").get(ndx));
    var that = this;
    console.log(button);

    button.click(function(event) {
        that.buttonPress(ndx, color);
    });

    button.mousedown(function(event) {
        button.css("background-color", color);
    });

    button.mouseup(function(event) {
        button.css("background-color", "lightgrey");
    });

    console.log("Set Button: " + ndx + " Color: " + color);
}

Simon.prototype.play = function() {
    this.state = "play";    // State is now playing
    this.current = 0;       // Starting with the first one
    this.playCurrent();
}

Simon.prototype.playCurrent = function() {
    var that = this;

    if(this.current < this.sequence.length) {
        // We have one to play
        var colors = ['red', 'green', 'blue', 'yellow'];
        document.getElementById(colors[this.sequence[this.current]]).play();

        //Get button and button color
        var button = $(this.form.find("input").get(this.sequence[this.current]));
        var color = colors[this.sequence[this.current]];

        //Light up button
        this.buttonOn(button,color);
        this.current++;

        window.setTimeout(function() {
            that.playCurrent();
        }, 1000);
    } else {
        this.current = 0;
        this.state = "enter";
    }
}

Simon.prototype.buttonOn = function (button,color) {
    var that = this;
    button.css("background-color", color);

    window.setTimeout(function() {
        $("input[type=button]").css("background-color" , "lightgrey");
    },1000);
}

Simon.prototype.buttonPress = function(ndx, color) {
    var that = this;
    console.log("Button press: " + ndx + " Color: " + color);

    if (ndx == this.sequence[this.current]) {
        //Button pressed correctly
        console.log("Correct Button!");

        //Play button Audio
        document.getElementById(color).currentTime = 0;
        document.getElementById(color).play();

        if (this.current == that.sequence.length-1) {
            //Sequence completed correctly
            console.log("Sequence completed correctly");
            this.current = 0;   //Reset current

            //Add new value to sequence
            this.sequence.push(Math.floor(Math.random() * 4));
            console.log("Generated New Value");

            window.setTimeout(function() {
                that.play();
                console.log("State: " + that.state);
            }, 1000);
        }
        else {
            //Sequence incomplete
            this.current += 1;  //Move to next button in sequence
            this.state = "enter";
            console.log("State: " + this.state);

        }
    }
    else {
        //Button pressed incorrectly
        console.log("Incorrect Button!");

        //Play buzzer
        document.getElementById("buzzer").play();
        this.state = "fail";
        console.log("State: " + this.state);

        //Generate new sequence
        this.sequence = [];
        this.sequence.push(Math.floor(Math.random() * 4));
        console.log("Generated New Sequence");


        window.setTimeout(function() {
            that.play();
            console.log("State: " + that.state);
        }, 1000);


    }
}