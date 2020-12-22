#include "planet.h"
#include<iostream>

// =======================================================
// =======================================================

// definitions

//#define scriptflow

// =======================================================

// class constructor
planet::planet(){
	
	size = 0;
	population = 0;
	type = 0;
	this->planet_mupd();
}

planet::planet(int s, int p, int t){
	size = s;
	population = p;
	type = t;
	this->planet_mupd();
}

// =======================================================

// overloads
std::ostream& operator<<(std::ostream& os, const planet& plan){
	os << &plan;
	return os;
}


// =======================================================

// class functions - getter
const int& planet::gsize(){ return size; }

const int& planet::gpop(){ return population; }

const int& planet::gtype(){ return type; }

const int& planet::gfstored(){ return food_stored; }

const int& planet::gmstored(){ return mineral_stored; }



void planet::planet_prod(){
	#ifdef scriptflow
	std::cout << "running planet_porod()" <<std::endl << std::endl;
	#endif
	
	// standin for actual stuff
	this->food_prod = (this->population+1);
	this->mineral_prod = (this->population+1);
}


void planet::need_upd(){
	#ifdef scriptflow
	std::cout << "running need_upd()" <<std::endl << std::endl;
	#endif

	// standin for actual stuff
	food_need = population;
	mineral_need = population;

	int food_stored = food_prod - food_need; //+ food_stored;
	int mineral_stored = mineral_prod - mineral_need; //+ mineral_stored;

}


void planet::planet_pop(){
	#ifdef scriptflow
	std::cout << "running planet_pop()" <<std::endl << std::endl;
	#endif

	if(food_stored > 0 && mineral_stored > 0 && population < size){
		this->population++;
		this->food_need = this->population;
		this->mineral_need = this->population;
		
	} else if(food_stored < 0){
		this->population--;

	// add condition for negative minerals
	}
}


void planet::planet_mupd(){
	#ifdef scriptflow
	std::cout << "running planet_upd()" <<std::endl << std::endl;
	#endif

	this->planet_prod();
	this->need_upd();
}

// =======================================================
// =======================================================








