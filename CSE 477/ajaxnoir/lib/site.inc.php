<?php
/**
 * @file
 * A file loaded for all pages on the site.
 */
require __DIR__ . "/../vendor/autoload.php";

define("LOGIN_SESSION", "ajaxnoir_login");

// Start the session system
session_start();

// Create and localize the Site object
$site = new Noir\Site();
$localize = require 'localize.inc.php';
if(is_callable($localize)) {
	$localize($site);
}

/*
 * Login functionality
 */
if(!isset($open)) {
	// This is a page other than the login pages
	if (!isset($_SESSION[LOGIN_SESSION])) {
		// If not logged in, force to the login page
		$root = $site->getRoot();
		header("location: $root/login.php");
		exit;
	} else {
		// We are logged in.
		$user = $_SESSION[LOGIN_SESSION]['user'];
	}
}

