'''
Game where you try to make all the words you can given some letters

author Tim Rotzinger 03/11/2018

'''
import cmd
import random
import string

WORDS_FILE_PATH = "C:\projects\wordgame\words.txt"

class Words(object):
    def __init__(self):
        self.words = None
        with open(WORDS_FILE_PATH, 'r') as wordsfile:
            self.words = wordsfile.read().strip().split()
        #self.words = ['tar', 'rat', 'pizza', 'boys']
            
    def words_from_letters_repeats(self, letters):
        '''
        input:  letters, a list of letters to build words from
        output: a set of words that can be built from the letters
        
        Given some letters, return a set where the values are the 
        words that can be made from the letters (with repeats)
        '''
        words_from_letters = []
        for word in self.words:
            tmp_word = list(word)
            #print (tmp_word)
            flag = True
            for letter in tmp_word:
                if letter not in letters:
                    flag = False
                    break
            if flag:
                words_from_letters.append(word)
        return [w for w in words_from_letters if len(w) > 1] 
    
    def words_from_letters(self, letters):
        '''
        input:  letters, a list of letters to build words from
        output: a set of words that can be built from the letters
        
        Given some letters, return a set where the values are the 
        words that can be made from the letters (no repeats)
        '''
        
        words_from_letters = []
        for word in self.words:
            popper_letters = letters.copy()
            tmp_word = list(word)
            #print (tmp_word)
            flag = True
            for letter in tmp_word:
                if letter not in popper_letters:
                    flag = False
                    break
                elif letter in popper_letters:
                    popper_letters.remove(letter)
            if flag:
                words_from_letters.append(word)
        return [w for w in words_from_letters if len(w) > 1]        
    
    
class WordGame(cmd.Cmd):
    def __init__(self):
        self.words = Words()
        super(WordGame, self).__init__()
    
    def _generate_letters(self, number):
        self.letters = [random.choice(string.ascii_lowercase) for i in range(int(number))]
    
    def do_get_letters(self, number):
        if hasattr(self, 'letters'):
            print (self.letters)
            return
        if number:
            self._generate_letters(number)
            print (self.letters)
        else:
            print ("enter a number")
    
    def do_new_letters(self, number):
        if number:
            self._generate_letters(number)
            print (self.letters)
        else:
            print ("enter a number")
            
    def do_answers(self, what):
        answers = self.words.words_from_letters(self.letters)
        print ("without repeats, there are {} possible words from your letters".format(len(answers)))
        print (answers)
    
    def do_answers_with_repeats(self, what):
        answers = self.words.words_from_letters_repeats(self.letters)
        print ("with repeats, there are {} possible words from your letters".format(len(answers)))
        print (answers)    
        
if __name__ == "__main__":
    #words = Words()
    #print (words.words[:10])
    #l = ['a', 't', 'r', 'd', 'u']
    #print (words.words_from_letters(l))
    #print ('with repeats : ', words.words_from_letters_repeats(l))
    game = WordGame()
    game.cmdloop("welcome to the word game!")
    print ("Done.")
	