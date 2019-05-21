<?php
/**
 * Created by PhpStorm.
 * User: shash
 * Date: 3/20/2018
 * Time: 3:20
 */

namespace Felis;


class StaffView extends View
{
    /**
     * Constructor
     * Sets the page title and any other settings.
     */
    public function __construct() {
        $this->setTitle("Felis Staff");

        $this->addLink("post/logout.php", "Log out");
    }
}