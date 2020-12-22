#include<iostream>
#include"planet.h"
#include"clist.h"

using namespace std;

void print_plan( planet* inpd){
	std::printf("size %d, population %d, type %d\n",
			inpd->gsize(), inpd->gpop(), inpd->gtype());
}



int main(int argc, char* argp[]){
	clist<int> test;
	planet creation2(5, 2, 3);

	print_plan(&creation2);
	creation2.planet_mupd();
	cout << "running planet_upd()" << endl;
	print_plan(&creation2);
	creation2.planet_mupd();
	cout << "running planet_upd()" << endl;
	print_plan(&creation2);

	/*
	std::cout << "psize = " << creation2.gsize() << std::endl;
	std::cout << "ppop = " << creation2.gpop() << std::endl;
	std::cout << "ptype = " << creation2.gtype() << std::endl;
	*/
	return 0;
}





