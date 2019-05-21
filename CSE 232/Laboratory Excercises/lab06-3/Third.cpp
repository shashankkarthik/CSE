#include <iostream>  
using std::cout; using std::endl; using std::cin; 

void setlong(long* l_p, long l){
   *l_p = l; 
}


int main() { 
   long a; 
   setlong(&a, 10); 
   cout << a << endl; 
   
   long* b; 
   setlong(b, 10); 
   cout << *b << endl; 
} 

