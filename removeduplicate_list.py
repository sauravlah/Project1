a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
x = len(a)
print "THe number of elements is %d" % x
a.sort()
print a
while x > 0:
    if a[x-1] != a[x-2]:
        x = x-1
    elif a[x - 1] == a[x - 2]:

        print "Duplicate entry found. The entry is %d" % a[x - 1]
        print "The duplicate entry is being removed..............."
    a.pop(x - 1)
    x = x-1
print a
