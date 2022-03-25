from word_list import word_list
from random import randint

def search(crt,pos,wrg,wrg_pos):
    def wrapped(word):
        rest =dict(zip(range(5),word))
        for s in wrg:
            if s in word:
                return False
        for i,s in crt:
            if word[i]!=s:
                return False
            else:
                if s in rest.values():
                    del rest[i]
        for i,s in wrg_pos:
            if word[i]==s:
                return False
        for s in pos:
            if s not in rest.values():
                return False
        return True
    return wrapped

wl = word_list
crt =set()
pos =set()
wrg =set()
wrg_pos=set() 
word = 'world' 
for i in range(6): 
    res = input()
    for i in range(5):
        if res[i]=='c':
            crt.add((i,word[i]))
            pos.discard(word[i])
        elif res[i]=='p':
            pos.add(word[i])
            wrg_pos.add((i,word[i]))
        elif res[i]=='w':
            wrg.add(word[i])
    wl =list(filter(search(crt,pos,wrg,wrg_pos),wl))
    n = len(wl)
    rnd = randint(0,n-1)
    word = wl[rnd]
    print(word,len(wl))
