
#include<iostream>
#include<xmmintrin.h>


std::ostream& operator<<(std::ostream& os, __m128 &vfloat){
	float* pfloat = reinterpret_cast<float*>(&vfloat);
	for(int i=0; i<4; i++){
		os << vfloat[i] << ", ";
	}
	return os << std::endl;
}



int main(int carg, char** larg){
	
	__m128 v_float = _mm_set_ps1(2.3);

	std::cout << v_float;

}


