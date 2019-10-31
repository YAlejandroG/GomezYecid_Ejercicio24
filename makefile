gauss.png : gauss.py gauss.dat
	python gauss.py
	
gauss.dat : gauss.x
	./gauss.x > gauss.dat
	
gauss.x : gauss.cpp
	c++ gauss.cpp -o gauss.x
	
clean : 
	rm gauss.x gauss.dat gauss.png