/*
David Flores flores45@whippet
2016-02-02
lab03.cpp

Your Comments
*/

#include <iostream>
using std::cout; using std::endl; using std::cin;
#include <cmath>
using std::pow;

double fn(double x)
{
	double result = ((-6) * pow(x,2) + 5 * x + 3);
	
	return result;
}

double integral(double x)
{
	double result = ((-2) * pow(x,3) + (5.0/2) * pow(x,2) + 3 * x);
	
	return result;
}

double trapezoid(double a, double b, long n)
{
	double mult = ((b - a) / (2 * n));
	double width = ((b - a) / n);
	double sum = 0;
	
	for (double k = a; k < b; k += width)
	{
		sum += (fn(k + width) + fn(k));
	}
	
	double result = mult * sum;
	
	return result;
}

int main()
{
	double flt_tol;
	double n;
	double tru_int = integral(1) - integral(0);
	
	cout << "Enter a float tolerance: ";
	cin >> flt_tol;
	
	cout << "Enter an initial number of trapezoids: ";
	cin >> n;
	
	double trap_value = trapezoid(0,1,n);
	double diff = tru_int - trap_value;
	
	while (diff > flt_tol)
	{
		cout << "Result: " << trap_value << ", traps: " << n << ", diff: " << diff << endl;
		
		n *= 2;
		trap_value = trapezoid(0,1,n);
		diff = tru_int - trap_value;
	}
	
	cout << "Trap count: " << n << ", estimate value: " << trap_value << ", exact: "
		<< tru_int << ", tolerance: " << flt_tol << endl;
}

