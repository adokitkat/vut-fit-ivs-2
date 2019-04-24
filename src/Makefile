#Pasieme pytóny Makefile
MAIN=main.py
MATH_LIB=mathematica.py
MATH_TESTS=calc_tests.py
PROFILE=profiling.py
ZIP_FILE=xmlkvy00_xmudry01_xpauld00_xkoprd00

.PHONY:
	all
	init
	pack
	clean
	test
	doc
	run
	profile
	installer

#preloží projekt a program pre profiling
all: init run	
	
init:
	pip3 install -r requirements.txt
	pip3 freeze

#zabalí projekt tak, aby mohol byť odovzdaný
pack: doc installer clean
	mkdir -p ../../xmlkvy00_xmudry01_xpauld00_xkoprd00/repo

	cp -r ../ ../../xmlkvy00_xmudry01_xpauld00_xkoprd00/repo
	cp -r ../installer ../../xmlkvy00_xmudry01_xpauld00_xkoprd00
	cp -r ../doc ../../xmlkvy00_xmudry01_xpauld00_xkoprd00

	rm -rf ../../xmlkvy00_xmudry01_xpauld00_xkoprd00/repo/installer
	rm -rf ../../xmlkvy00_xmudry01_xpauld00_xkoprd00/repo/doc

	cd ../../ && zip -r $(ZIP_FILE).zip xmlkvy00_xmudry01_xpauld00_xkoprd00/

#vyčistí nepotrebné súbory
clean:
	rm -rf ../installer/tmp && rm -rf ../installer/usr
	rm -rf ../../xmlkvy00_xmudry01_xpauld00_xkoprd00/

#spustí testy pre matematickú knižnicu
test:$(MATH_TESTS)
	python3 $(MATH_TESTS)

#generovanie dokumentácie pre matematickú knižnicu
doc: Doxyfile
	rm -rf ../doc
	mkdir ../doc
	doxygen $(MATH_LIB)
	mv html/ ../doc
	rm -rf latex/

#spustí program
run:$(MAIN)
	python3 $(MAIN)

#spustí profiling
profile:$(PROFILE)
	python3 $(PROFILE)

installer: main.py mathematica.py gui.py requirements.txt
	bash installer.sh
