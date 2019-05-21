/*
Shashank Karthikeyan karthik1@xserver
2016-04-11
proj09-bank.cpp

Your Comments
*/


#include "proj09-bank.h"

#include "proj09-bankaccount.h"

#include <iostream>
using std::cout; using std::endl;
#include <string>
using std::string;
#include <map>
using std::map; using std::pair;
#include <random>
using std::default_random_engine;
std::uniform_real_distribution<double> distribution(10000, 99000); //Sets range for defualt random engine
#include <limits>




Bank::Bank(string bank_name, long seed)
{	//Bank constructor
	
	name_ = bank_name;
	bank_id_ = distribution(rand_eng_);
	map<long, BankAccount> accounts_;
	default_random_engine rand_eng_;
}

long Bank::bank_id()
{
	return bank_id_;
}

string Bank::bank_name()
{
	return name_;
}

long Bank::create_account(string account_name, string password, double funds)
{
	long account_id = distribution(rand_eng_); //Creates random account ID
	if (accounts_.count(account_id) == 0) //Makes sure account ID does not already exist
	{
		accounts_[account_id] = BankAccount(account_name,password,funds);
	}
	return account_id;
	
}

double Bank::balance(long account_id, string password)
{
	if (accounts_.find(account_id) != accounts_.end()) //Checks to see if account exists
	{
		if (password == accounts_[account_id].password_) //Checks to see if passwords match
		{
			return accounts_[account_id].funds_;
		}
		
		else
		{
			return std::numeric_limits<double>::min();
		}
	}
	
	else
	{
		return std::numeric_limits<double>::min();
	}
}

bool Bank::transfer(long from_id, string from_password, long to_id, string to_password, double amount)
{
	
	if(accounts_.find(from_id) != accounts_.end() && accounts_.find(from_id) != accounts_.end()) //Checks if both accounts exist
	{
		if(accounts_[from_id].password_ == from_password && accounts_[to_id].password_ == to_password) //Checks if both passwords are correct
		{
			if (amount <= accounts_[from_id].funds_ && amount > 0) //Checks if funds are available in sender's account and it the ammount to be transfered is postive.
			{
				accounts_[to_id].funds_ += amount;
				accounts_[from_id].funds_ -= amount;
				return true;
			}
			
			else
			{
				return false;
			}
		}
		
		else
		{
			return false;
		}
	}
	
	else
	{
		return false;
	}
	
}

void Bank::print_account(long id, string password, ostream& out)
{
	if (accounts_.find(id) != accounts_.end())
	{
													
		if(accounts_[id].password_ == password)
		{
			out << "ID:" << id << ", "<<"Name:" << accounts_[id].name_ << ", "<<"funds:" << accounts_[id].funds_ << endl;
		}
		
		else
		{
			out << "Bad Password" << endl;
		}
	}
	else
	{
		out << "No such Account" << endl;
	}
	
}
