/*
Shashank Karthikeyan karthik1@xserver
2016-04-18
Section 2

Your Comments
*/

#include <iostream>
using std::ostream; using std::cout; using std::endl;
#include <algorithm>
using std::swap;

#include "class-10.h"


TextBuffer::TextBuffer(size_t s)
{	
	buf_ = new char[capacity_];
	size_ = s;
	capacity_ = s;
	back_ = s-1;
	cursor_ = 0;
}

TextBuffer::TextBuffer(TextBuffer& og_buffer)
{	
	buf_ = og_buffer.buf_;
	size_ = og_buffer.size_;
	capacity_ = og_buffer.capacity_;
	back_ = og_buffer.back_;
	cursor_ = og_buffer.cursor_;
}

TextBuffer::~TextBuffer()
{
	delete [] buf_;
}

TextBuffer& TextBuffer::operator=(TextBuffer b)
{
	swap(b);
	return *this;
		
}

void TextBuffer::grow()
{
	char* temp_buf_ = buf_;
	char* big_buf_ = new char[capacity_ * 2];
	
	for(unsigned int i = 0u; i < cursor_; i++)
	{
		big_buf_[i] = buf_[i];
	}
	
	for(unsigned int i = capacity_-1; i > back_; i--)
	{
		big_buf_[i+capacity_] = buf_[i];
	}
	
	buf_ = big_buf_;
	back_ += capacity_;
	capacity_ *= 2; 
	
	delete [] temp_buf_;
	
	
}

void TextBuffer::swap(TextBuffer& buffer_2)
{
	std::swap(buf_,buffer_2.buf_);
	std::swap(size_,buffer_2.size_);
	std::swap(capacity_,buffer_2.capacity_);
	std::swap(back_,buffer_2.back_);
	std::swap(cursor_,buffer_2.cursor_);
	
}


bool TextBuffer::isfull()
{
	if (size_ == capacity_)
	{
		return true;
	}
	return false;	
}

bool TextBuffer::isempty()
{
	if (size_ == 0)
	{
		return true;
	}
	return false;
}


void TextBuffer::insert(char c)
{
	if(isfull())
	{
		grow();
	}
	buf_[cursor_] = c;
	cursor_++;
}

bool TextBuffer::del()
{
	if(cursor_ == 0)
	{
		return false;
	}
	cursor_ --;
	size_ --;
	return true;
}

bool TextBuffer::left()
{	
	if(cursor_== 0)
	{
		return false;
	}
	buf_[back_] = buf_[cursor_-1];
	cursor_--;
	back_--;
	return true;
	
}

bool TextBuffer::right()
{
	if(cursor_ == capacity_-1)
	{
		return false;
	}
	buf_[cursor_] = buf_[back_++];
	cursor_++;
	back_++;
	return true;
}

ostream& operator<<(ostream& out, TextBuffer &tb)
{
	out << "Size: " << tb.size_ << " Capacity: " << tb.capacity_<< " Cursor: " << tb.cursor_ << " Back: " << tb.back_ << endl;
	for (unsigned int i= 0u; i < tb.capacity_; i++)
	{
		out << tb.buf_[i] << ",";
	}
	out << endl;
	
	for (unsigned int i = 0u; i < tb.cursor_; i++)
	{
		out << tb.buf_[i];
	}
	out << "|";
	
	for (unsigned int i = tb.back_; i < tb.capacity_; i++)
	{
		out << tb.buf_[i];
	}
	out << endl;
	
	return out;
}


