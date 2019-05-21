<?php
require 'format.inc.php';
require 'lib/game.inc.php';
$view = new Wumpus\WumpusView($wumpus);
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
        <?php
        echo $view->presentStatus();
        ?>


        <div class="rooms">
            <?php
            echo $view->presentRoom(0);
            echo $view->presentRoom(1);
            echo $view->presentRoom(2);
            ?>
        </div>

        <div class="BottomText">
            <?php
            echo $view->presentArrows();
            ?>
        </div>
    </div>

</body>
</html>

