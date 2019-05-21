<?php
require 'format.inc.php';
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <link href="step2.css" type="text/css" rel="stylesheet" />
    <meta charset="UTF-8">
    <title>You Killed the Wumpus</title>
</head>
<body>
    <?php echo presentHeader("Stalking the Wumpus"); ?>
    <div class = "main">
        <figure>
            <img src="images/dead-wumpus.jpg" width="600" height="325" alt="Cave Cat">
        </figure>

        <div class="BottomText">
            <p>You killed the Wumpus</p>
            <p><a href="welcome.php">New Game</a> </p>
        </div>
    </div>

</body>
</html>
