from random import randint
from string import ascii_lowercase,ascii_uppercase
from word_list import word_list
# word_list = set(word_list)
nwl = len(word_list)


class CTerm:
    color_map = {'red': '\033[91m',
                 'green': '\033[92m',
                 'yellow': '\033[93m',
                 'blue': '\033[94m',
                 'magenta': '\033[95m',
                 'cyan': '\033[96m',
                 'white': '\033[97m',
                 }
    reset = '\033[0m'

    @classmethod
    def c(cls,word, color):
        if color in cls.color_map:
            return f'{cls.color_map[color]}{word}{cls.reset}'


class Wordle:

    def __init__(self, times=6) -> None:
        rnd = randint(0, nwl-1)
        self.word = word_list[rnd]
        self.count = 0
        self.times = 6

    def guess(self, ans):

        if self.count >= self.times:
            return False, ''
        elif len(ans) == 5 and ans in word_list:
            self.count += 1
            if ans == self.word:
                return True, 'ccccc'
            else:
                rv = ''
                swd = set(self.word)
                wc = dict(zip(swd,map(self.word.count,swd)))
                for i in range(5):
                    if ans[i] == self.word[i]:
                        rv += 'c'
                        wc[ans[i]]-=1
                    elif ans[i] in wc and wc[ans[i]]>0:
                        rv += 'p'
                        wc[ans[i]]-=1
                    else:
                        rv += 'w'
                return True, rv
        else:
            return False, ''


def play_game_in_terminal():
    alphabet = ['white']*26
    wd = Wordle()
    for i in range(6):
        while 1:
            ans = input(f'{i+1}: give a guess:\n')
            ok, res = wd.guess(ans.lower())
            if ok:
                color_word=''
                for i in range(5):
                    color_word+=CTerm.c(ans[i].upper(),{'c':'green','p':'yellow','w':'white'}[res[i]])
                    alphabet[ord(ans[i])-97]={'c':'green','p':'yellow','w':'red'}[res[i]]
                color_alphabet =''.join(map(lambda x:CTerm.c(x[0],x[1]),zip(ascii_uppercase,alphabet)))
                print(color_alphabet)
                print(color_word)
                if res=='ccccc':
                    print(f'Correct! the wordle is "{wd.word.upper()}"')
                    return
                break
            else:
                if i==5:
                    break
                print('invalid guess')
    print(f'the wordle is "{wd.word.upper()}"')

if __name__ == '__main__':
    play_game_in_terminal()
