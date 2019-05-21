/*
Shashank Karthikeyan
Section 02
Project 06 - functions-06.cpp
*/
#include <iostream>
using std::cout; using std::endl;
#include <string>
using std::string;
#include <vector>
using std::vector;
#include <map>
using std::map; using std::pair;
#include <fstream>
using std::ifstream;
#include <sstream>
using std::stringstream;
#include "split.h"


void process_file(string filename, map<string, vector<pair<long,long>>>& encode_map, map<pair<long,long>, string>& decode_map)
{	
	string good_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'";
	
	ifstream file(filename); //Gets file
	int line_count = 0;
	string line;
	
	while(getline(file, line))
	{
		vector<string> words; //Vector stores good words for each line
		split(line, words, good_chars); //Gets good words ands stores them in words
		
		for(unsigned int i = 0u; i < words.size(); i++)
		{
			pair<long,long>location; //Stores line # and word # for each word
			
			location.first = line_count;
			location.second = i;
			
			encode_map[words[i]].push_back(location); //Adds location pair to encode map with word as key
			
			decode_map[location] = words[i]; //Adds word to decode map with location pair as key
			
		}		
		
		line_count ++;
	}

}


string encode(string to_encode, map<string, vector<pair<long,long>>>& encode_map)
{
	if(encode_map.count(to_encode) != 0) //Checks if word is in encode_map
	{	
		pair<long,long> location = encode_map[to_encode][0]; //Gets location pair of first instance of word
		
		stringstream ss;
		ss << location.first << ":" << location.second; 
		
		string encoded;
		ss >> encoded;
		
		return encoded;
	}
	return"";
}

string decode(string to_decode, map<pair<long,long>, string>& decode_map)
{
	stringstream decode;
	decode << to_decode; 
	
	stringstream line;
	stringstream word;
	
	long line_numb;
	long word_numb;
	string token;
	
	getline(decode, token, ':');
	line << token;
	line >> line_numb; //Gets line number
	
	getline(decode, token, ':');
	word << token;
	word >> word_numb; //Gets word number
	
	pair<long,long> location; //Creats pair with line and word numb
	location.first = line_numb;
	location.second = word_numb;
	
	string decoded = decode_map[location];
	return decoded;
	
	
} 


/*int main()
{
	map<string, vector<pair<long,long>>> encode_map;
	map<pair<long,long>, string> decode_map;
	process_file("gburg.txt",encode_map, decode_map);
	auto word = encode_map["we"];
	auto first_instance = word[4];
	cout << first_instance.first << endl;
	cout << first_instance.second << endl;
	
	pair<long,long> location;
	location.first = 11;
	location.second = 5;
	auto word2 = decode_map[location];
	cout << word2 << endl;
	
	cout << endl;
	
	
	vector<string> words={"fourscore", "seven", "fathers"};
	for(string w: words)
	{
		cout << encode(w,encode_map) << endl;
	}
	
	cout << endl;
	
	cout << decode("0:0", decode_map);
	
	
}
*/



