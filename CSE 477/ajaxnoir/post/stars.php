<?php
/**
 * Created by PhpStorm.
 * User: shash
 * Date: 4/24/2018
 * Time: 19:44
 */
require '../lib/site.inc.php';

$controller = new Noir\StarController($site, $user, $_POST);
echo $controller->getResult();