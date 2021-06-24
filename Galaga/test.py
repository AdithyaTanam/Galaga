import itertools

def minion_game(string):
    # your code goes here
    stuart_score = 0
    kevin_score = 0
    kwords_set = gen_kevin_words(list(string))
    swords_set = gen_stuart_words(list(string))
    kscore = calculate_score(kwords_set, string)
    # print(kscore)
    sscore = calculate_score(swords_set, string)
    # print(sscore)
    if(kscore > sscore):
        print('Kevin',kscore)
    elif (kscore == sscore):
        print('Draw')
    else:
        print('Stuart', sscore)
    
def gen_kevin_words(listchars):
    words = []
    for i, start_char in enumerate(listchars):
        if start_char in ['A','E','I','O','U']:
            words.append(start_char)
            for j in range(1, len(listchars)-(i+1)+1):
                for x in ret_comb(listchars[(i+1):(i+1+j)]):
                    temp_word = start_char + ''.join(x)
                    words.append(temp_word)
    # print(set(words))
    return set(words)

def gen_stuart_words(listchars):
    words = []
    for i, start_char in enumerate(listchars):
        if start_char not in ['A','E','I','O','U']:
            words.append(start_char)
            for j in range(1, len(listchars)-(i+1)+1):
                for x in ret_comb(listchars[(i+1):(i+1+j)]):
                    temp_word = start_char + ''.join(x)
                    words.append(temp_word)
    return set(words)  

def ret_comb(filtered_listchars):
    yield from itertools.permutations(filtered_listchars,len(filtered_listchars))

def calculate_score(words_set, actual_string):
    score = 0
    for i in words_set:
        score += occurrences(actual_string, i)
    return score

def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count

if __name__ == '__main__':
    s = input()
    minion_game(s)