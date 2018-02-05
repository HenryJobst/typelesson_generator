from random import randint, shuffle

letters = ['i','t','e','r','a','n','h','s','u','d','o','v','ä','b']
#letters = ['ä','b']
mode = 1
lowercase = 1
maxchar = 600
maxlinechar = 55
minblocksize = 2
maxblocksize = 4
minwordlen = 2
maxwordlen = 6

linelen = 0
charlen = 0

def words():
    global minwordlen
    global maxwordlen
    global letters
    
    words = []
    for line in open('/usr/share/dict/ngerman'):
        lcline = line.strip()
        if len(lcline) < minwordlen:
            continue
        if len(lcline) > maxwordlen:
            continue
        isok = True
        for ch in lcline:
            if ch not in letters:
                isok = False
                break
        if not isok:
            continue

        if lowercase:
            words.append(lcline)
        else:
            words.append(line.strip())

    shuffle(words)
    return words

def handleGap():
    global linelen
    global charlen
    
    if linelen > maxlinechar:
        linelen = 0
        print('')
    elif linelen > 0:
        linelen += 1
        charlen += 1
        print(' ', end='')

def handleEnd():
    if charlen > maxchar:
        print('')
        return True
    return False

def addBlock(block):
    global linelen
    global charlen
    
    blocksize = len(block)
    
    print(block, end='')

    linelen += blocksize
    charlen += blocksize
        
while True:
    if mode == 0:
        for blocksize in range(minblocksize, (minblocksize + randint(0,maxblocksize-minblocksize+1))):
            block = ''
            for idx in range(blocksize):
                letteridx = randint(0, len(letters) - 1)
                #print('letteridx:', letteridx)
                block += letters[letteridx]

            handleGap()
            addBlock(block)
            
        if handleEnd():
            break
        
    elif mode == 1:
        mywords = words()        
        handleGap()
        idx = randint(0, len(mywords) - 1)
        block = mywords[idx]
        addBlock(block)

        if handleEnd():
            break
