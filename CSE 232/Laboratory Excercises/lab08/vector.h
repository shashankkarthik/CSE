#ifndef VECTOR_H
#define VECTOR_H

#include<string>
using std::string;

struct MathVector{
  long x;
  long y;

  MathVector();
  MathVector(long, long);
  MathVector add (const MathVector&);
  MathVector mult(long);
  long mult(const MathVector&);
  double magnitude();
};

string vec_to_str(const MathVector&);


#endif
