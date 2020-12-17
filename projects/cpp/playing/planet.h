#include<iostream>


class planet {
	private:
		int size;
		int population;
		int type;
	public:
		planet();
		planet(int, int, int);

		const int& gsize();
		const int& gpop();
		const int& gtype();

};


