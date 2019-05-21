<?php
/**
 * Created by PhpStorm.
 * User: Shashank Karthikeyan
 * Date: 2/15/2018
 * Time: 7:10 PM
 */
require 'lib/guessing.inc.php';
$controller = new Guessing\GuessingController($guessing, $_POST);
if($controller->isReset()) {
    unset($_SESSION[GUESSING_SESSION]);
}
header("location: guessing.php");
exit;
