/*
David Flores
2016-03-29
circbuf.cpp
*/

#include <vector>
using std::vector;
#include <iostream>
using std::ostream; using std::endl;
#include <stdexcept>
using std::runtime_error;

#include "circbuf.h"

CircBuf::CircBuf(long size)
{
	size_ = size;
	count_ = 0;
	front_ = 0;
	back_ = 0;
	buffer_.assign(size, 0);
}

long CircBuf::pop_front()
{
	if (empty())
	{
		throw runtime_error("Accessing an empty Circular Buffer. Idiot.");
	}
	else
	{
		auto val = buffer_.at(front_);
		
		front_++;
		if (front_ >= size_)
		{
			front_ %= size_;
		}
		count_--;
		
		return val;
	}
}

bool CircBuf::remove()
{
	if (empty())
	{
		return false;
	}
	else
	{
		front_++;
		if (front_ >= size_)
		{
			front_ %= size_;
		}
		count_--;
		
		return true;
	}
}

bool CircBuf::add(long val)
{
	if (full())
	{
		return false;
	}
	else
	{
		buffer_.at(back_) = val;
		
		back_++;
		if (back_ >= size_)
		{
			back_ %= size_;
		}
		count_++;
		
		return true;
	}
}

bool CircBuf::empty() const
{
	if (count_ <= 0)
	{
		return true;
	}
	else
	{
		return false;
	}
}

bool CircBuf::full() const
{
	if (count_ >= size_)
	{
		return true;
	}
	else
	{
		return false;
	}
}

ostream& operator<<(ostream &out, const CircBuf &cb)
{
	out << "[";
	if (cb.empty())
	{
		for (auto i = 0; i < cb.size_; i++)
		{
			out << "x,";
		}
	}
	if (cb.full())
	{
		for (auto i = 0; i < cb.size_; i++)
		{
			out << cb.buffer_.at(i) << ",";
		}
	}
	else
	{
		for (auto i = 0; i < cb.size_; i++)
		{
			if ((i >= 0 && i < cb.front_ && cb.back_ > cb.front_)
				 || (i >= cb.back_ && i < cb.front_)
				 || (i < cb.size_ && i >= cb.back_ && cb.front_ < cb.back_))
			{
				out << "x,";	 
			}
			else
			{
				out << cb.buffer_.at(i) << ",";
			}
		}
	}
		
	out << "]" << endl;
	return out;
}
