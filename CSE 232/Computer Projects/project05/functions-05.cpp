	/*
Shashank Karthikeyan
Section 02
Project 05
*/

#include <iostream>
using std::cout; using std::endl; using std::string;
#include <vector>
using std::vector;
#include <fstream>
using std::ifstream;
#include <sstream>
using std::stringstream;
#include <random>
using std::mt19937_64; using std::uniform_int_distribution;



string filter_string (string s) 
	{
	string s_filtered;	
	for (unsigned int i = 0; i < s.length(); i++) 
	{
		if(isalpha(s[i]))	//Checks if charecter in string is alphabetic
		{
			s_filtered += tolower(s[i]); //Converts all alphabetic charecters to lowercase
		}
		
	}

	return s_filtered;
		
}


void read_key (ifstream &in_file, vector<long> &shift_key)
{
	string first_line;
	
	getline(in_file, first_line); //Gets the first line of the .txt and stores it in string first_line
	
	stringstream s;
	long val;
	
	s << first_line; //Stores the contents of string first_line in stringstream s
	while (s)
	{
		s >> val; 					//Val takes the value of each number in stringstream
		shift_key.push_back(val);	//Pushes val to the end of shift_key vector.
	}
	
	
	/*
	 Due to the nature of my loop the final value was beeing appended 
	 twice so I just removed it after.
	 */
	 
	shift_key.erase(shift_key.end()-1);	
}



string encode (string to_encode, vector<long>& shifts, 
			   mt19937_64 &reng, 
			   uniform_int_distribution<long>& dist)
	{
		
		stringstream encoded_final; 
		unsigned int x = 0; //shift key vector index
		for(unsigned int i =0; i < to_encode.length(); i++)
		{
			char letter = to_encode[i]; 
			int index = letter - 'a'; //gets index of current charecter
			long random_int = dist(reng);  //gets random int
			
			long encoded1 = (26 * random_int) + index;
			
			if(x >= shifts.size())		//Checks if shift index is greater than shift vector length
			{
				x = 0;					//If so, resets index to 0;
			}
			
			long encoded2 = encoded1 + shifts[x];
			
			encoded_final << encoded2 << " ";
			
			x++;				
			
			
		}
		return encoded_final.str();
	}

string decode(string to_decode, vector<long>& shifts)
{
	string decoded_final;
	unsigned int x = 0; //Shifts vector index
	long encoded_val;
	vector<long> encoded_vec; 
	
	stringstream encoded;
	encoded << to_decode;
	
	while (encoded) //makes vector containing encoded values;
	{
		encoded >> encoded_val;
		encoded_vec.push_back(encoded_val);
	}
	/*
	 Due to the nature of my loop the final value was beeing appended to the 
	 vector twice so I just removed it after.
	*/
	encoded_vec.erase(encoded_vec.end()-1);
	
	for (unsigned int i = 0; i < encoded_vec.size(); i++)
	{
		if(x >= shifts.size())
		{
			x = 0;
		}
		
		long decoded1 = encoded_vec[i] - shifts[x];
		
		long decoded_index = decoded1 % 26;
		
		char letter = decoded_index +'a';
		decoded_final += letter; 
		
		x++;	
	}
	return decoded_final;
	
	
}



