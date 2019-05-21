<?php
require __DIR__ . "/../../vendor/autoload.php";

/** @file
 * Empty unit testing template
 * @cond 
 * Unit tests for the class
 */

use Felis\Site as Site;

class SiteTest extends \PHPUnit_Framework_TestCase
{
	public function testEmailGetterSetter() {
        $site = new Site();

        $testEmail = "testUser@testDomain.com";
        $site->setEmail($testEmail);

        $this->assertEquals($testEmail, $site->getEmail());
	}

	public function testRootGetterSetter() {
	    $site = new Site();

	    $testRoot = "testRoot";
	    $site->setRoot($testRoot);

	    $this->assertEquals($testRoot, $site->getRoot());
    }

    public function testTablePrefixGetter() {
        $site = new Site();

        $testPrefix = "testPrefix";
        $site->dbConfigure("host","user","password",$testPrefix);

        $this->assertEquals($testPrefix, $site->getTablePrefix());
    }

    public function test_localize() {
        $site = new Site();
        $localize = require 'localize.inc.php';
        if(is_callable($localize)) {
            $localize($site);
        }
        $this->assertEquals('test_', $site->getTablePrefix());
    }
}

/// @endcond
