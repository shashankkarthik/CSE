#ifndef RECEIPT_BAG
#define RECEIPT_BAG

#include<iostream>
using std::ostream;
#include<random>
using std::mt19937_64; using std::uniform_int_distribution;

// forward declaration
template<typename T>
class RBag;

/*
  Node struct has templated data_ field and an int receipt_ field
  The two-arg constructor fills in the data_ and receipt_ from its args
*/
template <typename T>
struct Node{
public:
  T data_;
  Node* next_;
  int receipt_;

  Node()						: data_(), next_(nullptr), receipt_(0) {};
  Node (T data, int receipt)	: data_(data), next_(nullptr), receipt_(receipt) {};
  
  friend ostream& operator<<(ostream& out, Node& n){
    // FILL THIS IN. Print the Node
    out << "{ data : " << n.data_ << ", receipt : " << n.receipt_ << ", next : " << n.next_ << "}" <<endl;
    return out;
  };
  friend class RBag<T>;
};


/*
  RBag class. Has only a head_ to the first Node. Empty list has head_ == nullptr
  Both the random engine and uniform distribution are provided. When a random
  number is required elsewhere in the RBag, call dist_(reng_)
*/

template<typename T>
class RBag{
private:
  Node<T>* head_;
  mt19937_64 reng_;
  uniform_int_distribution<int> dist_;


public:
  RBag()	: head_(nullptr) {};	

  // rule of three
  RBag(const RBag& b)
  {
	  auto other_node = b.head_;
	  head_ = nullptr;
	  while(other_node)
	  {
		  append(other_node -> data_);
		  other_node = other_node -> next_;
	  }  
  }
  
  RBag& operator=(RBag other)
  {
	  swap(*this, other);
	  return *this;
  }
  
  ~RBag()
  {
	  auto node = head_;
	  while (node)
	  {
		  auto temp = node -> next_;
		  delete node;
		  node = temp;
	  }
  }

  // returns nullptr if not found, else returns pointer to the Node
  // and places the found Node at the front of the RBag linked list
  Node<T>* find(long receipt);

  // Make a new Node using dat and generating a random number receipt
  // then append to the front of the RBag linked list
  long append_front(T dat);
  
  // Node already exists, append to the front of the RBag linked list
  long append_front(Node<T>* n);

  // if Node is not found, return false, else delete the found Node
  // and return true
  bool remove(long receipt);
  
  friend ostream& operator<<(ostream& out, RBag& b){
    // FILL THIS IN. Print the RBag contents
    auto temp = b.head_;
    while(temp != nullptr)
    { 
		out << "{ data_ : " << temp -> data_ << ", receipt_ : " << temp -> receipt_ << ", next_ : " << temp -> next_ << "}" << endl;
		temp = temp -> next_;
	}
    return out;
  };
};

template<typename T>
Node<T>* RBag<T>::find(long receipt)
{
	auto head_orig = head_; //Temp. Variable to retain original head_ value
	
	if (head_ != nullptr)
	{
		if (head_ -> receipt_ == receipt) //If head_ points to desired node
		{
			return head_;
		}
		
		else
		{
			auto current = head_ -> next_; //Points to current node ( In this case, the second node)
			auto previous = head_; //Points to previous node ( In this case, first node which head points to)
			
			while (current != nullptr) //While not at the end of the list.
			{
				if (current -> receipt_ == receipt)
				{
					head_ = previous -> next_; //Assigns the head to point to the desired node making it the starting node of the list.
					previous -> next_ = current -> next_; //The node preceding the desired node now points to the node succeeding the desired node.
					current -> next_ = head_orig; //Desired node(now first) points to the second node which used to be first
					return head_;				  //(the same node that the original head pointed to).
				}
				
				else
				{	
					//Increment current and previous by one node.
					current = current -> next_;
					previous = previous -> next_;
				}
			}
		}
	}
	
	return nullptr; //If head_ is nullptr i.e. no bag exists.
}

template<typename T>
long RBag<T>::append_front(T dat)
{
	long receipt = dist_(reng_);
	Node<T>* node_ptr = new Node<T>(dat,receipt);
	if (head_ != nullptr)
	{
		node_ptr-> next_ = head_;
		head_ = node_ptr;
	}
	else
	{
		head_ = node_ptr;
	}	
	return receipt;
}

template<typename T>
long RBag<T>::append_front(Node<T>* n)
{
	if (head_ != nullptr)
	{
		n -> next_ = head_;
		head_ = n;
	}
	else
	{
		head_= n;
	}
	
	return n -> receipt_;
}

template<typename T>
bool RBag<T>::remove(long receipt)
{
	auto remove_address = find(receipt);
	if( remove_address == nullptr) //If node address is nullptr i.e. if node does not exist.
	{
		return false;
	}
	else
	{
		head_ = remove_address -> next_; 
		delete remove_address;
		return true;
	}

}



#endif
