.PHONY: dist run

dist:
	pyinstaller run.py \
		--name=PygletGame \
		--hidden-import=future \
		--osx-bundle-identifier=com.steveasleep.PygletGame \
		--windowed

run:
	./babysit.py python run.py