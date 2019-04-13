#include <iostream>
using namespace std;

// =================================================================

// print current array
void array_print(int *input, int size) {

	cout << "{" << *(input);
	for(int i=1; i<size; i++){
		cout << ", " <<  *(input+i);
	}
	cout << "}" << endl;
}


// sort input array via bouble sort alg.
int bouble(int *array, int size_real) {
	// declaration
	int hold;
	bool done = 0;

	// process
	cout << endl << "Called bouble" << endl;
	cout << endl << "Input array: ";
	array_print(array, size_real);

	for(int h=0; h<(size_real-1); h++) {

		// check for early break		
		if (done) {
			cout << "early termination, already done" << endl;
			break;
		}

		// predict early break
		done = 1;

		for(int i=0; i<(size_real-1); i++){

			if (*(array+i)>*(array+i+1)) {
				// swap values
				hold = *(array+i);
				*(array+i) = *(array+i+1);
				*(array+i+1) = hold;
				// no early break after array change
				done = 0;
			}	
		}
		// print result of round	
		cout << "after " << h+1 << "th round: ";
		array_print(array, size_real);
	}
	// print final array
	cout << "Function output:";
	array_print(array, size_real);
	cout << endl;
	
	return 0;
}

// =================================================================

int main(){
	
	int array[10] = {6, 5, 2, 1, 4, 3, 12, 0, 32, 11};
	int *arrayPoint = array;
	int arrayLength = (sizeof(array)/sizeof(*array));

	
	// call boublesort	
	bouble(arrayPoint, arrayLength);
	
	array_print(arrayPoint, arrayLength);

	return 0;
}
