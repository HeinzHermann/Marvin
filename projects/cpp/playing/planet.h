#ifndef PLANET_H
#define PLANET_H

#include<iostream>


class planet {
	private:
		// general attributes
		int size;
		int population;
		int type;

		// market
		int food_stored;
		int food_need;
		int food_prod;

		int mineral_stored;
		int mineral_need;
		int mineral_prod;
		

	public:
		planet();
		planet(int, int, int);
		

		// methods
		const int& gsize();
		const int& gpop();
		const int& gtype();
		const int& gfstored();
		const int& gmstored();

		void need_upd();
		void planet_mupd();
		void planet_prod();
		void planet_pop();


};

//overloads
std::ostream& operator<<(std::ostream&, const planet&);

#endif
