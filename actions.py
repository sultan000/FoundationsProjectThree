# UTILS AND FUNCTIONALITY
from data import  population, clubs
from components import Club, Person

my_name = input("what is your name")
my_age = input("how old are you")
my_bio = input("say semothing about your self")
myself = Person(my_name, my_bio, my_age)

def introduction():
    print("Hello, %s. Welcome to our portal." % my_name)
    options()

def options():
    
    #print("would you like to: \n 1 ) create a new club. \n 2) browse and join clubs. \n 3) view existing clubs \n 4) display members of a clubs \n -1) close application") 
    
    text= """
    1 - Create a new club
    or: 
    2- browse and join club.
    or:
    3- view existing clubs.
    or:
    Display members of club.
    or:
    -1 close application 
    """
    print(text)
    option = input()
    while True :
       
        if option == "1" : 
            create_club()
        elif option == "2" : 
            view_clubs()
            join_clubs()
        elif option == "3" : 
             view_clubs()
        elif option == "4" :    
            view_club_members()
        elif option == "-1" :
            quit()
        else : 
             option = input("invalid option")

def create_club():
    
    club_name = input("pick a name for your awesome new club")
    club_dis = input("what is your club about?")
    new_club= Club(club_name,club_dis)
    new_club.recruit_member(myself)
    new_club.assign_president(myself)
    clubs.append(new_club)
    new_club.assign_president(myself)
    print("enter the numbers of the people you would like to recruit to your club(-1 to stop)")
    for index,person in enumerate(population) : 
        print ("[%s ] %s" % (index +1, person.name))
    while True : 
        member = input()
        if member == '-1' : 
            break
        elif int(member) >= 1 and int(member) <= len(population) :
            new_club.recruit_member(population[int(member)-1])
            print ("member has been added")
        else : 
            print("invalid") 
    text = (""" 
          here is your club : 
          %s
          %s
          Members : 
          """ % (new_club.name, new_club.description))
    print(text)
    new_club.print_member_list()   

        #for i, person in enumerate(population):
        #print ("[%s] %s" % (i+1,person.name))
    #x = input("")
    #while  x != '-1' : 
     #   if int(x) <= len(population):
      #    new_club.recruit_member(population[int(x)-1])
       #   print("new user added %s" % population[int(x)-1].name)
        #x = input("what else would you like to add ?")
    #new_club.print_member_list()
    #options()

def view_clubs():
    for club in clubs :
        text=("""
        Name: %s
        Description: %s
        Members: %s
        """ % (club.name,club.description,len(club.members)))
        print(text)
        # print("NAME: %s \nDescription %s \nMembers: %s \n" %(theclub.name,theclub.description,len(theclub.members)))


    

def view_club_members():
    view_clubs()
    club_name = input("enter the name of club you would like to see ")
    for club in clubs:
        if club_name.lower() == club.name.lower() : 
            print(view_club_members())

def join_clubs():
    flag = False
    view_clubs()
    club_name = input("enter the name of club you would like to join")
    for club in clubs : 
        if club_name.lower() == club.name.lower() : 
            club.recruit_member(myself) 
            flag = True
    if flag == False : 
        print("club does not exist")
        join_clubs()       

def application():
    introduction()
    
    
