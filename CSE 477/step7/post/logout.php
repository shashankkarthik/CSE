<?php
/**
 * Created by PhpStorm.
 * User: shash
 * Date: 3/20/2018
 * Time: 9:05
 */


require '../lib/site.inc.php';



unset($_SESSION[Felis\User::SESSION_NAME]);
$root = $site->getRoot();
header("location: $root/");

