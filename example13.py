SAMPLE = ['abc', 'xyz', 'aba', '1221', 'accb', 'acsvsvcfsdadada']

i = len(SAMPLE)
while i > 0:
    x =  SAMPLE[i - 1]
    z = len(x)
    i = i - 1
    if z > 2:
        print "The following string has more than 2 string characters:"
        print x




