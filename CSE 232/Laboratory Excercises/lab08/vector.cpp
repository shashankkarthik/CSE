/*
David Flores
2016-03-15
vector.cpp
*/

#include <cmath>
using std::sqrt;
#include <sstream>
using std::ostringstream;

#include "vector.h"

MathVector::MathVector() : x(0), y(0) {};

MathVector::MathVector(long a, long b) : x(a), y(b) {};

MathVector MathVector::add(const MathVector& mv)
{
	MathVector new_mv((x + mv.x), (y + mv.y));
	
	return new_mv;
}

MathVector MathVector::mult(long num)
{
	MathVector new_mv((x * num), (y * num));
	
	return new_mv;
}

long MathVector::mult(const MathVector& mv)
{
	long product = (x * mv.x) + (y * mv.y);
	
	return product;
}

double MathVector::magnitude()
{
	double mag = sqrt(x * x + y * y);
	
	return mag;
}

string vec_to_str(const MathVector &v)
{
	ostringstream oss;
	oss << v.x << ":" << v.y;
	
	return oss.str();
}
