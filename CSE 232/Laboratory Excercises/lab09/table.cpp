/*
David Flores flores45@whippet
2016-03-22
table.cpp

Your Comments
*/

#include <iostream>
using std::cout; using std::endl;
#include <vector>
using std::vector;
#include <random>
using std::mt19937_64; using std::uniform_int_distribution;
#include <limits>
using std::numeric_limits;

#include "table.h"

Table::Table(long width, long height, long val)
{
	width_ = width;
	height_ = height;
	
	t_.assign(height_, vector<long>(width_, val));
}

void Table::fill_random(long lo, long hi, unsigned int seed)
{
	mt19937_64 mt(seed);
	uniform_int_distribution<long> dist(lo, hi);
	
	for (int r = 0; r < height_; r++)
	{
		for (int c = 0; c < width_; c++)
		{
			t_[r][c] = dist(mt);
		}
	}
}

bool Table::set_value(unsigned int row_num, unsigned int col_num, long val)
{
	if (row_num < height_ && col_num < width_)
	{
		t_[row_num][col_num] = val;
		
		return true;
	}
	else
	{
		return false;
	}
}

long Table::get_value(unsigned int row_num, unsigned int col_num) const
{
	if (row_num < height_ && col_num < width_)
	{
		return t_[row_num][col_num];
	}
	else
	{
		return numeric_limits<long>::lowest();
	}
}

void Table::print_table(ostream& out)
{
	for (int r = 0; r < height_; r++)
	{
		for (int c = 0; c < width_; c++)
		{
			out << t_[r][c] << ",";
		}
		out << endl;
	}
}
