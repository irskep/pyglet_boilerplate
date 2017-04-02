.PHONY: dist run

dist:
	pyinstaller run.py \
		--name=LDTest \
		--hidden-import=future \
		--osx-bundle-identifier=com.steveasleep.ldtest \
		--windowed

run:
	./babysit.py python run.py