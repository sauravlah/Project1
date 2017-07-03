the_count = [1,2,3,4,5]
sample = ['abc', 'xyz', 'aba', '1221']
demo = [1,2,2,4,5]
fruits = ['apples', 'oranges','pears','apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for i in sample:
    x = len(i)
    print "The length of the string i is %d" %x
    print "The value of the first element is %s" %i[0]
    print "The value of the last element is %s" %i[x-1]
    if i[0] == i[x-1]:
     print "The value of required string after comparing is %s" % i











