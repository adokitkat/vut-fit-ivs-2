#Pasieme pytóny Makefile

MAIN=main.py
MATH_LIB=mathematica.py
MATH_TESTS=calc_tests.py
PROFILE=profiling.py
ZIP_FILE=xmlkvy00_xmudry01_xpauld00_xkoprd00

.PHONY:
	all
	pip
	init
	pack
	clean
	test
	doc
	run
	profile

#preloží projekt a program pre profiling
all: pip run	
	
pip: 
	pip3 freeze
	
init:
	pip3 install -r requirements.txt

#zabalí projekt tak, aby mohol byť odovzdaný
pack:
	cd ../.. && zip -r $(ZIP_FILE).zip *

#vyčistí nepotrebné súbory
clean:

#spustí testy pre matematickú knižnicu
test:$(MATH_TESTS)
	python3 $(MATH_TESTS)

#generovanie dokumentácie pre matematickú knižnicu
doc: Doxyfile
	cd .. && rm -rf doc
	cd .. && mkdir doc && cd doc && doxygen ../src/$^

#spustí program
run:$(MAIN)
	python3 $(MAIN)

#spustí profiling
profile:$(PROFILE)
	python3 $(PROFILE)

installer: main.py mathematica.py gui.py requirements.txt
	bash installer.sh