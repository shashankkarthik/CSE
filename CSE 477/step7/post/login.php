<?php
/**
 * Created by PhpStorm.
 * User: shash
 * Date: 3/20/2018
 * Time: 9:00
 */
$open = true;		// Can be accessed when not logged in
require '../lib/site.inc.php';

$controller = new Felis\LoginController($site, $_SESSION, $_POST);
header("location: " . $controller->getRedirect());