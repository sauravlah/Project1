
sentence = "while I wanted to do some practise I still am not sure where to begin."

COUT = len(sentence)
print COUT

sentence1 = (sorted(sentence[:]))
joinedsentence = ''.join(sentence1)
print "This is the sorted string of characters taken without joining from the %s" %sentence1
print "This is the sorted string of characters AFTER \"joining\" from %s." %joinedsentence

