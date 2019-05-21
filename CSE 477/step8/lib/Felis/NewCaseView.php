<?php
/**
 * Created by PhpStorm.
 * User: shash
 * Date: 3/28/2018
 * Time: 19:34
 */

namespace Felis;


class NewCaseView extends View
{
    private $site;	///< The Site object

    /**
     * Constructor
     * Sets the page title and any other settings.
     */
    public function __construct(Site $site) {
        $this->site = $site;
        $this->setTitle("Felis New Case");

        $this->addLink("staff.php","Staff");
        $this->addLink("cases.php","Cases");
        $this->addLink("post/logout.php","Logout");
    }

    public function present() {
        $html = <<<HTML
<form action="post/newcase.php" method="post">
	<fieldset>
		<legend>New Case</legend>
		<p>Client:
			<select name="client">
HTML;
        $users = new Users($this->site);
        foreach($users->getClients() as $client) {
            $id = $client['id'];
            $name = $client['name'];
            $html .= '<option value="' . $id . '">' . $name . '</option>';
        }

        $html .= <<<HTML

			</select>
		</p>

		<p>
			<label for="number">Case Number: </label>
			<input type="text" id="number" name="number" placeholder="Case Number">
		</p>

		<p><input type="submit" value="OK" name ="ok"> <input type="submit" value="Cancel" name="cancel"></p>

	</fieldset>
</form>
HTML;

        return $html;
    }

}