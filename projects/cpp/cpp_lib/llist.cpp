#include<iostream>


template <typename T>
void t_print(T var){
	std::cout << "We are now printing the type " << typeid(var).name() <<
			" and the variable var = " << var << std::endl;
}	


struct t_struct{
	
	// variables
	int numb = 0;
	t_struct* fp = NULL;
	t_struct* bp = NULL;
};

struct s_array{
	t_struct* init = new t_struct;
	t_struct* last = init;
	int n_elem = 1;

	
	// overloads
	int& operator[](int x){
		t_struct* np = init;
		for(int i=0; i<x; i++){
			np = np->fp;	
		}
		return np->numb;
	}
	
	
	// methods
	void add(int new_int){
		//do stuff
		t_struct* next;
	        next = new t_struct;
		next->numb = new_int;
		last->fp = next;
		next->bp = last;
		last = next;
		n_elem++;
	}

	void del(int pos){
		// navigate to del item
		t_struct* ip = init;
		for(int i=0; i<pos; i++){
			ip = ip->fp;
		}

		// add case where only init element exists
		if ((ip->bp != NULL) and (ip->fp != NULL)) {
			// move forwad p of pref elem to next elem
			ip->bp->fp = ip->fp;
			// move backward p of next elem to prev elem
			ip->fp->bp = ip->bp;
			// delete elemt
			free(ip);
		} else if((ip->bp != NULL) and (ip->fp == NULL)) {
			// set forward p of pref elem to NULL
			ip->bp->fp = NULL;
			// set last elem to new end
			this->last = ip->bp;
			// delete last elemt
			free(ip);
		} else if((ip->bp == NULL) and (ip->fp != NULL)) {
			// set backward p of next elem to NULL
			ip->fp->bp = NULL;
			// set new initial element
			this->init = ip->fp;
			// delete first elem
			free(ip);
		}
		n_elem--;
	}
	
	// print entire linked list
	void print(){
		t_struct* ip = init;
		std::cout << "[ ";
		for(int i=0; i<n_elem; i++){
			std::cout << ip->numb << " ";
			ip = ip->fp;	
		}
		std::cout << "]" << std::endl;

	}
	
};


int main(int argc, char* argv[]){
	
	s_array inta;
	inta[0] = 8;
	inta.add(5);
	inta.add(3);
	inta.add(1);
	printf("added numbers 5,3,1 and set inta[0] to 8\n");
	inta.print();
	inta[2]=77;
	inta.del(1);
	printf("set inta[2] to 77 and deleted element 1\n");
	inta.print();
	inta.del(0);
	printf("delete first elem\n");
	inta.print();
	inta.del(1);
	printf("delete last elem\n");
	inta.print();
	return 0;
}
