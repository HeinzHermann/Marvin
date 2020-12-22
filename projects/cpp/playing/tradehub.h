#ifndef TRADEHUB_H
#define TRADEHUB_H


#include<iostream>
#include "clist.h"
#include "planet.h"


class tradehub{

	private:
		clist<planet> plist;
		int food_sup;
		int food_dem;
		float food_price;

		int mineral_sup;
		int mineral_dem;
		float mineral_price;


	public:
		
		// constructor
		tradehub();

		// methods
		void market_upd();
		void calc_prices();

};

#endif
