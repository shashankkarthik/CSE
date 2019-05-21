<?php
/**
 * Created by PhpStorm.
 * User: shash
 * Date: 3/29/2018
 * Time: 17:55
 */

namespace Felis;


class CaseController
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
     * CaseController constructor.
     * @param Site $site The Site object
     * @param array $session $_SESSION
     * @param array $post $_POST
     */
    public function __construct(Site $site, $post) {
        $cases = new Cases($site);
        $users = new Users($site);

        $root = $site->getRoot();
        if (!isset($post['update'])) {
            $this->redirect = "$root/case.php";
            return;
        }

        $updatedRow = Array();
        $updatedRow['number'] = strip_tags($post['number']);

        $number = strip_tags($post['summary']);
        $allCases = $cases->getCases();


        $updatedRow['summary'] = strip_tags($post['summary']);
        $updatedRow['id'] = strip_tags($post['id']);

        foreach($allCases as $case) {
            if ($case->getNumber() == $number) {
                $this->redirect = "$root/case.php?id=" . $updatedRow['id'];
                return;
            }
        }

        $updatedRow['agentName'] = strip_tags($post['agent']);

        $allAgents = $users->getAgents();
        foreach($allAgents as $agent) {
            if ($agent['name'] == strip_tags($post['agent'])) {
                $updatedRow['agent'] = strip_tags($agent['id']);
            }
        }

        $client= $users->get(strip_tags($post['clientId']));
        $updateRow['client'] = strip_tags($post['clientId']);
        $updatedRow['clientName'] = strip_tags($client->getName());

        $updatedCase = new ClientCase($updatedRow);

        if (!$cases->update($updatedCase)) {
            $this->redirect = "$root/case.php?id=" . $updatedRow['id'];
            return;
        }
        else {
            $this->redirect = "$root/cases.php";
            return;
        }





    }
}