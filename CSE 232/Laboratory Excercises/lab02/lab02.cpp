/*
David Flores flores45@whippet
2016-01-26
lab02.cpp

Your Comments
*/

#include <iostream>
using std::cout; using std::cin; using std::endl;

int main()
{
	long input;
	
	cout << "Enter a number (Negative to quit): ";
	cin >> input;	
	
	while (input >= 0)
	{
		long add_p = 0, sum = 0;
		if (input >= 0 && input <= 9)
		{
			cout << "Single digit" << endl;
			cout << "Additive persistence is: " << add_p << ", root is: " << input << endl;
		}		
		else
		{
			cout << "Additive root" << endl;
			for (add_p = 1; input >= 10; add_p++)
			{
				sum = 0;
				long input_again = input;
				
				while (input_again > 0)
				{
					sum += input_again % 10;
					input_again /= 10;
				}				
				input = sum;				
				cout << "Sum: " << sum << " pass: " << add_p << endl;
			}			
			cout << "Additive persistence is: " << (add_p - 1) << ", root is: " << sum << endl;
		}		
		cout << "Enter a number (Negative to quit): ";
		cin >> input;
	}
	cout << "Bye-bye, bad guy." << endl;
}

