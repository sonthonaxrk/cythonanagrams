from libcpp.vector cimport vector
from libcpp.string cimport string
from libcpp cimport bool
from libcpp.memory cimport shared_ptr
from libcpp.map cimport map


cdef extern from "anagrams.cpp":
    pass


cdef extern from "anagrams.h" namespace "anagrams":

    cdef cppclass Counter:
        Counter() except +
        Counter(string word) except +
        bool is_anagram(shared_ptr[Counter] c);
        string word;


    cdef cppclass AnagramFinder:
        AnagramFinder() except +
        void add_word(string);
        vector[Counter] search();
        vector[shared_ptr[Counter]] anagrams;
