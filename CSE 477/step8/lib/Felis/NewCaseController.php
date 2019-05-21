<?php
/**
 * Created by PhpStorm.
 * User: shash
 * Date: 3/28/2018
 * Time: 19:24
 */

namespace Felis;


class NewCaseController
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
    public function __construct(Site $site, $user, $post) {
        $root = $site->getRoot();
        if(!isset($post['ok'])) {
            $this->redirect = "$root/cases.php";
            return;
        }

        $cases = new Cases($site);
        $id = $cases->insert(strip_tags($post['client']),
            $user->getId(),
            strip_tags($post['number']));

        if($id === null) {
            $this->redirect = "$root/newcase.php?e";
        } else {
            $this->redirect = "$root/case.php?id=$id";
        }
    }



}