<?php
/**
 * Created by PhpStorm.
 * User: Shashank Karthikeyan
 * Date: 2/15/2018
 * Time: 7:57 PM
 */
require __DIR__ . "/../vendor/autoload.php";

// Start php session
session_start();

define("GUESSING_SESSION", 'guessing');

if(!isset($_SESSION[GUESSING_SESSION])) {
    $_SESSION[GUESSING_SESSION] = new Guessing\Guessing();
}

if(isset($_GET['seed'])) {
    $_SESSION[GUESSING_SESSION] = new Guessing\Guessing(strip_tags($_GET['seed']));
}
$guessing = $_SESSION[GUESSING_SESSION];