<?php
/**
 * Created by PhpStorm.
 * User: shash
 * Date: 2/7/2018
 * Time: 6:27 PM
 */

namespace Wumpus;

class WumpusView {

    /**
     * Constructor
     * @param Wumpus $wumpus The Wumpus object
     */
    public function __construct(Wumpus $wumpus) {
        $this->wumpus = $wumpus;
    }

    /** Generate the HTML for the number of arrows remaining */
    public function presentArrows() {
        $a = $this->wumpus->numArrows();
        return "<p>You have $a arrows remaining.</p>";
    }

    public function presentStatus() {
        $status = "";

        $roomNum = $this->wumpus->getCurrent()->GetNum();

        $status .= "<p>You are in room $roomNum.</p>";

        if ($this->wumpus->hearBirds()) {
            $status .= "<p>You hear birds!</p>";
        }

        if ($this->wumpus->feelDraft()) {
            $status .= "<p>You feel a draft!</p>";
        }

        if ($this->wumpus->smellWumpus()) {
            $status .= "<p>You smell a wumpus!</p>";
        }

        if ($this->wumpus->wasCarried()) {
            $newRoomNum = $this->wumpus->getCurrent()->GetNum();
            $status .= "<p>You were carried by the birds to room $newRoomNum!</p>";
        }

        return $status;

    }

    /** Present the links for a room
     * @param $ndx An index 0 to 2 for the three rooms */
    public function presentRoom($ndx) {
        $room = $this->wumpus->getCurrent()->getNeighbors()[$ndx];
        $roomnum = $room->getNum();
        $roomndx = $room->getNdx();
        $roomurl = "game-post.php?m=$roomndx";
        $shooturl = "game-post.php?s=$roomndx";

        $html = <<<HTML
<div class="room">
  <figure><img src="images/cave2.jpg" width="180" height="135" alt=""/></figure>
  <p><a href="$roomurl">$roomnum</a></p>
<p><a href="$shooturl">Shoot Arrow</a></p>
</div>
HTML;

        return $html;
    }


    private $wumpus;    // The Wumpus Object

}