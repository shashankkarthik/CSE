function randomWord() {
    var words = ["moon","home","mega","blue","send","frog","book","hair","late",
        "club","bold","lion","sand","pong","army","baby","baby","bank","bird","bomb","book",
        "boss","bowl","cave","desk","drum","dung","ears","eyes","film","fire","foot","fork",
        "game","gate","girl","hose","junk","maze","meat","milk","mist","nail","navy","ring",
        "rock","roof","room","rope","salt","ship","shop","star","worm","zone","cloud",
        "water","chair","cords","final","uncle","tight","hydro","evily","gamer","juice",
        "table","media","world","magic","crust","toast","adult","album","apple",
        "bible","bible","brain","chair","chief","child","clock","clown","comet","cycle",
        "dress","drill","drink","earth","fruit","horse","knife","mouth","onion","pants",
        "plane","radar","rifle","robot","shoes","slave","snail","solid","spice","spoon",
        "sword","table","teeth","tiger","torch","train","water","woman","money","zebra",
        "pencil","school","hammer","window","banana","softly","bottle","tomato","prison",
        "loudly","guitar","soccer","racket","flying","smooth","purple","hunter","forest",
        "banana","bottle","bridge","button","carpet","carrot","chisel","church","church",
        "circle","circus","circus","coffee","eraser","family","finger","flower","fungus",
        "garden","gloves","grapes","guitar","hammer","insect","liquid","magnet","meteor",
        "needle","pebble","pepper","pillow","planet","pocket","potato","prison","record",
        "rocket","saddle","school","shower","sphere","spiral","square","toilet","tongue",
        "tunnel","vacuum","weapon","window","sausage","blubber","network","walking","musical",
        "penguin","teacher","website","awesome","attatch","zooming","falling","moniter",
        "captain","bonding","shaving","desktop","flipper","monster","comment","element",
        "airport","balloon","bathtub","compass","crystal","diamond","feather","freeway",
        "highway","kitchen","library","monster","perfume","printer","pyramid","rainbow",
        "stomach","torpedo","vampire","vulture"];

    return words[Math.floor(Math.random() * words.length)];
}

function isLetter(str) {
    return str.length === 1 && str.match(/[a-z]/i);
}

//Generates HTML for word blanks
function generateWordHTML(word){
    var html = "";
    for(var i=0;i<word.length;i++){
        html += "_ ";
    }
    html += "";

    return html;
}

//Generates Game HTML given target guess word
function generateHTML(word) {
    var html = "<img id='man' src='hangman/hm0.png' height='300' width='125'>"

    html += "<p id='guess'>"
    html += generateWordHTML(word);
    html += "</p>";

    html += "<form>"

    html += "<input type='hidden' id='word' value='" + word + "'>";
    html += "</p>" + "<label for='letter'>Letter:</label>"
        + "<input id='letter' type='text' name='letter'>";
    html += "<p><input id='guessButton' type='submit' value='Guess!'>"
        + "<input type='submit' id='newGameButton' value='New Game'></p>"
        + "<p id='message'>&nbsp;</p>"

    html +="</form>";
    return html;
}

function hangman() {
    var targetWord = randomWord(); //Target to guess
    console.log(targetWord);

    var totalGuesses = 0; //Nunmber of guesses the user has used up so far
    var maxGuesses = 6; //No more than 6 guesses
    var playArea = document.getElementById("play-area");

    playArea.innerHTML = generateHTML(targetWord);

    var image = "hangman/hm0.png";
    var man = document.getElementById("man");
    var guessButton = document.getElementById("guessButton");
    var newGameButton = document.getElementById("newGameButton");
    var message = document.getElementById("message");
    var word = document.getElementById("guess");

    newGameButton.onclick = function (event) {
        var oldWord = document.getElementById("word");
        event.preventDefault();
        totalGuesses = 0;
        targetWord = randomWord();
        console.log("new word: " , targetWord);
        word.innerHTML = generateWordHTML(targetWord);
        oldWord.value = targetWord;
    }

    guessButton.onclick = function (event) {
        event.preventDefault();
        var letter = document.getElementById("letter");

        // Only grab 1st character
        letter = letter.value.charAt(0);
        // Check that it's actually a letter
        if (!isLetter(letter)) {
            message.innerHTML = "You must enter a letter!";
            letter.value = "";
        }
        else {
            // Check if the letter is in the word
            if (targetWord.indexOf(letter) == -1) {
                console.log("you wrongly guessed: " , letter);
                totalGuesses += 1;
                if(totalGuesses >= maxGuesses){
                    message.innerHTML = "You guessed poorly!";
                    man.src = "hangman/hm6.png";
                    var str = "";
                    for(var i=0;i<targetWord.length;i++){
                        str += targetWord[i] + " ";
                    }
                    console.log("word expanded", str);
                    word.innerHTML = str;
                }
                else{
                    letter.value = "";
                    var imgSub = image.substr(0, 10);
                    man.src = imgSub + totalGuesses + image.substr(11, image.length);
                }
            }
            else {
                var partialWord = "";
                for (var i = 0; i < targetWord.length; i++) {
                    if (targetWord[i] == letter) {
                        partialWord += letter + " ";
                    }
                    else if(word.innerHTML.indexOf(targetWord[i]) != -1){
                        partialWord += targetWord[i] + " ";
                    }
                    else {
                        partialWord += "_ ";
                    }
                }
                console.log("you correctly guessed: ", letter);
                word.innerHTML = partialWord;
                partialWord = partialWord.replace(/ /g, "");
                if(partialWord == targetWord){
                    message.innerHTML = "You Win!"

                }
            }

        }
    }





}

