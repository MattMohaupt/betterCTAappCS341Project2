#-------------------------------------------------------------------------------------------
#Project 2: Chicago Lobbyist Database App
#Presentation Tier
#Date: 10/16/24
#Course: CS 341, Spring 2024, UIC
#System: Visual Studio Code
#Author: Matthew Mohaupt; mmohau3; 651525023
#Description: a console-based database application in Python using an N-tier design which consists of the data-tier, object-tier and 
#    presentation-tier
#-------------------------------------------------------------------------------------------
import sqlite3
import objecttier

#print the general stats of the database at the moment
def printStats(dbConn):
    print()
    print("General Statistics:")
    #use the mfunctions from objecttier to get the information
    numLobbyies = objecttier.num_lobbyists(dbConn)
    numEmployers = objecttier.num_employers(dbConn)
    numClients = objecttier.num_clients(dbConn)
    print("  Number of Lobbyists: {:,}".format(numLobbyies))
    print("  Number of Employers: {:,}".format(numEmployers))
    print("  Number of Clients: {:,}".format(numClients))
    print()
    return

#print out a list of lobbyist's ids, names and phone numbers based on what the name the user inputted
def command1(dbConn):
    print()
    index = 0
    name = input("Enter lobbyist name (first or last, wildcards _ and % supported): ")
    print()
    idlist = objecttier.get_lobbyists(dbConn, name) #this is a list of Lobbyist objects with only id
    numLobbyies = len(idlist)
    print("Number of lobbyists found: {:}".format(numLobbyies))
    #check if too many elements in the list
    if(numLobbyies > 100):
        print("There are too many lobbyists to display, please narrow your search and try again...")
        return
    print()
    if(len(idlist) < 1):
        return
    for obj in idlist: #use for each to print out all the information needed for each object
        print("{:} : {:} {:} Phone: {:}".format(obj.Lobbyist_ID, obj.First_Name, obj.Last_Name, obj.Phone))
    print()
    return



#user inputs a lobbyist ID, output all lobbyist details from object
#    output full name, address, contact info, years registered, total compensation, list of employers
def command2(dbConn):
    print()
    inputID = input("Enter Lobbyist ID: ")
    print()
    details = objecttier.get_lobbyist_details(dbConn, inputID) #returns a lobbyistdetails object
    #if no object was created from the lobbyist id then id doesnt exist
    if(details == None):
        print("No lobbyist with that ID was found.")
        print()
        return
    
    #else print out the details of that lobbyist
    print("{:} :".format(details.Lobbyist_ID))
    print("  Full Name: {:} {:} {:} {:} {:}".format(details.Salutation, details.First_Name, details.Middle_Initial, details.Last_Name, details.Suffix))
    print("  Address: {:} {:} , {:} , {:} {:} {:}".format(details.Address_1, details.Address_2, details.City, details.State_Initial, details.Zip_Code, details.Country))
    print("  Email: {:}".format(details.Email))
    print("  Phone: {:}".format(details.Phone))
    print("  Fax: {:}".format(details.Fax))
    #can output a int list using *list without having to use a loop, but autograder has ending cologn so need to end with one too
    #though it means needing to use different print statements for years registered and int list
    print("  Years Registered:", end =' ')
    #can output a int list using *list without having to use a loop, but autograder has ending cologn so need to end with one too
    print(*details.Years_Registered, sep=", ", end=",\n")
    #can output a string list using join without having to use a loop, but autograder has ending cologn so need to end with one too 
    #   and it joins to the seperator
    #though it means needing to use different print statements for emplyers and string list
    print("   Employers: ", end=' ')
    print(", ".join(details.Employers), end= ",\n")
    print("   Total Compensation: ${:,.2f}".format(details.Total_Compensation))
    
    print()
    return

#user inputs a year, print the top N(n being how many to limit the query by) lobbyists based on their total compensation for that year
def command3(dbConn):
    print()
    npeople = input("Enter the value of N: ") #input is in form of string so need to cast it later
    if(int(npeople) < 1): #make sure n is a natural number because cant have negative positions or show the top zero of a category
        print("Please enter a positive value for N...\n")
        return
    year = input("Enter the year: ") #this input is also in string but since year is a string in the database, doesnt matter
    print()
    lobbyistlist = objecttier.get_top_N_lobbyists(dbConn, int(npeople), year) #returns a list lobbyistclient objects
    index = 0
    if(len(lobbyistlist) < 1): #get_top_n_lobbyist returns an empty list if error or nothing found so check for that
        return
    #printing out the lobbyistclient detais
    while(index < len(lobbyistlist)):
        print("{:} . {:} {:}".format((index+1), lobbyistlist[index].First_Name, lobbyistlist[index].Last_Name))
        print("  Phone: {:}".format(lobbyistlist[index].Phone))
        print("  Total Compensation: ${:,.2f}".format(lobbyistlist[index].Total_Compensation))
        print("  Clients:", end=' ')
        print(", ".join(lobbyistlist[index].Clients), end= ", \n")
        index+=1
    print()
    return

#register a lobbyist for a new year taking year input and id input
def command4(dbConn):
    print()
    year = input("Enter year: ")
    id = input("Enter the lobbyist ID: ")
    success = objecttier.add_lobbyist_year(dbConn, int(id), int(year)) #need to cast id and year since inputs are type string
    print()
    #add_lobbyist_year will return 1 on success and 0 on failure, only check for success and assume failure otherwise
    if(success == 1): 
        print("Lobbyist successfully registered.")
    else:
        print("No lobbyist with that ID was found.")
    print()
    return

#change the salutations of a lobbyist taking in id input and new salutations input
#salutation are like {mr, ms, mrs, doctor, etc}
def command5(dbConn):
    print()
    id = input("Enter the lobbyist ID: ")
    salutations = input("Enter the salutation: ")
    #need to cast id since inputs are type string but salutation is fine since it is a string in the database
    success = objecttier.set_salutation(dbConn, int(id), salutations)
    print()
    #set_salutation will return 1 on success and 0 on failure, only check for success and assume failure otherwise
    if(success == 1):
        print("Salutation successfully set.")
    else:
        print("No lobbyist with that ID was found.")
    print()
    return

##################################################################  
#
# main
#
##################################################################
print('** Welcome to the Chicago Lobbyist Database Application **')
dbConn = sqlite3.connect('Chicago_Lobbyists.db') #connect to the database
printStats(dbConn)
userinput = input("Please enter a command (1-5, x to exit): ")
#set up a while loop and a switch statement so we can continualy get user input until exit and switch to each command when specified
while(userinput != 'x'):
    match userinput:
        case "1":
            command1(dbConn)
        case "2":
            command2(dbConn)
        case "3":
            command3(dbConn)
        case "4":
            command4(dbConn)
        case "5":
            command5(dbConn)
        case _:
            print("**Error, unknown command, try again...")
    userinput = input("Please enter a command (1-5, x to exit): ")

#
# done
#
