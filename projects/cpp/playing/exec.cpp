#include<iostream>
#include"planet.h"


int main(int argc, char* argp[]){
	planet creation;
	planet creation2(1, 2, 3);

	std::cout << "psize = " << creation2.gsize() << std::endl;
	std::cout << "ppop = " << creation2.gpop() << std::endl;
	std::cout << "ptype = " << creation2.gtype() << std::endl;

	return 0;
}





