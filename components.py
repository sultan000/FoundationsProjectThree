# CLASSES AND METHODS
class Person():
    def __init__(self, name, bio, age):
       
        self.name = name
        self.bio = bio
        self.age = age
        
        

class Club():
    def __init__(self, name, description):
       
        self.name = name
        self.description = description
        self.president= None
        self.members = []


    def assign_president(self, person):
       
        self.president = person
        


    def recruit_member(self, person):
        # your code goes here!
        self.members.append(person)


    def print_member_list(self):
        # your code goes here!
        for member in self.members :
            if member.name == self.president.name:
                print("- %s (%s years old , President) - %s" % (member.name,member.age,member.bio))
            else:
                print("- %s (%s years old ) - %s" % (member.name,member.age,member.bio))

