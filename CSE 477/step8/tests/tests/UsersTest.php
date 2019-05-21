<?php
require __DIR__ . "/../../vendor/autoload.php";

/** @file
 * Empty unit testing template/database version
 * @cond 
 * Unit tests for the class
 */

class UsersTest extends \PHPUnit_Extensions_Database_TestCase
{
    private static $site;

    public static function setUpBeforeClass() {
        self::$site = new Felis\Site();
        $localize  = require 'localize.inc.php';
        if(is_callable($localize)) {
            $localize(self::$site);
        }
    }

	/**
     * @return PHPUnit_Extensions_Database_DB_IDatabaseConnection
     */
    public function getConnection()
    {

        return $this->createDefaultDBConnection(self::$site->pdo(), 'karthik1');
    }

    /**
     * @return PHPUnit_Extensions_Database_DataSet_IDataSet
     */
    public function getDataSet()
    {
        return $this->createFlatXMLDataSet(dirname(__FILE__) . '/db/user.xml');

        //return $this->createFlatXMLDataSet(dirname(__FILE__) . 
		//	'/db/users.xml');
    }

    public function test_construct() {
        $users = new Felis\Users(self::$site);
        $this->assertInstanceOf('Felis\Users', $users);
    }

    public function test_login() {
        $users = new Felis\Users(self::$site);

        // Test a valid login based on email address
        $user = $users->login("dudess@dude.com", "87654321");
        $this->assertInstanceOf('Felis\User', $user);

        // Test a valid login based on email address
        $user = $users->login("cbowen@cse.msu.edu", "super477");
        $this->assertInstanceOf('Felis\User', $user);

        // Test a failed login
        $user = $users->login("dudess@dude.com", "wrongpw");
        $this->assertNull($user);

        // Test User Data
        $user = $users->login("cbowen@cse.msu.edu", "super477");

        $this->assertEquals(8,$user->getId());
        $this->assertEquals("cbowen@cse.msu.edu",$user->getEmail());
        $this->assertEquals("Owen, Charles", $user->getName());
        $this->assertEquals("999-999-9999",$user->getPhone());
        $this->assertEquals("Owen Address", $user->getAddress());
        $this->assertEquals("Owen Notes", $user->getNotes());
        $this->assertEquals(strtotime("2015-01-01 23:50:26"),$user->getJoined());
        $this->assertEquals("A",$user->getRole());


    }

    public function test_get_id() {
        $users = new Felis\Users(self::$site);

        //Test with valid ID
        $user = $users->get(8);
        $this->assertInstanceOf('Felis\User', $user);

        //Test with invalid ID
        $user = $users->get(9999);
        $this->assertNull($user);
    }

    public function test_update() {
        $users = new Felis\Users(self::$site);

        //Update valid user with valid data
        $user = $users->get(7);

        $user->setName("UpdatedName");
        $user->setEmail("UpdatedEmail");
        $user->setAddress("UpdatedAddress");
        $user->setNotes("UpdateNotes");
        $user->setPhone("UpdatedPhone");
        $user->setRole("C");

        $this->assertTrue($users->update($user));
        $updatedUser = $users->get(7); //Gets updates user for comparison

        $this->checkEquals($user,$updatedUser);


        //Update valid user with bad data (violating integrity constraint)
        $user = $users->get(7);
        $user->setEmail("cbowen@cse.msu.edu");

        $this->assertFalse($users->update($user));


        //Update invalid user (User ID DNE)
        $reflection = new ReflectionClass('\Felis\User');
        $reflectionProp = $reflection->getProperty('id');
        $reflectionProp->setAccessible(true);

        $user = $users->get(7);
        $reflectionProp->setValue($user,11); //Invalid User ID
        $this->assertFalse($users->update($user));
    }

    public function test_getClients() {
        $users = new Felis\Users(self::$site);

        $clients = $users->getClients();

        $this->assertEquals(2, count($clients));
        $c0 = $clients[0];
        $this->assertEquals(2, count($c0));
        $this->assertEquals(9, $c0['id']);
        $this->assertEquals("Simpson, Bart", $c0['name']);
        $c1 = $clients[1];
        $this->assertEquals(10, $c1['id']);
        $this->assertEquals("Simpson, Marge", $c1['name']);
    }


    /**
     * Asserts that two Felis/User objects have the same properties (does not check ID)
     * @param User $user1 first User object to compare
     * @param User $user2 second User object to compare
     */
    private function checkEquals($user1,$user2) {
        $this->assertEquals($user1->getName(),$user2->getName());
        $this->assertEquals($user1->getEmail(),$user2->getEmail());
        $this->assertEquals($user1->getAddress(),$user2->getAddress());
        $this->assertEquals($user1->getNotes(),$user2->getNotes());
        $this->assertEquals($user1->getPhone(),$user2->getPhone());
        $this->assertEquals($user1->getRole(),$user2->getRole());
    }




	
}

/// @endcond
