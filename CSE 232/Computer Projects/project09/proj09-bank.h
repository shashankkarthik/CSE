#ifndef BANK_CLASS
#define BANK_CLASS

#include "proj09-bankaccount.h"

#include <string>
using std::string;
#include <map>
using std::map; using std::pair;
#include <random>
using std::default_random_engine;


class Bank{
private:
	string name_;
	long bank_id_;
	map<long, BankAccount> accounts_;
	default_random_engine rand_eng_;
public:
	Bank(string bank_name, long seed = 1234);
	long bank_id();
	string bank_name();
	long create_account(string account_name, string password, double funds);
	double balance(long account_id, string password);
	bool transfer(long from_id, string from_password, long to_id, string to_password, double amount);
	void print_account(long id, string password, ostream& out);

};


#endif
