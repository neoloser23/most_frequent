def most_frequent(word):
    freq1={}
    for letter in word:
        freq1[letter]=freq1.get(letter,0)+1
    for item in freq1:
        print("{} = {}".format(item,freq1[item]))
#most_frequent("mississippi")#test1
#most_frequent("Sagittarius")#test2
