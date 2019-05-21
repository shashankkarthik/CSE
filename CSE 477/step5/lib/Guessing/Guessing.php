<?php
/**
 * Created by PhpStorm.
 * User: shash
 * Date: 2/15/2018
 * Time: 7:13 PM
 */

namespace Guessing;


class Guessing
{
    const MIN = 1;
    const MAX = 100;
    const INVALID = "invalid";
    const TOOLOW = "tooLow";
    const TOOHIGH = "tooHigh";
    const CORRECT = "correct";

    public function __construct($seed = null) {
        if($seed === null) {
            $seed = time();
        }

        srand($seed);
        $this->number = rand(self::MIN, self::MAX);
    }

    public function getNumber() {
        return $this->number;
    }

    public function getNumGuesses() {
        return $this->numGuesses;
    }

    public function guess($guess) {
        $this->currentGuess = $guess;
        if ($this->check() != self::INVALID) {
            $this->numGuesses += 1;
        }
    }

    public function getGuess() {
        return $this->currentGuess;
    }

    public function check() {
       if (!isset($this->currentGuess)) {
            return;
        }
        elseif (!is_numeric($this->currentGuess)) {
           return self::INVALID;
        }
        elseif ($this->currentGuess > self::MAX || $this->currentGuess < self::MIN ) {
            return self::INVALID;
        }
        else {
           if ($this->currentGuess < $this->number) {
               return self::TOOLOW;
           }
           elseif ($this->currentGuess > $this->number) {
               return self::TOOHIGH;
           }
           return self::CORRECT;
        }
    }

    private $number;
    private $numGuesses = 0;
    private $currentGuess;
}