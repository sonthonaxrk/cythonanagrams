#import <unordered_map>
#import <map>

#ifndef ANAGRAM_H
#define ANAGRAM_H

namespace anagrams {

    class Counter {
	public:
	    Counter(std::string word);
	    bool is_anagram(std::shared_ptr<Counter> c);
            std::unordered_map<char, int> counts;
	    std::string word;
    };

    class AnagramFinder {
        public:
	    std::vector<std::shared_ptr<Counter>> anagrams;
	    std::vector<Counter> search();
            AnagramFinder();
            ~AnagramFinder();
	    void add_word(std::string word);

    };
}

#endif
