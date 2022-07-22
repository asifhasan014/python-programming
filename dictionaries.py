#First method to create a dictionay
user = {'name':'Asif Hasan','age':30}
print(user)
#Second method to create a dictionay
user2= dict(name='Asif Hasan Talukder',age=30)
print(user2)
#Access the value of a dictionary
print(user2['name'])
print(user2['age'])
#How to add data in a empty dictionay
user3={}
user3['name']='Adib Hasan'
user3['age']='32'
print(user3)
#Third method to create a dictionay
user4= dict.fromkeys(['name','age'],'unknown')
user4['name']='Latul Hasan'
print("name of user4 is "+ user4['name'])
print("name of user4 is "+ user4.get('name'))
print(user4)

#Word counter problem
print("\n******************** word counter *************************")
def wordCount(word):
    dictonary = {}
    for char in word:
        dictonary[char] = word.count(char)
    return dictonary

print(wordCount('AsifHasan'))
print("\n******************** The End  *************************")


