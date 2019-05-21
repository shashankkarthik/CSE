/*
David Flores flores45@whippet
2016-01-19
lab01.cpp

Your Comments
*/

#include <iostream>
using std::cout; using std::cin; using std::endl;

int main()
{
	long days;
	long secs;
	long start_dist = 19481000000;
	double end_dist;
	double speed = 17.027;
	
	cout << "Enter a number of days after 01/15/2015: ";
	cin >> days;
	secs = days * 24 * 3600;
	end_dist = start_dist + (speed * secs);
	
	double end_miles = end_dist * .621371;
	double end_AU = end_dist / 149597871;
	double radio_time = (((end_dist * 1000) / 299792458) / 3600) * 2;
	
	cout << "Voyager distance from Sun " << days << " after 01/16/2015 in kilometers is: " << end_dist << " km." << endl;
	cout << "Voyager distance from Sun " << days << " after 01/16/2015 in miles is: " << end_miles << " mi." << endl;
	cout << "Voyager distance from Sun " << days << " after 01/16/2015 in AUs is: " << end_AU << " AU." << endl;
	
	cout << "Radio trip time for radio communication to the Sun in hours is: " << radio_time << " hrs." << endl;
}

