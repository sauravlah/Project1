print "--------MAIN MENU--------"
print ("1. Backup ")
print ("2. User management ")
print ("3. Reboot the server")
print (30 * '-')

is_valid =0
while not is_valid :
    try:
         choice = int (raw_input('Enter your choice [1-3] : '))
         is_valid = 1
    except ValueError, e :
        print ("'%s' is not a valid integer." %e.args[0].split(":")[1])

        if choice == 1:
            print ("Starting Backup........")
        elif choice == 2:
            print ("Starting User management.....")
        elif choice == 3:
            print ("Rebooting the server..........")
        else:
            print ("Invalid number. Try again.......")