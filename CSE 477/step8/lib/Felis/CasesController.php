<?php
/**
 * Created by PhpStorm.
 * User: shash
 * Date: 3/28/2018
 * Time: 19:24
 */

namespace Felis;


class CasesController
{
    private $redirect;

    /**
     * @return string
     */
    public function getRedirect()
    {
        return $this->redirect;
    }	///< Page we will redirect the user to.



    /**
     * CasesController constructor.
     * @param Site $site The Site object
     * @param array $session $_SESSION
     * @param array $post $_POST
     */
    public function __construct(Site $site, $post) {
        $root = $site->getRoot();
        if(isset($post["add"])) {
            $this->redirect = "$root/newcase.php";
        }
        else {
            $this->redirect = "$root/cases.php";
        }



    }

}