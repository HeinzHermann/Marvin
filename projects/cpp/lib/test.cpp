#include<iostream>


int main(int carg, char* larg[]){
	
	char a = 'a';
	char b = 'b';
	char c = 'c';
	int x = static_cast<int>(a);
	int xb = static_cast<int>(b);
	int xc = static_cast<int>(c);
	std::cout << "a = " << a << std::endl << "x = " << x << std::endl;
	std::cout << "b = " << b << std::endl << "x = " << xb << std::endl;
	std::cout << "c = " << c << std::endl << "x = " << xc << std::endl;
	return 0;


}
