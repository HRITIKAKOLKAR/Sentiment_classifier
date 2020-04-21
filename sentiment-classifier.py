
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(str_word):
    words=""
    for i in str_word:
        if i not in punctuation_chars:
            words+=i
    return words

def get_pos(string_):
    pos=0
    string_=strip_punctuation(string_)
    for i in string_.split():
        if i.lower() in positive_words:
            pos+=1
            i=i.lower()
    return pos

def get_neg(string_):
    neg=0
    string_=strip_punctuation(string_)
    for i in string_.split():
        if i.lower() in negative_words:
            neg+=1
            i=i.lower()
    return neg

ptdcsv = open("project_twitter_data.csv","r")
rdcsv = open("resulting_data.csv","w")
def w(rdcsv):
    rdcsv.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    rdcsv.write("\n")

    lst =  ptdcsv.readlines()
    lst.pop(0)
    for lines in lst:
        main_lst = lines.strip().split(',')
        rdcsv.write("{}, {}, {}, {}, {}".format(main_lst[1], main_lst[2], get_pos(main_lst[0]), get_neg(main_lst[0]), (get_pos(main_lst[0])-get_neg(main_lst[0]))))    
        rdcsv.write("\n")

        

w(rdcsv)
ptdcsv.close()
rdcsv.close()

