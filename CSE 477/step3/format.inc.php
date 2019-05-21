<?php
/**
 * Created by PhpStorm.
 * User: Shashank Karthikeyan
 * Date: 1/30/2018
 * Time: 1:30 AM
 */


/**
 * Create the HTML for the header block
 * @param $title The page title
 * @return string HTML for the header block
 */
function presentHeader($title) {
    $html = <<<HTML
<header>
<nav><p><a href="welcome.php">New Game</a>
<a href="game.php">Game</a>
<a href="instructions.php">Instructions</a></p></nav>
<h1>$title</h1>
</header>
HTML;
    return $html;
}
