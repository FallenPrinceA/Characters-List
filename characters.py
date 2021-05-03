print("Here is a list of my main characters from various stories: ")

characters = ['ichiro pendragon heavenly dragon kings', 'ichiro kuriyama deliquent king of uA', 'ichiro fukokami tales of a monster hunter',
				'ayyomi tsukino twirl in the twilight nightmare', 'ciara shattered paradise', 'hiei nakatomi emperor battle school', 'yami kolison and jenna one soul of two hearts']

#Prints the Entire List
print(characters)

#Prints the First Element of the List
print(characters[0])

#Capitalizes the first element of the List
print(characters[0].title())

#prints at index 1 and 3 (2nd and 4th items in list)
print(characters[1].title())
print(characters[3].title())

#prints last item in the list
print(characters[-1].title())

#returns second item from the end of the list
print(characters[-2].title())

#returns third item from the end of the list
print(characters[-3].title())

#use lists to print a message
message = "The first main character I ever written for a story was " + characters[0].title() + "."
print(message)

print("------------------------------------3.1 Names ------------------------------")
#Stores a List of Names then print Each Name by Calling the Index
names = ['Ichiro Fukokami', 'Sora Niro', 'Yumeko Kaneko', 'Itsuki Kasuga', 'Sara Ayami']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

print("------------------------------------3.2 Greetings ------------------------------")
#Prints a Greeting for the Names you created in 3.1
msg1 = "Good morning " + names[0] + "-Kun, I hope your day is going well, have a great day!"
msg2 = "Good morning " + names[1] + "-Kun, I hope your day is going well, have a great day!"
msg3 = "Good morning " + names[2] + "-Kun, I hope your day is going well, have a great day!"
msg4 = "Good morning " + names[3] + "-Kun, I hope your day is going well, have a great day!"
msg5 = "Good morning " + names[4] + "-Kun, I hope your day is going well, have a great day!"
print(msg1)
print(msg2)
print(msg3)
print(msg4)
print(msg5)

print("------------------------------------3.3 Your Own List ------------------------------")
#Create your own list then print a series of statements about these lists 
creepypasta = ['I met the devil while working the Night Shift', 'I met God, the Grim Reaper, and the Devil on the Same Day', 
"I'm a retired ex priest", 
'The Devil Game', 'The Girl the Universe Forgot']

listmsg1 = "The story that is my all time favorite is " + creepypasta[0] + " it was about a man who met the Devil who tried to tempt him for his soul, had a really good twist!"
listmsg2 = "The story that stuck with me the most is " + creepypasta[1] + " it was one of my all time favorites and is about a man who died and has to meet God and the Devil to decide if he wanted to go to Heaven or Hell."
listmsg3 = "This story " + creepypasta[2] + " had the best twist and was about a priest who found out he was the anti-christ."
listmsg4 = "This story " + creepypasta[3] + " was about how to summon the Devil and had a horror twist at the end."
listmsg5 = "This story was very tragic " + creepypasta[4] + " it was about a girl who was forgotten due to a strange paranormal anomaly that erased her from the Universe."

print(listmsg1)
print(listmsg2)
print(listmsg3)
print(listmsg4)
print(listmsg5)

#Modifying the First Element in the List
mod = ['Ichiro', 'Issei', 'Sora', 'Vali']
print(mod)
mod[0] = 'Levi'
print(mod)

#Adding a New Element to the End of the list
mod.append('Ichiro')
print(mod)

#start with a empty list and use append to add elements to it
kings = []
print(kings)

kings.append('Carrie')
kings.append('I.T.')
kings.append('Dark Towers')
kings.append('The Shining')
kings.append("Salem's Lot")
kings.append('The Outsider')
kings.append('The Stand')
print(kings)

#By choosing the index you can add a new element to a list
newCharacters = ['Ichiro', 'Issei', 'Vali', 'Sora', 'Levi', 'Yuuto']
print(newCharacters)
newCharacters.insert(0, 'Saji')
print(newCharacters)

#by using Del and choosing the index you can delete a element from a list
del newCharacters[0]
print(newCharacters)

#pop removes the last item from the list and allows you to work with the last item after removing it
paradise = ['Ciara', 'Klaus', 'Amelia', 'Finn', 'Elvira', 'Isabella', 'Silas']
print(paradise)
#THE LAST ELEMENT IS REMOVED FROM THE LIST BUT NOW YOU CAN MANIPULATE IT BY KEEPING ACCESS TO IT
paradise_monster = paradise.pop()
print("One of the characters in my upcoming novel is " + paradise_monster.title() + " he has the power to turn into monsters.")
print(paradise)

#You can use pop for any element in the list however doing so removes it from the list completely
first_paradise = paradise.pop(0)
print("The main character in paradise is " + first_paradise.title() + " she is a young girl from Ireland who gains the power to manipulate ice.")

#Remove Item by Value Only
brainstorm = ['Paradise', 'I sold my soul to the devil at a bar in New Orleans', "I met the Seven Strongest Beings at my Bar", "I'm the son of the Devil"]
the_paradise = 'Paradise'
brainstorm.remove(the_paradise)
print(brainstorm)
print("\n I decided to stop working on " + the_paradise.title() + " due to it not being a one off short story but a serial style story.")

print("------------------------------------Guest List Assignment ------------------------------")
guests = ['Ichiro', 'Yumeko', 'Vali', 'Sora', 'Jenna', 'Serafall', 'Koneko', 'Mittelt']
print("Hello " + guests[0] + " you have been invited to the party I am hosting tonight, please arrive by midnight.")
print("Hello " + guests[1] + " you have been invited to the party I am hosting tonight, please arrive by midnight.")
print("Hello " + guests[2] + " you have been invited to the party I am hosting tonight, please arrive by midnight.")
print("Hello " + guests[3] + " you have been invited to the party I am hosting tonight, please arrive by midnight.")
print("Hello " + guests[4] + " you have been invited to the party I am hosting tonight, please arrive by midnight.")
print("Hello " + guests[5] + " you have been invited to the party I am hosting tonight, please arrive by midnight.")
print("Hello " + guests[6] + " you have been invited to the party I am hosting tonight, please arrive by midnight.")
print("Hello " + guests[7] + " you have been invited to the party I am hosting tonight, please arrive by midnight.")

print("\n" + guests[2].title() + " can't make it to the party so he has been removed from the list")

guests[2] = 'Issei'

print("\nHello " + guests[0] + " you have been invited to the party I am hosting tonight, please arrive by midnight.")
print("Hello " + guests[1] + " you have been invited to the party I am hosting tonight, please arrive by midnight.")
print("Hello " + guests[2] + " you have been invited to the party I am hosting tonight, please arrive by midnight.")
print("Hello " + guests[3] + " you have been invited to the party I am hosting tonight, please arrive by midnight.")
print("Hello " + guests[4] + " you have been invited to the party I am hosting tonight, please arrive by midnight.")
print("Hello " + guests[5] + " you have been invited to the party I am hosting tonight, please arrive by midnight.")
print("Hello " + guests[6] + " you have been invited to the party I am hosting tonight, please arrive by midnight.")
print("Hello " + guests[7] + " you have been invited to the party I am hosting tonight, please arrive by midnight.")

print("\nI have found a bigger table and therefore will invite more people to the party!")
guests.insert(0, 'Rias')
guests.insert(4, 'Akeno')
guests.append('Sona')
print("Hello " + guests[0] + " you have been invited to the party I am hosting tonight, please arrive by midnight.")
print("Hello " + guests[1] + " you have been invited to the party I am hosting tonight, please arrive by midnight.")
print("Hello " + guests[2] + " you have been invited to the party I am hosting tonight, please arrive by midnight.")
print("Hello " + guests[3] + " you have been invited to the party I am hosting tonight, please arrive by midnight.")
print("Hello " + guests[4] + " you have been invited to the party I am hosting tonight, please arrive by midnight.")
print("Hello " + guests[5] + " you have been invited to the party I am hosting tonight, please arrive by midnight.")
print("Hello " + guests[6] + " you have been invited to the party I am hosting tonight, please arrive by midnight.")
print("Hello " + guests[7] + " you have been invited to the party I am hosting tonight, please arrive by midnight.")
print("Hello " + guests[8] + " you have been invited to the party I am hosting tonight, please arrive by midnight.")
print("Hello " + guests[9] + " you have been invited to the party I am hosting tonight, please arrive by midnight.")
print("Hello " + guests[10] + " you have been invited to the party I am hosting tonight, please arrive by midnight.")

#use len to print the number of guests invited to the party
print("\nThe number of guests invited to the party is : ")
print(len(guests))

print("\nI just recieved notice that I will only be able to invite two to the party tonight")
uninvite1 = guests.pop(0)
print("Hello " + uninvite1 + " I am afraid that due to the shorter venue I can only invite two the party now, sorry for late notice but you won't be able to attend.")
uninvite2 = guests.pop(2)
print("Hello " + uninvite2 + " I am afraid that due to the shorter venue I can only invite two the party now, sorry for late notice but you won't be able to attend.")
uninvite3 = guests.pop(2)
print("Hello " + uninvite3 + " I am afraid that due to the shorter venue I can only invite two the party now, sorry for late notice but you won't be able to attend.")
uninvite4 = guests.pop(2)
print("Hello " + uninvite4 + " I am afraid that due to the shorter venue I can only invite two the party now, sorry for late notice but you won't be able to attend.")
uninvite5 = guests.pop(2)
print("Hello " + uninvite5 + " I am afraid that due to the shorter venue I can only invite two the party now, sorry for late notice but you won't be able to attend.")
uninvite6 = guests.pop(2)
print("Hello " + uninvite6 + " I am afraid that due to the shorter venue I can only invite two the party now, sorry for late notice but you won't be able to attend.")
uninvite7 = guests.pop(2)
print("Hello " + uninvite7 + " I am afraid that due to the shorter venue I can only invite two the party now, sorry for late notice but you won't be able to attend.")
uninvite8 = guests.pop(2)
print("Hello " + uninvite8 + " I am afraid that due to the shorter venue I can only invite two the party now, sorry for late notice but you won't be able to attend.")
uninvite9 = guests.pop(2)
print("Hello " + uninvite9 + " I am afraid that due to the shorter venue I can only invite two the party now, sorry for late notice but you won't be able to attend.")

print("\nThe remaining guests are: " + guests[0] + " and " + guests[1] + ".")
print("Hello " + guests[0] + " you have still been invited to the party I am hosting tonight, please arrive by midnight.")
print("Hello " + guests[1] + " you have still been invited to the party I am hosting tonight, please arrive by midnight.")

#use len to print the number of guests invited to the party
print("\nThe number of guests invited to the party is : ")
print(len(guests))

del guests[0]
del guests[0]
print(guests)
print("\nThere are no more remaining guests to invite.")

#use len to print the number of guests invited to the party
print("\nThe number of guests invited to the party is : ")
print(len(guests))

print()
print()

print("-------------Sorting a List Permanently with the sort method-----------------")

newCharacters = ['Klaus Malebranche', 'Ciara Le Fay', 'Ophelia Belphegor', 'Nariko Orochito', 'Akane Orochito']
print(newCharacters)
newCharacters.sort()
print(newCharacters)

#Sort the list in opposite order using reverse method
newCharacters.sort(reverse=True)
print(newCharacters)

print("\n")

#Temporarily Sort a List using Sorted Method
Fantasy = ['Angels', 'Demons', 'Witches', 'Nymphs', 'Gods/Goddesses', 'Vampires', 'Werewolves', 'Spirits']

print("Here is the original list of fantasy races:")
print(Fantasy)

print("\nHere is the Sorted list: ")
print(sorted(Fantasy))


print("\nHere is the reverse sorted list:")
print(sorted(Fantasy, reverse=True))

print("\nHere is the original list again:")
print(Fantasy)
print("\n")

#using the reverse method you can print a list in reverse but not alphabetically reverse
newCharacters = ['Klaus Malebranche', 'Ciara Le Fay', 'Ophelia Belphegor', 'Nariko Orochito', 'Akane Orochito']
print(newCharacters)
newCharacters.reverse()
print(newCharacters)

#using len you can find the length of a list
print("\nThe number of characters in the new Characters list is: ")
print(len(newCharacters))

print("------------------------------------Location List Assignment ------------------------------")

settings = ["Fallen Harvest", "Umarekawari Forest", "Ashira City", "Hoshizora Town", "Dragon Storm", "Hagakure Town"]
print("\nThese are the various fantasy settings in my novel: ")
print(settings)

print("\nThese are the various fantasy settings in my novel in alphabetic order: ")
print(sorted(settings))

print("\nThese are the various fantasy settings in my novel: ")
print(settings)

print("\nHere is the reverse sorted list of fantasy settings in my novel : ") 
print(sorted(settings, reverse=True))

print("\nThese are the various fantasy settings in my novel: ") 
print(settings)

settings.reverse()
print("\nHere are the fantasy settings in reverse: ")
print(settings)

settings.reverse()
print("\nWhen we reverse the settings again they go back to their original state: ") 
print(settings)

settings.sort()
print("\nHere the fantasy settings list is printed in permanent alphabetic order: ") 
print(settings)

settings.sort(reverse=True)
print("\nFinally the list is printed permanently in reverse alphabetic order: ") 
print(settings)
