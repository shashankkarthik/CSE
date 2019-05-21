#ifndef ktSMALLEST_H_
#define ktSMALLEST_H_

#include <iostream>
using std::cout; using std::endl;
#include <ctime>
#include <cmath>
#include <vector>
using std::vector;
#include <algorithm>
#include <chrono>

/** Ignore forward declarations. */
enum Prefix {First, Second, Third, Other};
const char* PrefixStrings[] = {"st", "nd", "rd", "th"};
template <typename Comparable>
void PrintKth(const vector<Comparable> &nums, int k);
template <typename Comparable>
void Print(const vector<Comparable> &nums);
Prefix DeterminePrefix(const int value);
/*********************************/

template <typename Comparable>
void InsertionSort(vector<Comparable> &nums) 
{
    /**
     *      You code goes here.
     */
	int j;
	int temp;

	for (unsigned int i = 1; i < nums.size(); i++)
	{
		temp = nums[i];
		j = i-1;
		while (j >= 0 && nums[j] > temp)
		{
			nums[j+1] = nums[j];
			j--;
		}
		nums[j+1] = temp; 
	}
}

template <typename Comparable>
int getmax(vector<Comparable> a)
{
	int max;
	int max_index;
	for (unsigned int i = 0; i < a.size(); i++)
	{
		if (a[i] > max)
		{
			max = a[i];
			max_index = i;
		}
	}

	return max_index;
}



template <typename Comparable>
void KthSmallestUsingExtractMin(const vector<Comparable> &a, int k)
{
    /**
     *      You code goes here.
     */

   //your code goes here  
   //you can add helper methods can be called from this method..
	vector<Comparable> tempvec;
    for (int i = 0; i < k; i++)
    {
    	tempvec.push_back(a[i]);
    }


   	int max_index = getmax(tempvec);
   	int max = tempvec[max_index];

   	for (unsigned int i = k; i < a.size(); i++)
   	{
   		if (a[i] < max)
   		{	


   			tempvec[max_index] = a[i];
   			max_index = getmax(tempvec);
   			max = tempvec[max_index];;
   		}
   	}

   	InsertionSort(tempvec);
	PrintKth(tempvec, k);
}

// nums not const because it will be sorted, unless copied before
template <typename Comparable>
void  KthSmallestUsingSorting(vector<Comparable> &nums, int k)
{
    /**
     *      You code goes here.
     */

    // This method involves sorting. Make sure
    // InsertionSort is finished.
    InsertionSort(nums);

    //your code goes here
    PrintKth(nums, k);
}

/******************************************
 *		Do not modify code below this line.
 *****************************************/

template <typename Comparable>
void Print(const vector<Comparable> &nums)
{
	cout<< "Vector Contents " << endl<<endl;
	int temp2=0;
	for (int i=0; i< nums.size(); i++)
	{
		temp2=nums[i];
		cout<< "["<<i<<"]"<<" --> " << temp2<< endl;
	}

}

template <typename Comparable>
void PrintKth(const vector<Comparable> &nums, int k)
{
	int temp2=0;
	temp2 = nums[k-1];

    Prefix pre = DeterminePrefix(k);
    cout << k << PrefixStrings[pre] << " smallest elements is: "
        << temp2 << endl;
}


// Determine what to prefix the number being printed with
Prefix DeterminePrefix(const int value)
{
    // everything between 10 and 20 ends with th
    if (value >= 10 && value <= 20)
        return Other;
    // The remainder will indicate the last digit
    switch(value % 10)
    {
        case 1:
            return First;
        case 2:
            return Second;
        case 3:
            return Third;
        default:
            return Other;
    }
}

#endif /* ktSMALLEST_H_ */

