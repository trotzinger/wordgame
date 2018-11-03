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
            self.words = wordsfile.read().strip()
    def words_from_letters(self, letters):
        '''
        input:  letters, a list of letters to build words from
        output: a set of words that can be built from the letters
        
        Given some letters, return a set where the values are the 
        words that can be made from the letters (no repeats)
        '''
        
if __name__ == "__main__":
    words = Words()
    print (words.words)
    print ("Done.")
	