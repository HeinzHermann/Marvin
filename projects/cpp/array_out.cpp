
// =================================================================

#include "head_print.hpp"
#include <iostream>
using namespace std;

// =================================================================

// print current array
void parray(int *input, int size) {

	cout << "{" << *(input);
	for(int i=1; i<size; i++){
		cout << ", " <<  *(input+i);
	}
	cout << "}" << endl;
}


// =================================================================

