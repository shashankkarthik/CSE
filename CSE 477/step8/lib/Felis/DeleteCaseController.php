<?php
/**
 * Created by PhpStorm.
 * User: shash
 * Date: 3/29/2018
 * Time: 20:11
 */

namespace Felis;


class DeleteCaseController
{
    private $redirect;

    /**
     * @return string
     */
    public function getRedirect()
    {
        return $this->redirect;
    }

    /**
     * DeleteCaseController constructor.
     * @param Site $site The Site object
     * @param array $session $_SESSION
     * @param array $post $_POST
     */
    public function __construct(Site $site, $post) {

    }
}