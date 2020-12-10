#include <iostream>
#include "anagrams.h"


using namespace anagrams;


AnagramFinder::AnagramFinder () : anagrams() {}

AnagramFinder::~AnagramFinder () {}

void AnagramFinder::add_word(std::string word) {
	std::shared_ptr<Counter> counter = std::make_shared<Counter>(word);
	this->anagrams.push_back(counter);

}


std::vector<Counter> AnagramFinder::search() {
	return std::vector<Counter>();
}


Counter::Counter(std::string word) {
	this->counts = std::unordered_map<char, int>();
	this->word = word;

	for (char& c : word) {
		auto iter = this->counts.find(c);
		if (iter != this->counts.end() ) {
			// Increment the counter
			counts[c] = iter->second + 1;
		} else {
			// Initialise for character
			counts[c] = 1;
		}
	}
}


bool Counter::is_anagram(std::shared_ptr<Counter> c)
{
	return (this->counts == c->counts) && (this->word != c->word);
}
