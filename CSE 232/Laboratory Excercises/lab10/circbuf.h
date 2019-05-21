#ifndef CIRCBUF_CLASS
#define CIRCBUF_CLASS

#include <vector>
using std::vector;
#include <iostream>
using std::ostream;

class CircBuf
{
	private:
		vector<long> buffer_;
		long size_;
		long count_;
		long front_;
		long back_;
		
	public:
		CircBuf(long size = 10);
		long pop_front();
		bool remove();
		bool add(long val);
		bool empty() const;
		bool full() const;
		
		friend ostream& operator<<(ostream &out, const CircBuf &cb);
};

ostream& operator<<(ostream &out, const CircBuf &cb);

#endif
