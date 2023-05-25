import os
from pathlib import Path
import random

class Processor:

    easy_words = []
    medium_words = []
    hard_words = []

    def classify_all_words(self):

        file_dir = os.path.dirname(__file__)
        print(file_dir)


        working_path = Path(os.path.join(file_dir,'resources/words.txt'))

        try:
            contents = working_path.read_text(encoding='utf-8')
        except FileNotFoundError:
            print(f'The resource file was not found in the {working_path}.')
        else:
            #Remove special characters and tones
            contents = contents.translate({ord(i): None for i in '-,;.?,¿»«_:=+)(*&$#!|¡'})
            contents = contents.translate({ord(i): None for i in '1234567890'})
            contents = contents.translate({ord(i): 'a' for i in 'á'})
            contents = contents.translate({ord(i): 'e' for i in 'é'})
            contents = contents.translate({ord(i): 'i' for i in 'í'})
            contents = contents.translate({ord(i): 'o' for i in 'ó'})
            contents = contents.translate({ord(i): 'u' for i in 'ú'})
            #split the words and sort them
            words = contents.split()
            words.sort()

            unique_words = {}

            for word in words:
                k_word = str(word).lower().lstrip().rstrip()

                if len(k_word) < 3:
                    continue

                #Add the word the first time
                if not word in unique_words:
                    unique_words[k_word] = 1
                else:
                    #if the word already exists,tben update the counter
                    w_len = unique_words.get(k_word)
                    w_len = w_len + 1
                    unique_words[k_word] = w_len
            
            #saving_file = Path('Resources/r18.txt')
            sorted_unique_Words = sorted(unique_words.items(), key = lambda x:x[1], reverse=True)
            #print(sorted_unique_Words)

            #Group the words from easier and common to harder and uncommon
            easier_words = ''.join(list(map
                                (lambda word : word[0] + ';', 
                                    filter(lambda x: x[1] > 70 and len(x[0]) <= 3, sorted_unique_Words))))  
            
            medium_words = ''.join(list(map
                                 (lambda word : word[0] + ';', 
                                    filter(lambda x: x[1] <= 70 and x[1] > 30 and len(x[0]) > 3 and len(x[0]) < 6, sorted_unique_Words))))
            
            hard_words =  ''.join(list(map
                                 (lambda word : word[0] + ';', 
                                    filter(lambda x: x[1] <= 30 and len(x[0]) > 6  and len(x[0]) <= 8, sorted_unique_Words))))

            
            working_path_easier = Path(os.path.join(file_dir,'resources/easy.txt'))
            working_path_medium = Path(os.path.join(file_dir,'resources/medium.txt'))
            working_path_hard = Path(os.path.join(file_dir,'resources/hard.txt'))

            working_path_easier.write_text(easier_words)
            working_path_medium.write_text(medium_words)
            working_path_hard.write_text(hard_words)

    def load_words(self):

        file_dir = os.path.dirname(__file__)
        print(file_dir)


        working_easy_path = Path(os.path.join(file_dir,'resources/easy.txt'))
        working_medium_path = Path(os.path.join(file_dir,'resources/medium.txt'))
        working_hard_path = Path(os.path.join(file_dir,'resources/hard.txt'))

        try:
            easy_words_content = working_easy_path.read_text(encoding='utf-8')
            medium_words_content = working_medium_path.read_text(encoding='utf-8')
            hard_words_content = working_hard_path.read_text(encoding='utf-8')
        except FileNotFoundError:
            print(f'The resource file was not found in the {working_easy_path}.')
        else:
            self.easy_words = easy_words_content.split(';')
            self.medium_words = medium_words_content.split(';')
            self.hard_words = hard_words_content.split(';')
    
    def next_easy_word(self):
        word = ''
        while len(word) <= 0:
              word = random.choice(self.easy_words)

        self.easy_words.pop(self.easy_words.index(word))

        kword =  list(filter(lambda i:(i in word),word))
        guess =  ''.join(kword.pop(
                                kword.index(
                                    random.choice(kword))) for _ in range(len(kword)))
   
        return  (word, guess)
    
    def next_medium_word(self):

        word = ''
        while len(word) <= 0:
            word = random.choice(self.medium_words)


        self.medium_words.pop(self.medium_words.index(word))

        kword =  list(filter(lambda i:(i in word),word))
        guess =  ''.join(kword.pop(
                                kword.index(
                                    random.choice(kword))) for _ in range(len(kword)))
   
        return  (word, guess)
    
    def next_hard_word(self):

        word = ''
        while len(word) <= 0:
            word = random.choice(self.hard_words)


        self.hard_words.pop(self.hard_words.index(word))

        kword =  list(filter(lambda i:(i in word),word))
        guess =  ''.join(kword.pop(
                                kword.index(
                                    random.choice(kword))) for _ in range(len(kword)))
   
        return  (word, guess)
    

wc = Processor()
wc.classify_all_words()
wc.load_words()

for _ in range(3):
    print(wc.next_easy_word())

for _ in range(3):
    print(wc.next_medium_word())

for _ in range(3):
    print(wc.next_hard_word())

