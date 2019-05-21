<?php
/**
 * Created by PhpStorm.
 * User: shash
 * Date: 3/20/2018
 * Time: 10:07
 */

namespace Felis;


class LoginView extends View
{
    public function presentForm() {
        $html = <<<HTML
<form method="post" action="post/login.php">
	<fieldset>
		<legend>Login</legend>
		<p>
			<label for="email">Email</label><br>
			<input type="email" id="email" name="email" placeholder="Email">
		</p>
		<p>
			<label for="password">Password</label><br>
			<input type="password" id="password" name="password" placeholder="Password">
		</p>
		<p>
			<input type="submit" value="Log in"> <a href="">Lost Password</a>
		</p>
		<p><a href="./">Felis Agency Home</a></p>

	</fieldset>
</form>
HTML;
        return $html;
    }

    public function getError() {
        if (isset($_GET['e'])) {
            $html = <<<HTML
<p class="msg" align="center">Invalid login credentials</p>
HTML;
            return $html;
        }
    }
}