/*
Shashank Karthikeyan karthik1@xserver
2016-04-11
proj09-bankaccount.cpp

Your Comments
*/

#include <iostream>
using std::cout; using std::endl;

#include <string>
using std::string;

#include <locale>
using std::isalnum;

#include "proj09-bankaccount.h"


BankAccount::BankAccount()
{	
	//Chosen default values
	name_ = "";
	password_ = "";
	funds_ = 0;
}

BankAccount::BankAccount(string name, string password, double funds)
{
	if(funds < 0) //If funds is negative, sets it 0
	{
		funds = 0;
	}
	
	funds_ = funds;
	name_ = name;
	
	unsigned int count = 0u;
	for(unsigned int i = 0u; i < password.length(); i++) //Checks if password is alphanumeric
	{
		if (isalnum(password[i]))
		{
			count ++;
		}
	}
	
	if (count == password.length())
	{
		password_ = password;
	}
}

ostream& operator<<(ostream &out, const BankAccount&ba)
{
	out << "Name: " << ba.name_ << endl;
	out << "Funds: " << ba.funds_ << endl;
	return out;
}
