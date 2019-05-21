#include<iostream>
using std::cout; using std::endl; 
#include<limits>
using std::numeric_limits;

/* wfp, 5/22/14
do floating point division while checking for 0 
*/
long my_func(double num, double divisor){
    double result;
    if (divisor != 0)
        result = num/divisor;
    else
        result = numeric_limits<double>::min();
    return result;
}

/* wfp, 5/22/14
divide 3.0 by smaller and smaller divisors while the
divisor is greater than 0
*/
int main (){
    double decrement = 0.4;
    double value = 3.0;
    double divisor = 2.0;
    double result;
    while (divisor >= 0){
        result = my_func(value, divisor);
        cout<<"Result of:"<<value<<" divided by:"<<divisor
                         <<" equals:"<<result<<endl;
        divisor -= decrement;
    }
}
            
