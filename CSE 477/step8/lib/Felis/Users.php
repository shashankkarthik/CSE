<?php
/**
 * Created by PhpStorm.
 * User: shash
 * Date: 3/20/2018
 * Time: 8:02
 */

namespace Felis;

/**
 * Manage users in our system.
 */
class Users extends Table
{
    /**
     * Constructor
     * @param $site The Site object
     */
    public function __construct(Site $site) {
        parent::__construct($site, "user");
    }

    /**
     * Test for a valid login.
     * @param $email User email
     * @param $password Password credential
     * @returns User object if successful, null otherwise.
     */
    public function login($email, $password) {
        $sql =<<<SQL
SELECT * from $this->tableName
where email=?
SQL;
        $pdo = $this->pdo();
        $statement = $pdo->prepare($sql);

        $statement->execute(array($email));
        if($statement->rowCount() === 0) {
            return null;
        }

        $row = $statement->fetch(\PDO::FETCH_ASSOC);
        // Get the encrypted password and salt from the record
        $hash = $row['password'];
        $salt = $row['salt'];

        // Ensure it is correct
        if($hash !== hash("sha256", $password . $salt)) {
            return null;
        }

        return new User($row);
    }

    /**
     * Get a user based on the id
     * @param $id ID of the user
     * @returns User object if successful, null otherwise.
     */
    public function get($id) {
        $sql =<<<SQL
SELECT * from $this->tableName
WHERE id=?
SQL;
        $pdo = $this->pdo();
        $statement = $pdo->prepare($sql);

        $statement->execute(array($id));
        if ($statement->rowCount() === 0) {
            return null;
        }

        return new User($statement->fetch(\PDO::FETCH_ASSOC));

    }

    /**
     * Modify a user record based on the contents of a User object
     * @param User $user User object for object with modified data
     * @return true if successful, false if failed or user does not exist
     */
    public function update(User $user) {
        $sql =<<<SQL
update $this->tableName
set email=?, name=?, phone=?, address=?, notes=?, role=?
where id=?
SQL;

        $pdo = $this->pdo();
        $statement = $pdo->prepare($sql);

        try {
            $ret = $statement->execute(array(
                $user->getEmail(), $user->getName(), $user->getPhone(),
                $user->getAddress(), $user->getNotes(), $user->getRole(),
                $user->getId()
            ));
        } catch(\PDOException $e) {
            return false;
        }
        if($ret === false || $statement->rowCount() == 0) {
            return false;
        }

        return true;
    }

    public function getClients() {
        $sql =<<<SQL
select id, name 
from $this->tableName
where role=?
SQL;
        $pdo = $this->pdo();
        $statement = $pdo->prepare($sql);

        $statement->execute(array(User::CLIENT));
        if ($statement->rowCount() === 0) {
            return null;
        }

        return $statement->fetchAll(\PDO::FETCH_ASSOC);
    }

    public function getAgents() {
        $sql =<<<SQL
select id, name
from $this->tableName
where role=? or role=?
SQL;
        $pdo = $this->pdo();
        $statement = $pdo->prepare($sql);

        $statement->execute(array(User::ADMIN, User::STAFF));
        if ($statement->rowCount() === 0) {
            return null;
        }

        return $statement->fetchAll(\PDO::FETCH_ASSOC);


    }



}