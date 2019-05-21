<?php

namespace Felis;

/**
 * View class uses by index.html (home page)
 */
class HomeView  extends View {
    /**
     * Constructor
     * Sets the page title and any other settings.
     */
    public function __construct() {
        $this->setTitle("Felis Investigations");

        $this->addLink("login.php", "Log in");
    }


    public function addTestimonial($text, $name) {
        $this->testimonials[] = "<blockquote><p>$text</p><p><cite>$name</cite></p></blockquote>";
    }

    public function testimonials() {
        $html = "";
        if (count($this->testimonials ) == 0) {
            return $html;
        }
        $html .= "<section class=\"testimonials\">";
        $html .= "<h2>TESTIMONIALS</h2>";

        //Left Testimonials
        $html .= "<div class=\"left\">";
        for ($i = 0; $i < count($this->testimonials)/2; $i++) {
            $html .= $this->testimonials[$i];
        }
        $html .= "</div>";

        //Right Testimonials
        $html .= "<div class=\"right\">";
        for ($i = count($this->testimonials)/2; $i < count($this->testimonials); $i++) {
            $html .= $this->testimonials[$i];
        }
        $html .= "</div>";

        $html .= "</section>";

        return $html;
    }


    /**
     * Add content to the header
     * @return string Any additional comment to put in the header
     */
    protected function headerAdditional() {
        return <<<HTML
<p>Welcome to Felis Investigations!</p>
<p>Domestic, divorce, and carousing investigations conducted without publicity. People and cats shadowed
    and investigated by expert inspectors. Katnapped kittons located. Missing cats and witnesses located.
    Accidents, furniture damage, losses by theft, blackmail, and murder investigations.</p>
<p><a href="">Learn more</a></p>
HTML;
    }

    private $testimonials = Array();


}