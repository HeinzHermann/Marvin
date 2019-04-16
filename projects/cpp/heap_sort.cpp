#include <iostream>
#include "head_print.hpp"

using namespace std;



// =======================================================================
// == test functions

void test_print() {

	int array[6] = {6, 5, 4, 3, 2, 1};
	int *arrayP = array;
	int size = (sizeof(array)/sizeof(*array));

	cout << "sizeof(array) = " << sizeof(array) << endl;
	cout << "sizeof(*array) = " << sizeof(*array) << endl;
	cout << "sizeof(&array) = " << sizeof(&array) << endl;
	cout << "array = " << array << endl;
	cout << "*array = " << *array << endl;
	cout << "&array = " << &array << endl;
	cout << "size = " << size << endl;

}

// =======================================================================
// == defined functions


// repair down
int drepair(int *heap, int size, int position) {
	// check for position = 0 case...
	int hold
	if((position*2)+1 <= size) {

		if(*(heap+position) > *(heap+(position*2))) {
			hold = *(heap+position);
			*(heap+position) = *(heap+(position*2));
			*(heap+(position*2)) = hold;
			drepair(heap, size, position*2);
		} else if(*(heap+position) > *(heap+((position*2)+1)) {
			hold = *(heap+position);
			*(heap+position) = *(heap+((position*2)+1));
			*(heap+((position*2)+1)) = hold;
			drepair(heap, size, (position*2)+1);
		}

	} else if(position*2 <= size) {
		if(*(heap+position) > *(heap+(position*2))) {
			hold = *(heap+position);
			*(heap+position) = *(heap+(position*2));
			*(heap+(position*2)) = hold;
			drepair(heap, size, position*2);
		}

	}
	return 0;
}



// main minheap function
int minheap(int *array, int size) {
	
	cout << "called minheap" << endl;
	
	int aCounter = 0;
	int heap[size];
	// initialize array
	for(int i=0; i<size; i++) {
		heap[i] = 99999;
	}

	// heap buildup
	for(int j=0; j<size; j++) {
		heap[j] = *(array+j);
		

	}
	


	return 0;
}


// =======================================================================
// == main function


int main() {

	int array[6] = {6, 5, 4, 3, 2, 1};
	int *arrayP = array;
	int size = (sizeof(array)/sizeof(*array));
	//print_Array(arrayP, size);
	cout << "initial array: ";
	parray(arrayP, size);
	minheap(array, size);

	return 0;

}

