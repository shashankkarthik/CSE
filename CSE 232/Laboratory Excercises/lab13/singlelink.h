#ifndef SINGLELINK_H
#define SINGLELINK_H

#include <iostream>
using std::ostream; using std::cout; using std::endl;
#include <stdexcept>
using std::out_of_range;

// --------------------------------------------------------
// Node class for singly linked lists
// --------------------------------------------------------
template <typename T>
struct Node 
{
	public:
	    Node *next_;
	    T data_;
	
	public:    
	    Node()    : next_(nullptr) {};
	    Node(T d) : next_(nullptr), data_(d) {};
};

// --------------------------------------------------------
// Singly linked list class
// --------------------------------------------------------
template <typename T>
class SingleLink
{
	private:
	    Node<T> *head_;
	    Node<T> *tail_;
	
	public:
	    SingleLink()          : head_(nullptr), tail_(nullptr) {};
	    SingleLink(Node<T> n) : head_(&n),      tail_(&n)      {};
	    
	public:
	    // needed for "rule of three"
	    // (1) copy constructor
	    SingleLink(const SingleLink &other)
		{
			auto node = other.head_;
			if (node)
			{
				head_ = new Node<T>(node.data_);
			}
			auto cur_node = node;
			node = node->next_;
			while (node)
			{
				cur_node->next_ = new Node<T>(node.data_);
				cur_node = node;
				node = node->next_;
			}
			tail_ = cur_node;
		}
	    // (2) copy asignment operator
	    // (3) destructor
	    // implement these after you complete the lab
	
	public:
	    // The append_back method has been provided for you (see below)
	    void append_back(T dat);
	    
	    /*
			Special conditions for del:
				head_ == nullptr (i.e. Nothing to delete.)
				head_ == tail_ (i.e. There's only one node.)
				head_->data_ == val (i.e. We're deleting the first node.)
		*/
	    bool del(T val);
	    Node<T>& operator[](size_t index);
	
	    friend ostream& operator<<(ostream& out, SingleLink& s)
	    {
			for (auto ptr = s.head_; ptr != nullptr; ptr = ptr->next_)
			{
				out << ptr->data_ << ", ";
			}
			return out;
		};
};

// append node n to the end of the list
// fast because of the tail_ pointer
template<typename T>
void SingleLink<T>::append_back(T dat)
{
    Node<T>* node = new Node<T>(dat);
    
    // Add the new node to the end
    if (tail_ != nullptr) {
        tail_->next_ = node;
        tail_ = node;
    }
    
    // The list is empty, so head and tail point to the new node
    else {
        head_ = node;
        tail_ = node;
    }
}

template<typename T>
bool SingleLink<T>::del(T val)
{
	if (head_ == nullptr) // If there's nothing to delete.
	{
		return false;
	}
	else
	{
		Node<T>* next = head_;
		if (next->data_ == val)
		{
			head_ = next->next_;
			delete next;
			return true;
		}
		while (next != nullptr)
		{
			if (next->next_ != nullptr && (next->next_)->data_ == val)
			{
				Node<T>* temp = next->next_;
				next->next_ = (next->next_)->next_;
				delete temp;
				return true;
			}
			next = next->next_;
		}
		return false;
	}
}

template <typename T>
Node<T>& SingleLink<T>::operator[](size_t index)
{
	Node<T>* node = head_;
	for (size_t i = 1; i < index; i++)
	{
		if (node->next_ == nullptr)
		{
			throw out_of_range("Index out of range. It's okay. This is hard stuff.");
		}
		node = node->next_;
	}
	return *node;
}

#endif
