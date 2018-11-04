'''
Game where you try to make all the words you can given some letters

author Tim Rotzinger 03/11/2018

'''
import cmd

WORDS_FILE_PATH = "C:\wordgame\words.txt"

class Words(object):
    def __init__(self):
        self.words = None
        with open(WORDS_FILE_PATH, 'r') as wordsfile:
            self.words = wordsfile.read().strip().split()
            
    def words_from_letters(self, letters):
        '''
        input:  letters, a list of letters to build words from
        output: a set of words that can be built from the letters
        
        Given some letters, return a set where the values are the 
        words that can be made from the letters (no repeats)
        '''
        words_from_letters = []
        print (letters)
        for word in self.words:
            tmp_word = list(word)
            print (tmp_word)
            flag = True
            for letter in letters:
                if letter not in tmp_word:
                    flag = False
            if flag:
                words_from_letters.append(word)
        return words_from_letters
        
if __name__ == "__main__":
    words = Words()
    #print (words.words[:10])
    l = ['a', 't', 'r', 'd', 'u']
    print (words.words_from_letters(l))
    print ("Done.")
	