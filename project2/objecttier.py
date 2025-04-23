#
# objecttier
#
# Builds Lobbyist-related objects from data retrieved through 
# the data tier.
#
# Original author: Ellen Kidane
#
#-------------------------------------------------------------------------------------------
#Project 2: Chicago Lobbyist Database App
#Object Tier
#Date: 10/16/24
#Course: CS 341, Spring 2024, UIC
#System: Visual Studio Code
#Author: Matthew Mohaupt; mmohau3; 651525023
#Description: a console-based database application in Python using an N-tier design which consists of the data-tier, object-tier and 
#    presentation-tier
#-------------------------------------------------------------------------------------------
import datatier


##################################################################
#
# Lobbyist:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#
class Lobbyist:
   Lobbyist_ID = -1
   First_Name = ""
   Last_Name = ""
   Phone = ""

   def __init__(self, Lobbyist_ID, First_Name, Last_Name, Phone):
      self._Lobbyist_ID = Lobbyist_ID
      self._First_Name = First_Name
      self._Last_Name = Last_Name
      self._Phone = Phone

   @property
   def Lobbyist_ID(self):
      return self._Lobbyist_ID

   @property
   def First_Name(self):
      return self._First_Name

   @property
   def Last_Name(self):
      return self._Last_Name

   @property
   def Phone(self):
      return self._Phone
      

##################################################################
#
# LobbyistDetails:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   Salutation: string
#   First_Name: string
#   Middle_Initial: string
#   Last_Name: string
#   Suffix: string
#   Address_1: string
#   Address_2: string
#   City: string
#   State_Initial: string
#   Zip_Code: string
#   Country: string
#   Email: string
#   Phone: string
#   Fax: string
#   Years_Registered: list of years
#   Employers: list of employer names
#   Total_Compensation: float
#
class LobbyistDetails:
   Lobbyist_ID = -1
   Salutation = ""
   First_Name = ""
   Middle_Initial = ""
   Last_Name = ""
   Suffix = ""
   Address_1 = ""
   Address_2 = ""
   City = ""
   State_Initial = ""
   Zip_Code = ""
   Country = ""
   Email = ""
   Phone = ""
   Fax = ""
   Years_Registered = []
   Employers = []
   Total_Compensation = 0.0

   def __init__(self, Lobbyist_ID, Salutation, First_Name, Middle_Initial, Last_Name, Suffix, Address_1, Address_2, City, State_Initial, Zip_Code, Country, Email, Phone, Fax, Years_Registered, Employers, Total_Compensation):
      self._Lobbyist_ID = Lobbyist_ID
      self._Salutation = Salutation
      self._First_Name = First_Name
      self._Middle_Initial = Middle_Initial
      self._Last_Name = Last_Name
      self._Suffix = Suffix
      self._Address_1 = Address_1
      self._Address_2 = Address_2
      self._City = City
      self._State_Initial = State_Initial
      self._Zip_Code = Zip_Code
      self._Country = Country
      self._Email = Email
      self._Phone = Phone
      self._Fax = Fax
      self._Years_Registered = Years_Registered
      self._Employers = Employers
      self._Total_Compensation = Total_Compensation

   @property
   def Lobbyist_ID(self):
      return self._Lobbyist_ID
   
   @property
   def Salutation(self):
      return self._Salutation

   @property
   def First_Name(self):
      return self._First_Name
   
   @property
   def Middle_Initial(self):
      return self._Middle_Initial

   @property
   def Last_Name(self):
      return self._Last_Name
   
   @property
   def Suffix(self):
      return self._Suffix

   @property
   def Address_1(self):
      return self._Address_1

   @property
   def Address_2(self):
      return self._Address_2

   @property
   def City(self):
      return self._City

   @property
   def State_Initial(self):
      return self._State_Initial

   @property
   def Zip_Code(self):
      return self._Zip_Code

   @property
   def Country(self):
      return self._Country

   @property
   def Email(self):
      return self._Email

   @property
   def Phone(self):
      return self._Phone
   
   @property
   def Fax(self):
      return self._Fax

   @property
   def Years_Registered(self):
      return self._Years_Registered

   @property
   def Employers(self):
      return self._Employers

   @property
   def Total_Compensation(self):
      return self._Total_Compensation

##################################################################
#
# LobbyistClients:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#   Total_Compensation: float
#   Clients: list of clients
#
class LobbyistClients:
   Lobbyist_ID = -1
   First_Name = ""
   Last_Name = ""
   Phone = ""
   Total_Compensation = 0.0
   Clients = []

   def __init__(self, Lobbyist_ID, First_Name, Last_Name, Phone, Total_Compensation, Clients):
      self._Lobbyist_ID = Lobbyist_ID
      self._First_Name = First_Name
      self._Last_Name = Last_Name
      self._Phone = Phone
      self._Total_Compensation = Total_Compensation
      self._Clients = Clients

   @property
   def Lobbyist_ID(self):
      return self._Lobbyist_ID

   @property
   def First_Name(self):
      return self._First_Name

   @property
   def Last_Name(self):
      return self._Last_Name

   @property
   def Phone(self):
      return self._Phone
   
   @property
   def Total_Compensation(self):
      return self._Total_Compensation

   @property
   def Clients(self):
      return self._Clients

##################################################################
# 
# num_lobbyists:
#
# Returns: number of lobbyists in the database
#           If an error occurs, the function returns -1
#
def num_lobbyists(dbConn):
   cmd = "SELECT COUNT(Lobbyist_ID) FROM LobbyistInfo;"
   row = datatier.select_one_row(dbConn, cmd)
   return row[0]

##################################################################
# 
# num_employers:
#
# Returns: number of employers in the database
#           If an error occurs, the function returns -1
#
def num_employers(dbConn):
   cmd = "SELECT COUNT(Employer_ID) FROM EmployerInfo;"
   row = datatier.select_one_row(dbConn, cmd)
   return row[0]

##################################################################
# 
# num_clients:
#
# Returns: number of clients in the database
#           If an error occurs, the function returns -1
#
def num_clients(dbConn):
   cmd = "SELECT COUNT(Client_ID) FROM ClientInfo;"
   row = datatier.select_one_row(dbConn, cmd)
   return row[0]

##################################################################
#
# get_lobbyists:
#
# gets and returns all lobbyists whose first or last name are "like"
# the pattern. Patterns are based on SQL, which allow the _ and % 
# wildcards.
#
# Returns: list of lobbyists in ascending order by ID; 
#          an empty list means the query did not retrieve
#          any data (or an internal error occurred, in
#          which case an error msg is already output).
#
def get_lobbyists(dbConn, pattern):
   lobbyers = []
   cmd = "SELECT Lobbyist_ID, First_Name, Last_Name, Phone FROM LobbyistInfo where First_Name LIKE (?) OR Last_Name LIKE (?) GROUP BY Lobbyist_ID ORDER BY Lobbyist_ID ASC;"
   table = datatier.select_n_rows(dbConn, cmd, (pattern, pattern, ))
   #if nothing in the tabe return nothing as well
   if(table == None):
      return []
   #turn every row from the table into the appropriate lobbyist object and append it to the list lobbyers that we will return after we went through the whole table
   for row in table:
      lobbyerobject = Lobbyist(row[0], row[1], row[2], row[3])
      lobbyers.append(lobbyerobject)
   return lobbyers

##################################################################
#
# get_lobbyist_details:
#
# gets and returns details about the given lobbyist
# the lobbyist id is passed as a parameter
#
# Returns: if the search was successful, a LobbyistDetails object
#          is returned. If the search did not find a matching
#          lobbyist, None is returned; note that None is also 
#          returned if an internal error occurred (in which
#          case an error msg is already output).
#
def get_lobbyist_details(dbConn, lobbyist_id):
   #need to break down select commands because there are so many arguments to get
   #this command is to get all the info from LobbyistInfo
   infocmd = "SELECT * FROM LobbyistInfo WHERE Lobbyist_ID = (?);"
   #this is for getting years and compensation
   yearcmd = "SELECT Year FROM LobbyistYears  WHERE Lobbyist_ID = (?);"
   #this is for getting employer data
   employcmd = "SELECT DISTINCT Employer_Name FROM LobbyistAndEmployer JOIN EmployerInfo ON LobbyistAndEmployer.Employer_ID = EmployerInfo.Employer_ID WHERE Lobbyist_ID = (?) ORDER BY Employer_Name;"
   #this is for getting how much they were compensated
   costcmd = "SELECT Compensation_Amount FROM Compensation WHERE Lobbyist_ID = (?);"

   inforow = datatier.select_one_row(dbConn, infocmd, (lobbyist_id, ))
   #if nothing is returned nothing as well
   if(inforow == ()):
     return None
   yeartable = datatier.select_n_rows(dbConn, yearcmd, (lobbyist_id, ))
   employtable = datatier.select_n_rows(dbConn, employcmd, (lobbyist_id, ))
   compensationtable = datatier.select_n_rows(dbConn, costcmd, (lobbyist_id, ))
   yearslist = []
   employlist = []
   compensation = 0.00
   #if nothing is returned then no compensation
   if(compensationtable == None):
     compensation = 0.00
   #this will tally every compensation the lobbyist did
   else:
      for row in compensationtable:
         compensation = compensation + row[0]
   #this will put every year in a list so we can put in the lobbyistdetails object
   for row in yeartable:
      yearslist.append(row[0])
   #this will put every employer in a list so we can put in the lobbyistdetails object
   for row in employtable:
      employlist.append(row[0])
   #take the lobbyist found and return that lobbyistdetails object
   lobbyer = LobbyistDetails(inforow[0], inforow[1], inforow[2], inforow[3], inforow[4], inforow[5], inforow[6], inforow[7], inforow[8], inforow[9], inforow[10], inforow[11], inforow[12], inforow[13], inforow[14], yearslist, employlist, compensation)
   return lobbyer
         

##################################################################
#
# get_top_N_lobbyists:
#
# gets and returns the top N lobbyists based on their total 
# compensation, given a particular year
#
# Returns: returns a list of 0 or more LobbyistClients objects;
#          the list could be empty if the year is invalid. 
#          An empty list is also returned if an internal error 
#          occurs (in which case an error msg is already output).
#
def get_top_N_lobbyists(dbConn, N, year):
   lobbyers = []
   #if not a realistic number then dont even bother
   if(N < 1):
      return []
   #this will return us info and top paid N lobbyist in the year
   infocmd = "SELECT LobbyistInfo.Lobbyist_ID AS lid, First_Name, Last_Name, Phone, SUM(Compensation_Amount) AS money FROM LobbyistInfo JOIN Compensation ON Compensation.Lobbyist_ID = lid WHERE strftime('%Y', Period_End) = (?) GROUP BY lid ORDER BY money DESC LIMIT (?);"
   #this will return us the list of all the employers of the lobbyist
   employcmd = "SELECT DISTINCT Compensation.Client_ID, Client_Name FROM ClientInfo JOIN Compensation ON Compensation.Client_ID = ClientInfo.Client_ID WHERE Lobbyist_ID = (?) AND strftime('%Y', Period_End) = (?) GROUP BY ClientInfo.Client_ID ORDER BY Client_Name;"
   infotable = datatier.select_n_rows(dbConn, infocmd, (year, N, ))
   #if nothing in the tabe return nothing as well
   if(infotable == None):
      return []
   #turn every row from the table into the appropriate lobbyistclinet object and append it to the list lobbyers that we will return after we went through the whole table
   for row in infotable:
      #need to get the list of all clients first before making object
      employers = []
      employtable = datatier.select_n_rows(dbConn, employcmd, (row[0], str(year)))
      for erow in employtable:
         employers.append(erow[1])
         #make lobbyistclients object and append it to list that gets returned
      lobbyerobject = LobbyistClients(row[0], row[1], row[2], row[3], row[4], employers)
      lobbyers.append(lobbyerobject)
   return lobbyers
   


##################################################################
#
# add_lobbyist_year:
#
# Inserts the given year into the database for the given lobbyist.
# It is considered an error if the lobbyist does not exist (see below), 
# and the year is not inserted.
#
# Returns: 1 if the year was successfully added,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def add_lobbyist_year(dbConn, lobbyist_id, year):
   dbCursor = dbConn.cursor()
   #command to insert
   insertcmd = "INSERT INTO LobbyistYears(Lobbyist_ID, Year) VALUES((?), (?));"
   #command to check if lobbyistid is valid
   checkcmd = "SELECT Year from LobbyistYears where Lobbyist_ID = (?);"
   row = datatier.select_one_row(dbConn, checkcmd, (lobbyist_id, ))
   #if nothing shows up then bad lobbyistid
   if(row == ()):
      return 0
   #try catch block to make sure no errors occur
   try:
      dbCursor.execute(insertcmd, (lobbyist_id, year, ))
      dbConn.commit()
   except Exception as err:
      print(err)
      return 0  
   #check to see if rowcount changed, then we know changes are good
   if(dbCursor.rowcount > 0):
      return 1
   else:
      return 0


##################################################################
#
# set_salutation:
#
# Sets the salutation for the given lobbyist.
# If the lobbyist already has a salutation, it will be replaced by
# this new value. Passing a salutation of "" effectively 
# deletes the existing salutation. It is considered an error
# if the lobbyist does not exist (see below), and the salutation
# is not set.
#
# Returns: 1 if the salutation was successfully set,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def set_salutation(dbConn, lobbyist_id, salutation):
   dbCursor = dbConn.cursor()
   #command to update
   updatecmd = "UPDATE LobbyistInfo SET Salutation = (?) WHERE Lobbyist_ID = (?)"
   #command to check if lobbyistid is valid
   checkcmd = "SELECT Year from LobbyistYears where Lobbyist_ID = (?);"
   row = datatier.select_one_row(dbConn, checkcmd, (lobbyist_id, ))
   #if nothing shows up then bad lobbyistid
   if(row == ()):
      return 0
   
   #try catch block to make sure no errors occur
   try:
      dbCursor.execute(updatecmd, (salutation, lobbyist_id, ))
      dbConn.commit()
   except Exception as err:
      print(err)
      return 0  
   #check to see if rowcount changed, then we know changes are good
   if(dbCursor.rowcount > 0):
      return 1
   else:
      return 0