.PHONY: dist run

dist:
	pyinstaller run.py -F --hidden-import=future

run:
	./babysit.py python run.py