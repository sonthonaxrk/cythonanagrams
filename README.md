# Cython Anagrams for tech test

Appologies for the delay in getting this over to you.  I appreciate this was a very simple test, but since I'm doing this in my own time I prefer to get something out of it too; that is some revision, as I have not touched any code for a few months now.

I took the liberty of using Python *and* C++ for this task.  Please rest assured that I would never do this in a real world situation, and would absolutely choose a simpler stack (I was also considering using Keras to make probablilistic anagram checker but didn't want to embarass myself).

Appologies for the quality of the code, I am extremely rusty. And I haven't packaged it properly.

## Usage

	$ python setup.y install
	$ python setup.py build_ext --inplace
	$ python test_anagrams.py
	$ anagrams file_to_test.txt

Or
	
	$ ./cli.py file_to_test.txt
