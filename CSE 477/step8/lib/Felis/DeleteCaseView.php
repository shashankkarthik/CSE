<?php
/**
 * Created by PhpStorm.
 * User: shash
 * Date: 3/29/2018
 * Time: 20:03
 */

namespace Felis;


class DeleteCaseView extends View
{
    private $site;	///< The Site object
    private $caseId; ///< Case ID

    /**
     * Constructor
     * Sets the page title and any other settings.
     */
    public function __construct(Site $site, $get)
    {
        $this->site = $site;
        $this->caseID = $get['id'];
        $this->setTitle("Felis Delete?");
        $this->addLink("staff.php", "Staff");
        $this->addLink("cases.php","Cases");
    }

    public function present() {
        $cases = new Cases($this->site);
        $case = $cases->get($this->caseId);
        $number = $case->getNumber();
        $html = <<<HTML
<form>
	<fieldset>
		<legend>Delete?</legend>
		<p>Are you sure absolutely certain beyond a shadow of
			a doubt that you want to delete case $number</p>

		<p>Speak now or forever hold your peace.</p>

		<p><input type="submit" value="Yes"> <input type="submit" value="No"></p>

	</fieldset>
</form>
HTML;
        return $html;

    }

}