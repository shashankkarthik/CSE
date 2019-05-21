#ifndef LINEARSEARCH_H_
#define LINEARSEARCH_H_

#include <vector>
using std::vector;

template <typename Comparable>
/**
 * @pre: array(vector) is non empty
 * @return bool
 * @post: the value returned true if found false otherwise
 */
//your code goes here!
bool linearSearch(vector<Comparable> &data, int valueToFind) 
{
	for(int i=0; i < data.size(); i++)
	{
		if (data[i] == valueToFind)
		{
			return true;
		}
	}
	return false;
}


#endif /* LINEARSEARCH_H_ */
