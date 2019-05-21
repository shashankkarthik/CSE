<?php
/**
 * Function to localize our site
 * @param $site The Site object
 */
return function(Felis\Site $site) {

    // Set the time zone
    date_default_timezone_set('America/Detroit');

    $site->setEmail('karthik1@cse.msu.edu');
    $site->setRoot('/~karthik1/step7');
    $site->dbConfigure('mysql:host=mysql-user.cse.msu.edu;dbname=karthik1',
        'karthik1',       // Database user
        'karthik1cse477mysql',     // Database password
        'test_');            // Table prefix

};