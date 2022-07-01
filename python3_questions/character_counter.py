class CharacterCounter:
    "Class description text accessible with className.__doc__"

    def __init__(self):
        self.vowel = "aeıioöuü"
        self.consonant = "bcçdfgğhjklmnprsştvyz"
        self.v_count = 0
        self.c_count = 0

    def get_word(self):
        return input("Write a word: ")

    def _character_is_vowel(self, char):
        return char in self.vowel

    def _character_is_consonant(self, char):
        return char in self.consonant

    def increase_the_counter(self):
        for char in self.word:
            if self._character_is_vowel(char):
                self.v_count += 1
            if self._character_is_consonant(char):
                self.c_count += 1
        return (self.v_count, self.c_count)

    def print(self):
        vowel, consonant = self.increase_the_counter()
        msg = "{} word has {} vowel and {} consonant characters."
        print(msg.format(self.word, vowel, consonant))

    def run(self):
        self.word = self.get_word()
        self.print()


if __name__ == "__main__":
    counter = CharacterCounter()
    # print(counter.__doc__)
    # instance = dir(counter)
    counter.run()
