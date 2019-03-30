#include <iostream>



int foo(int a, int b){

	return (a + b);
};






int main() {
	
	int a,b,c,d;
	a = 5;
	b = 4;
	c = a + b;
	
	std::cout <<"a = " << a;
	std::cout <<"\nb = " << b;
	std::cout <<"\nwithout a function a + b = " << c;	

	d = foo(a,b);

	std::cout <<"\nwith the function foo(a,b) a + b = " << d;

	std::cout <<"\n\n"; //empty space for goot measure
	
	return 0;
	};


