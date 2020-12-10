# distutils: language = c++
from anagrams cimport AnagramFinder, Counter
from libcpp.memory cimport shared_ptr
from libcpp.vector cimport vector


cdef class PyAnagramFinder:
    cdef AnagramFinder *c_anangram_finder

    def __cinit__(self):
        self.c_anangram_finder = new AnagramFinder()

    def __dealloc__(self):
        del self.c_anangram_finder

    def add_word(self, word):
        return self.c_anangram_finder.add_word(word.encode('utf'))

    cpdef search(self):
        cdef vector[shared_ptr[Counter]] anagrams
        cdef vector[shared_ptr[Counter]] matches

        duplicate_words = set()
        # Matches need to be stored in an ordered set

        for c_counter in self.c_anangram_finder.anagrams:
            for previously_iterated in anagrams:
                if previously_iterated.get().is_anagram(c_counter):

                    prev_word = previously_iterated.get().word.decode()
                    curr_word = c_counter.get().word.decode()

                    if prev_word not in duplicate_words:
                        duplicate_words.add(prev_word)

                    if curr_word not in duplicate_words:
                        duplicate_words.add(curr_word)

            anagrams.push_back(c_counter)

        return duplicate_words
