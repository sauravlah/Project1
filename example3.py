days = "MONDAY TUESDAY WEDNESDAY THURSDAY FRIDAY"
print "The different days of the week is:", days
print "=================================================================="
tabby_cat = "\tI'm tabbed in. "
persian_cat = "I'm split\ non a line. "
backslash_cat = "I'm \\ a \\ cat. "

fat_cat = """"
I'll do a list:
\a Cat food
\a Fishies
\a catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

while True:
    for i in ["/", "-", "|", "\\", "|"]:
        print "%s\r" %i

