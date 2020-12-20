#include<iostream>
#include "tradehub.h"


using namespace std;


// constructor
tradehub::tradehub(){

	clist<planet> plist; // causes problems with linker

	int food_sup = 0;
	int food_dem = 0;

	int mineral_sup = 0;
	int mineral_dem = 0;
	// add constructor
}



// methods
/*
void tradehub::market_upd(){

	// reset variables for next tick
	food_sup = 0;
	food_dem = 0;

	mineral_sup = 0;
	mineral_dem = 0;


	for(int i=0; i<plist.size(); i++){

		plist[i].planet_mupd();
		// add surplus to supply or deficit to demand
		if(plist[i].gfstored() > 0){
			food_sup += plist[i].gfstored();
		} else {
			food_dem -= plist[i].gfstored();
		}


		if(plist[i].gmstored() > 0){
			mineral_sup += plist[i].gmstored();
		} else {
			mineral_dem -= plist[i].gmstored();
		}
	}
}
*/

void tradehub::calc_prices(){
	// add stuff
}



