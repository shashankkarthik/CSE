CPPFLAGS=-std=c++11 -g

search: main.o
	g++ $(CPPFLAGS) main.o -o search

main.o: main.cpp LinearSearch.h
	g++ $(CPPFLAGS) -c main.cpp
