#ifndef BANKACCOUNT_CLASS
#define BANKACCOUNT_CLASS

#include <string>
using std::string;
#include <iostream>
using std::ostream;



class BankAccount{
private:
	string name_;
	string password_;
	double funds_;

public:
	BankAccount();
	
	BankAccount(string name,string password, double funds = 0);
	
	friend ostream& operator<<(ostream &out, const BankAccount&ba);
	
	friend class Bank;
};

#endif
