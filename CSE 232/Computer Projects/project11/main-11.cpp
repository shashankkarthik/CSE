#include <iostream>
using std::cout;
using std::endl;

#include "class-11.h"


int main ()
{
    cout << "Create a bag of longs and add: 10, 20" << endl;
    RBag<long> b;
    b.append_front(10);
    b.append_front(20);
    cout << "current bag :\n" << b << endl;

    cout << "Prepend 30 and get a receipt : ";
    long rcpt = b.append_front(30);
    cout << rcpt << endl;
    cout << "current bag :\n" << b << endl;

    cout << "Create a new node and prepend" << endl;
    Node<long>* n = new Node<long>(40,100);
    b.append_front(n);
    cout << "current bag :\n" << b << endl;

    cout << "Search for the receipt : ";
    auto ptr = b.find(rcpt);
    if (ptr != nullptr) {
        cout << *ptr << "(Correct)" << endl;
    } else {
        cout << "item not found (incorrect)" << endl;
    }
    cout << "current bag :\n" << b << endl;

    cout << "Search for invalid receipt : ";
    ptr = b.find(1);
    if (ptr == nullptr) {
        cout << "item not found (correct)" << endl;
    } else {
        cout << "item found (incorrect) : " << *ptr << endl;
    }
    cout << "current bag :\n" << b << endl;

    cout << "Remove item from bag" << endl;
    b.remove(rcpt);
    cout << "current bag :\n" << b << endl;
}
