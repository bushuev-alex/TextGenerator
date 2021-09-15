from collections import Counter
import random
import nltk
import re


class TextGenerator(object):

    def __init__(self, some_file):
        self.file = file
        self.word_list = nltk.tokenize.regexp_tokenize(some_file.read(), r'[\S]+')
        self.trigrams = [[[self.word_list[i], self.word_list[i+1]], self.word_list[i+2]] for i in range(len(self.word_list) - 2)]
        self.trigrams_dict = {}
        self.first_word_pattern = r"^[A-Z].*[a-z]$"
        self.second_word_pattern = r"^[A-Z][a-z]*[!?.]+.*[a-z]$"
        self.last_word_pattern = r".*[.?!]$"

    def setdefault_for_trigram(self):
        for pair in self.trigrams:
            head = " ".join(pair[0])
            tail = pair[1]
            self.trigrams_dict.setdefault(head, [])
            self.trigrams_dict[head].append(tail)

    def generate_head_sentence(self):
        while True:
            some_pair = random.choice(list(self.trigrams_dict.keys()))
            if re.match(self.first_word_pattern, some_pair) and re.match(self.second_word_pattern, some_pair) is None:
                # word[0] in string.ascii_uppercase:
                break
        return some_pair

    def generate_most_prob_word(self, some_pair):
        word_counter = Counter(self.trigrams_dict[some_pair])
        return word_counter.most_common()[0][0]

    def generate_weighted_word(self, some_pair):
        word_counter = Counter(self.trigrams_dict[some_pair])
        return random.choices(list(word_counter.keys()), weights=list(word_counter.values()))[0]

    def generate_sentence(self):
        sentence_list = []
        n = 0
        first_pair = self.generate_head_sentence()  # generate start of the sentence like "The first"
        sentence_list.append(first_pair)
        n += 2
        while True:  # generate words after "The first"
            while True:  # check if generate correct word after "The first"
                some_word = self.generate_most_prob_word(first_pair)
                if re.match(self.last_word_pattern, some_word) and n <= 3:
                    return False  # Incorrect word in the end of short sentence like "The first words[.!?]"
                else:
                    break
            sentence_list.append(some_word)
            n += 1
            if re.match(self.last_word_pattern, some_word) and n > 3:
                n += 1
                break  # break cycle if sentence is correct like "The first words count five."
            else:      # generate next word
                try:
                    first_pair = sentence_list[-2].split(" ")[1] + " " + sentence_list[-1]
                except IndexError:
                    first_pair = sentence_list[-2] + " " + sentence_list[-1]
            if n == 8:  # generate last two words with correct ending [.!?]
                j = 0
                while j < 5:
                    prelast_word = self.generate_most_prob_word(first_pair)
                    prelast_pair = sentence_list[-1] + " " + prelast_word
                    last_word = self.generate_weighted_word(prelast_pair)
                    j += 1
                    if re.match(self.last_word_pattern, last_word):  # check for correct ending [.!?]
                        sentence_list.append(prelast_word + " " + last_word)
                        break
                    if j == 5:
                        return False   # It is impossible to create correct sentence in this cycle.
                break
        return " ".join(sentence_list)


file = open(input(), 'r', encoding='utf-8')
GameOfThrones = TextGenerator(file)
GameOfThrones.setdefault_for_trigram()

k = 0
while k < 10:
    sentence = GameOfThrones.generate_sentence()
    if sentence:
        print(sentence)
        k += 1

file.close()
