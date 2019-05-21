<?php
require __DIR__ . "/../../vendor/autoload.php";
/** @file
 * Empty unit testing template
 * @cond
 * Unit tests for the class
 */

use Guessing\Guessing as Guessing;
use Guessing\GuessingView as View;

class GuessingViewTest extends \PHPUnit_Framework_TestCase
{
    const SEED = 1234;

    public function test_construct() {
        $guessing = new Guessing(self::SEED);
        $view = new View($guessing);

        $this->assertInstanceOf('Guessing\GuessingView',$view);
    }

    public function test_present() {
        $guessing = new Guessing(self::SEED);
        $view = new View($guessing);

        $html = $view->present();

        $this->assertContains('<form method="post" action="guessing-post.php">', $html);
        $this->assertContains('<h1>Guessing Game</h1>', $html);
        $this->assertContains('<p><input type="submit" name="clear" value="New Game"></p></form>', $html);

        $this->assertContains('Try to guess the number.', $html);

        $guessing->guess(-1);
        $html = $view->present();
        $invalidGuess = "Your guess of -1 is invalid!";
        $this->assertContains($invalidGuess, $html);

        $guessing->guess(22);
        $html = $view->present();
        $tooLowGuess = "After 1 guesses you are too low!";
        $this->assertContains($tooLowGuess, $html);

        $guessing->guess(24);
        $html = $view->present();
        $tooHighGuess = "After 2 guesses you are too high!";
        $this->assertContains($tooHighGuess, $html);

        $guessing->guess(23);
        $html = $view->present();
        $validGuess = "After 3 guesses you are correct!";
        $this->assertContains($validGuess, $html);


    }
}

/// @endcond
