<?php
require 'lib/game.inc.php';

$controller = new Wumpus\WumpusController($wumpus, $_REQUEST);
if($controller->isReset()) {
    unset($_SESSION[WUMPUS_SESSION]);
}

header('Location: ' . $controller->getPage());