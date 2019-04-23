PROJ_NAME=main.py
PROJ_MATH=mathematica.py
PROJ_GUI=gui.py
PROJ_TESTS=calc_tests.py
PROJ_PROFILE=profiling.py
ZIPFILE=calculator
ALLFILES=*

.PHONY:
	all
	pack
	clean
	test
	doc
	run
	profile

all:
	chmod +x $(PROJ_NAME)
	chmod +x $(PROJ_GUI)
	chmod +x $(PROJ_PROFILE)

pack:
	zip $(ZIPFILE).zip $(ALLFILES)

clean:

test:
	chmod +x $(PROJ_TESTS)
	./$(PROJ_TESTS)
doc:
	doxygen $(PROJ_MATH)

run:
	./$(PROJ_GUI)

profile:
	chmod +x $(PROJ_PROFILE)