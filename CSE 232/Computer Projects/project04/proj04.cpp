#include<iostream>
using std::cout; using std::endl; using std::cin;
#include<string>
using std::string;


string fibo_string(string f0, string f1,int length)
{
	string fib_string = "";
	//Adds the first 2 fib strings to the sequence
	fib_string += f0;
	fib_string += f1;
	
	string f_last = f1;
	string f_2nd_last = f0;
	
	while(fib_string.length() < length)
	{
		string fib_new = f_last + f_2nd_last; //sums the last and 2nd last terms
		fib_string = fib_new;
		
		//Gets new last and 2nd last terms.
		f_2nd_last = f_last;
		f_last = fib_new; 
		
	}
	
	if((fib_string.length() == length))
	{
		return fib_string;
	}
	else
	{
		return fib_string.substr(0,length);
	}
	
}


long find_substring(string fibo, string target)
{
	long count = 0;
	int index_found = fibo.find(target,0); //Finds the first instance
	while(index_found != -1)
	{
		count += 1;
		index_found = fibo.find(target,index_found+1); //starts looking after the last instance
	}
	return count;
}

string lcs(string a_str, string b_str)
{	
	string lcs;
	if(a_str.length() < b_str.length() or a_str.length() == b_str.length()) // If a_str <= b
	{
		int count = 1;
		while(count <= a_str.length())
		{
			string target = a_str.substr(0,count);
			long check_sub = find_substring(b_str,target);
			if(check_sub != 0 and target.length() > lcs.length())
			{
				lcs = target;
			}
			count += 1;
	    }
		
	}
	
	
	else //If b_str < a_str
	{
		int count = 1;
		while(count <= b_str.length())
		{
			string target = b_str.substr(0,count);
			long check_sub = find_substring(a_str, target);
			if(check_sub != 0 and target.length() > lcs.length())
			{
				lcs = target;
			}
			count += 1;
		}	
	}
	
	return lcs;
}


int main () {
  long cases, start, finish, length;
  string f0, f1, target, f0f1_str;
  cin >> cases;
  for (int i=0; i < cases; i++){
    cin >> f0 >> f1 >> length >> start >> finish >> target;
    f0f1_str = fibo_string(f0,f1,length);

    // print the substring requested
    cout <<"Substring from "<< start<< " to " << finish << " is:"
	 << f0f1_str.substr(stasrt,finish-start+1)<<endl;

    // print the cnt of the target in the fibo_string
    cout <<  "Found target "<< target << " " << find_substring(f0f1_str, target)
	 << " times" <<endl;

    // print the longest common substring of the fibo and reversed fibo string
    string f1f0_str = fibo_string(f1,f0,length);
    cout << "LCS of " << f0 << "," << f1
	 <<" fibo and " << f1 << ","<< f0
	 <<" fibo is:" << lcs(f0f1_str, f1f0_str) << endl;

  }
}
