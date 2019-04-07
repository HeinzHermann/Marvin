#include <iostream>
using namespace std;


int checker1(int array){
//void checker0(){

	
	//int size = (sizeof(array)/sizeof(*array));
	int size = 5;
	for(int i=0; i<size; i++){
		cout << "iteration nubmer " << i << endl;
	}

	return 0;
}



int main(){
	
	int array[6] = {1, 2, 8, 4, 6, 5};
	int integer = 5;
	int& arrayRef = integer;
	int* arrayPoint = array;
	cout << "The Array is: " << array[0] << endl;
	cout << "The length of the Array is: " << 
		(sizeof(array)/sizeof(*array)) << endl;
	cout << "Test, test: arrayRef = " << arrayRef << endl;
	cout << "Test, test: arrayPoint = " << arrayPoint << endl;
	cout << "Test, test: arrayPoint = " << *(arrayPoint + 2) << endl;
	cout << "Test, test: arrayPoint = " << *(arrayPoint) << endl;


	//checker0();
	//checker(array);
	return 0;
}
