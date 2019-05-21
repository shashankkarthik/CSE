/*
Shashank Karthikeyan
Section 02
Project 06 - split.cpp
*/


#include <string>
using std::string;
#include <vector>
using std::vector;
#include <sstream>
using std::stringstream;

void split(string line, vector<string> &words, string good_chars)
{
	stringstream ss;
	ss << line;
	string word;
	
	while(ss)
	{
		ss >> word;
		string good_word; //new word containing only good chars from original word
		for(char&c:word)
		{	
			
			if(good_chars.find(c) != string::npos) //checks if char is in good_chars
			{	
				c = tolower(c);
				good_word += c;
			}
		}
		words.push_back(good_word); 
	}
	
	words.erase(words.end()-1);	//The last word was added twice so i just removed it.
	
	
	
}
