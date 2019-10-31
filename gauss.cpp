#include <iostream>
#include <random>
#include <cmath>

int main(){
	srand48(16);
	float r;
	float prop;
	float alpha;
	float num = drand48();
	for(int i=0;i<1000;i++){
		prop = num+drand48()-0.5;
		r = exp(-prop*prop/2)/exp(-num*num/2);
		if(r>1){
			r = 1;
		}	
		alpha = drand48();
		if(alpha<r){
			num = prop;
		}
		std::cout << num << std::endl;
	}
}