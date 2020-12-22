#include<iostream>
#include "tradehub.h"

using namespace std;


// constructor
tradehub::tradehub(){

	clist<planet> plist; // causes problems with linker

	int food_sup = 0;
	int food_dem = 0;
	float food_price = 0.f;

	int mineral_sup = 0;
	int mineral_dem = 0;
	float mineral_price = 0.f;
	// add constructor
}



// methods
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

void tradehub::calc_prices(){
	/*
	   prices per commodity scaled to one with law of supply and law of demand

	   lin func for demand: price(item) = 1 - (item/max_dem) [goes 1 -> 0]
	   lin func for supply: price(item) = (item/max_sup)     [goes 0 -> 1]

	   	price(dem)	= price(sup)
	   <==> item		= 1 / (1/max_dem + 1/max_sup)
	   
	   calc price for this tick:
	   price = item/max_sup = (1 / (1/max_dem + 1/max_sup)) / max_sup

	*/
	
	food_price = (1 / (1/food_dem) + (1/food_sup)) / food_sup;
	mineral_price = (1 / (1/mineral_dem) + (1/mineral_sup)) / mineral_sup;

}



