<?php
/**
 * Created by PhpStorm.
 * User: shash
 * Date: 4/24/2018
 * Time: 19:20
 */

namespace Noir;


class StarController extends Controller
{
    /**
     * StarController constructor.
     * @param Site $site Site object
     * @param $user User object
     * @param array $post $_POST
     */
    public function __construct(Site $site, $user, $post) {
        parent::__construct($site);

        $id = $post['id'];
        $rating = $post['rating'];

        $movieCollection = new Movies($this->site);
        $movie = $movieCollection->get($user,$id);

        if ($movie == null) {
            $this->result = json_encode(array('ok' => false, 'message' => 'Failed to update database!'));
        }
        else{
            $movieCollection->updateRating($user, $id, $rating);
            $view = new HomeView($site, $user);
            $table = $view->presentTable();
            $this->result = json_encode(array('ok' => true, 'table' => $table));
        }

    }

}