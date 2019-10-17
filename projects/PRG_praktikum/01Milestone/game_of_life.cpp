#include<iostream>
#include<cstdlib>
using namespace std;


void print_s(int grid[][30]) {
	
	cout << "    ";
	for(int a=0; a<30; a++) {
		if(a<10) {
			cout << " " << a << " ";
		}
		else {
			cout << a << " ";
		}
	}
	cout << endl;

	cout << "   -";
	for(int b=0; b<30; b++) {
		cout << "---";
	}
	cout << endl;
	
	for(int i=0; i<30; i++) {
		if(i<10) {
			cout << " " << i << " | ";
		}
		else {
			cout << i << " | ";
		}

		for(int j=0; j<30; j++) {
	
			std::cout << grid[i][j] << "  ";
		}
		cout << endl;
	}
}

//------------------------------------------------------------------


void print_d(int *grid) {
	
	cout << "    ";
	for(int a=0; a<30; a++) {
		if(a<10) {
			cout << " " << a << " ";
		}
		else {
			cout << a << " ";
		}
	}
	cout << endl;

	cout << "   -";
	for(int b=0; b<30; b++) {
		cout << "---";
	}
	cout << endl;
	
	for(int i=0; i<30; i++) {
		if(i<10) {
			cout << " " << i << " | ";
		}
		else {
			cout << i << " | ";
		}

		for(int j=0; j<30; j++) {
	
			std::cout << grid[(i*30) + j] << "  ";
		}
		cout << endl;
	}
}


void random(int grid[][30]) {

	for(int i=0; i<30; i++) {

		for(int j=0; j<30; j++) {
			grid[i][j] = (rand()%10);	
		}

	}

}


void copy(int *grid, int grid2[][30]) {

	for(int i=0; i<30; i++) {

		for(int j=0; j<30; j++) {
			grid[(i*30)+j] = grid2[i][j];	
		}

	}
}


void looper(int s_grid[][30], int *grid_d) {
	int status(1);
	string input_string;
	cout << endl;
	while (status) {
		cout << "Hello there, please give me an input: ";
		getline(cin, input_string);
	
		if(input_string == "") {
			status = 0;
		}
		else if(input_string == "random") {
			random(s_grid);
		}
		else if(input_string == "copy") {
			copy(grid_d, s_grid);
		}
		else if(input_string == "print s") {
			print_s(s_grid);
		}
		else if(input_string == "print d") {
			print_d(grid_d);
		}
		else {
			cout << "False, input, please try again" << endl;
		}

		cout << endl;

	}



}




//------------------------------------------------------------------------

int main() {
	
	srand(time(0));
	static int s_grid[30][30];
	
	for(int i=0; i<30; i++) {

		for(int j=0; j<30; j++) {
			s_grid[i][j] = 0;
		}

	}

	int grid_d[30*30] = {0};

	looper(s_grid, grid_d);
	

	return 0;




}












