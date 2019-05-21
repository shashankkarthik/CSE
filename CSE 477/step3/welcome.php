<?php
require 'format.inc.php';
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <link href="step2.css" type="text/css" rel="stylesheet" />
    <meta charset="UTF-8">
    <title>Welcome to Stalking the Wumpus</title>
</head>
<body>
    <?php echo presentHeader("Stalking the Wumpus"); ?>
    <div class = "main">
        <figure>
            <img src="images/cave-evil-cat.png" width="600" height="325" alt="Cave Cat">
        </figure>

        <div class = "BottomText">
            <p>Welcome to <em>Stalking the Wumpus</em></p>
            <p><a href="instructions.php">Instructions</a></p>
            <p><a href="game.php">Start Game</a></p>
        </div>
    </div>


</body>
</html>