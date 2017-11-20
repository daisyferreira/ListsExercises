
# coding: utf-8

# In[1]:


myList = ["Alan", "Beth", "Cath", "Dawn", "Elen", "Fenn"]    

for i in range(len(myList)):
    if (i+1) % 2 == 0:
        print(myList[i])


# In[2]:


from random import choice 

myList = "Alan Beth Cath Dawn Elen Fenn".split()
print(choice(myList))


# In[3]:


myList = "Alan Beth Cath Dawn Elen Fenn".split()


print(myList[::-1])
    


# In[4]:


#Step through a list of word Print only the LAST letter of each word

myList = "Alan Beth Cath Dawn Elen Fenn".split()

for index in myList:
    print(index[-1])


# In[5]:


#Step through a list of word and print a random letter of each word

from random import choice 

myList = "Alan Beth Cath Dawn Elen Fenn".split()

for i in myList:
    print(choice(i))


# In[6]:


myList = "Alan Beth Cath Dawn Elen Fenn".split()

print (len(myList))
print (len(myList[0:-1]))

myList.append("Gail")



# In[7]:


myList = "Alan Beth Cath Dawn Elen Fenn".split()


# insert takes two parametres. first is the index, sencond is what you want to insert
myList.insert(3,"Gail")
print(myList)

# index tells the index of an element
myList.index("Beth")
myList.index("Elen")



# In[8]:


temperature = [16, 13, 12, 15, 14, 12, 11, 20, 12, 19, 12, 12, 17, 12, 12]

#add a 5 between the 20 and the 12

temperature.index(20)
temperature.insert(8,5)
print(temperature)


# In[9]:


temperature = [16, 13, 12, 15, 14, 12, 11, 20, 12, 19, 12, 12, 17, 12, 12]
tem
#add three 7s to the end of the list

temperature.extend([7,7,7])
print(temperature)



# In[ ]:


temperature = [16, 13, 12, 15, 14, 12, 11, 20, 12, 19, 12, 12, 17, 12, 12]

#take out the 11

temperature.remove(11)
print(temperature)


# In[ ]:


temperature = [16, 13, 12, 15, 14, 12, 11, 20, 12, 19, 12, 12, 17, 12, 12]

#swap the 16 with the 17


temperature[0], temperature[12] = temperature[12], temperature[0]

print(temperature)


# In[ ]:


temperature = [16, 13, 12, 15, 14, 12, 11, 20, 12, 19, 12, 12, 17, 12, 12]

#remove all occurences of 12

while 12 in temperature:
    temperature.remove(12)
        
print(temperature)


# In[2]:


# Chooses a random letter in the alphabet
from random import choice
import string
wordOfChoice = "PSEUDOPSEUDOHYPOPARATHYROIDISM"
count = 0

randomLetter = choice(string.ascii_uppercase)
print(randomLetter)

#2) Counts the frequency of that random letter in the word
#"PSEUDOPSEUDOHYPOPARATHYROIDISM"
#or tells the user the random letter isnt in the word

if randomLetter in wordOfChoice:
    for letter in wordOfChoice:
        if randomLetter == letter:
            count += 1
    print("The letter {} is in the word {} {} times".format(randomLetter, wordOfChoice, count))
    
else:
    print("{} is not in the word {}".format(randomLetter, wordOfChoice))



# In[ ]:


"""Write a function that creates a STRONG password for a user, given a simple word that the user enters. It used the following algorithm:
1) Each I in the word is replaced with a 1
2) Each S in the word is replaced with a 5
3) The length of the word is appended to the end of the password."""

weakPassword = input("Enter a password that you want to make stronger")

if "i" in weakPassword:
    for i in weakPassword:
        if i == "i":
            i = "i"

print(weakPassword)

