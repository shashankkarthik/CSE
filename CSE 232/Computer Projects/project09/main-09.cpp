
#include <iostream>
using std::cout;
using std::endl;
using std::boolalpha;

#include <vector>
using std::vector;

#include <string>
using std::string;

#include <iomanip>
using std::setprecision;
using std::fixed;

#include <limits>
using std::numeric_limits;


#include "proj09-bank.h"



int main ()
{
  // Set output formatting flags for standard-out
  cout << boolalpha << setprecision(2) << fixed;

  //
  // Create a new bank object
  //
  const string bank_name = "Bank of Evil";
  Bank evil_bank(bank_name);

  cout << "Bank Name : " << evil_bank.bank_name() << endl;
  cout << "Bank ID   : " << evil_bank.bank_id() << endl << endl;


  //
  // Create two accounts and print them
  //
  const string bill_name = "bill punch";
  const string bill_pword = "abc123";
  const auto bill_amount = 1000;
  long bill_id = evil_bank.create_account(bill_name, bill_pword, bill_amount);

  const string homer_name = "homer simpson";
  const string homer_pwrod = "password";
  const auto homer_amount = -10;
  long homer_id = evil_bank.create_account(homer_name, homer_pwrod, homer_amount);

  evil_bank.print_account(bill_id, "abc12", cout);      // bad password
  evil_bank.print_account(bill_id+1, bill_pword, cout); // wrong account
  evil_bank.print_account(bill_id, bill_pword, cout);   // success!
  evil_bank.print_account(homer_id, homer_pwrod, cout); // funds at 0 not -10
  cout << endl;

  //
  // Perform a transfer
  //
  bool result = evil_bank.transfer(bill_id, bill_pword, homer_id, homer_pwrod, 100);
  cout << "Was it successful : " << result << endl;
  cout << "Bill new amount   : " << evil_bank.balance(bill_id, bill_pword) << endl;
  cout << "Homer new amount  : " << evil_bank.balance(homer_id, homer_pwrod) << endl;
  cout << endl;

  //
  // Try some invalid operations
  //
  double query = evil_bank.balance(123, "abc");  // bad id/password
  if (query == numeric_limits<double>::min()) {
    cout << "Bad Balance Inqury" << endl;
  }

  result = evil_bank.transfer(bill_id, bill_pword, homer_id, homer_pwrod, 1000);
  cout << "Not successful, insufficient funds, result was : " << result << endl;

  result = evil_bank.transfer(bill_id, bill_pword, homer_id, homer_pwrod, -1000);
  cout << "Not successful, negative funds, result was     : " << result << endl;
}
