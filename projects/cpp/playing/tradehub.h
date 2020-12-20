#include<iostream>
#include "clist.h"
#include "planet.h"


class tradehub{

	private:
		clist<planet> plist;
		int food_sup;
		int food_dem;

		int mineral_sup;
		int mineral_dem;


	public:
		
		// constructor
		tradehub();

		// methods
		void market_upd();
		void calc_prices();

};
