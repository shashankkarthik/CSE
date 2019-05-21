CPPFLAGS=-std=c++11 -g -Wall

all: kthelement

kthelement: main.o
	g++ $(CPPFLAGS) main.o -o kthelement

main.o: main.cpp KthSmallest.h
	g++ $(CPPFLAGS) -c main.cpp

clean:
	rm *.o kthelement