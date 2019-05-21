<?php
require 'format.inc.php';
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <link href="step2.css" type="text/css" rel="stylesheet" />
    <meta charset="UTF-8">
    <title>Stalking the Wumpus</title>
</head>

<body>
    <?php echo presentHeader("Stalking the Wumpus"); ?>
    <div class = "main">
        <figure>
            <img src="images/cave.jpg" width="600" height="325" alt="Cave">
        </figure>

        <?php
        echo '<p>' . date("g:ia l, F j, Y") . '</p>';
        ?>
        <p>You are in room</p>
        <p>&nbsp;</p>
        <p>You hear birds</p>
        <p>You feel draft</p>
        <p>You smell Wumpus</p>


        <div class="rooms">
            <div class="room">
                <figure>
                    <img src="images/cave2.jpg" width="180" height="135" alt="cave2">
                    <figcaption><a href="game.php">Room 3</a><br>
                            <a href="game.php">Shoot Arrow</a></figcaption>
                </figure>
            </div><div class="room">
                <figure>
                    <img src="images/cave2.jpg" width="180" height="135" alt="cave2">
                    <figcaption><a href="game.php">Room 13</a><br>
                            <a href="game.php">Shoot Arrow</a></figcaption>
                </figure>
            </div><div class="room">
                <figure>
                    <img src="images/cave2.jpg" width="180" height="135" alt="cave2">
                    <figcaption><a href="game.php">Room 7</a><br>
                        <a href="game.php">Shoot Arrow</a></figcaption>
                </figure>
            </div>
        </div>

        <div class="BottomText">
            <p>You have 3 arrows remaining.</p>
        </div>
    </div>

</body>
</html>

