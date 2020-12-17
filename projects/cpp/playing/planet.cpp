#include"planet.h"
#include<iostream>

// =======================================================
// =======================================================


// class constructor
planet::planet(){
	size = 0;
	population = 0;
	type = 0;
}

planet::planet(int s, int p, int t){
	size = s;
	population = p;
	type = t;
}

// =======================================================

// class functions - getter
const int& planet::gsize(){
	return size;
}

const int& planet::gpop(){
	return population;
}

const int& planet::gtype(){
	return type;
}



// =======================================================
// =======================================================








