ifdev:
	python setup-dev.py build_ext -if 
if:
	python setup.py build_ext -if 

inf:
	python setup.py build_ext -i

sdist:
	pyton setup.py sdist

tpm:
	gcc -fPIC -c src/tpm/*.c 
	gcc -shared -Wl,-soname,libtpm.so.1 -o libtpm.so.1.0.0 *.o
	rm -f *.o
	mv libtpm.so.1.0.0 /home/phn/lib/tpm/
	ln -s /home/phn/lib/tpm/libtpm.so.1.0.0  /home/phn/lib/tpm/libtpm.so.1
	ln -s /home/phn/lib/tpm/libtpm.so.1  /home/phn/lib/tpm/libtpm.so
	echo "Add /home/phn/lib/tpm/ to LD_LIBRARY_PATH"