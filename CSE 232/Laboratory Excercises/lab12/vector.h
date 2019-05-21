#ifndef VECTOR_H
#define VECTOR_H

#include <algorithm>
using std::copy; using std::swap;
#include <stdexcept>
using std::range_error;

namespace student
{
	template<typename T>
	class vector
	{
		private:
			T* data_;
			size_t size_;
			size_t capacity_;
						
		public:
			vector(size_t cap = 10): size_(0), capacity_(cap) {data_ = new T[capacity_];};
			vector(const vector&);
			~vector() {if (data_){delete [] data_;}};
			vector& operator=(vector);
			size_t capacity() {return capacity_;};
			size_t size() {return size_;};
			void push_back(T val);
			T& operator[](size_t val);
			T& front();
			T& back();
			void clear();
			T pop_back();
	};
	
	template<typename T>
	T& vector<T>::front()
	{
		if (size_ > 0)
		{
			return data_[0];
		}
		else
		{
			throw range_error("The vector is empty. Much like your brain.");
		}
	}
	
	template<typename T>
	T& vector<T>::back()
	{
		if (size_ > 0)
		{
			return data_[size_ - 1];
		}
		else
		{
			throw range_error("The vector is still empty. Why are you even trying anymore?");
		}
	}
	
	template<typename T>
	void vector<T>::clear()
	{
		capacity_ = 0;
		size_ = 0;
		delete [] data_;
		data_ = nullptr;
	}
	
	template<typename T>
	T vector<T>::pop_back()
	{
		T val = back();
		size_--;
		
		if (size_ < (capacity_ / 2))
		{
			capacity_ /= 2;
			T* new_data = new T[capacity_];
			copy(data_, data_ + size_, new_data);
			delete [] data_;
			data_ = new_data;
		}
		
		return val;
	}
	
	template<typename T>
	vector<T>::vector(const vector<T> &v)
	{
		size_ = v.size_;
		capacity_ = v.capacity_;
		data_ = new T[capacity_];
		copy(v.data_, v.data_ + v.size_, data_);
	}
	
	template<typename T>
	vector<T>& vector<T>::operator=(vector<T> v)
	{
		size_ = v.size_;
		capacity_ = v.capacity_;
		swap(v.data_, data_);
		return *this;
	}
		
	template<typename T>
	void vector<T>::push_back(T val)
	{
		if (size_ == capacity_)
		{
			capacity_ *= 2;
			T* new_data = new T[capacity_]();
			copy(data_, data_ + size_, new_data);
			delete [] data_;
			data_ = new_data;
		}
		
		data_[size_++] = val;
	}
	
	template<typename T>
	T& vector<T>::operator[](size_t val)
	{
		if (val < size_)
		{
			return data_[val];
		}
		else
		{
			throw range_error("Accessing index outside of vector. You done gone screw up, fool!");
		}
	}
};

#endif
