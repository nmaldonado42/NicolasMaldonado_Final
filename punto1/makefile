.PHONY: graphs.py

graphs.py: run
	python3 graphs.py

run: normalMP
	./normalMP

normalMP: normalMP.c
	gcc -fopenmp normalMP.c -lm -o normalMP