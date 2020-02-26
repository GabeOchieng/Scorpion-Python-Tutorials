"""numbers=[1,2,3]
numbers.insert(1,50)
print(numbers)
#list comprehension
new=[1,2,3]
out=[item**2 for item in new]
print(out)"""

#dynamic slicing scheme
"""nos=[0,1,2,3,4,5,6,7,8,9,10]
for i in range(len(nos)):
    print(nos[:11])

window_size=3
nos1=[0,1,2,3,4,5,6,7,8,9]
for i in range(len(nos1)-(window_size-1)):
    print(nos1[i:i+window_size])

#String Parsing:Spliting and Joining
people='john,kevin,oscar,dalphyn'
print(people)
new_people=people.split(',')
print(new_people)
joined=' '.join(new_people)
print(joined)
csv=','.join(new_people)
print(csv)
 
 #Tupules
person1=('Sandra',26,'MKU')
person2=('Mercy', 28,'JKUAT')
people=[person1,person2]
for name,age,college in people:
    print(name)
    print(age)
    print(college)
    print()"""

#Sets
fruits={'blueberry','raspberry','strawberry','citrus','strawberry'}
fruits1={'banana','orange','raspberry','languat','raspberry'}
all_fruits=fruits.union(fruits1)
unique_fruits=fruits1.difference(fruits)
print(unique_fruits)
print(all_fruits) 
new=[1,3,3,3,5,6,7,7,9]
brand_new=set(new)
print(brand_new)

#List Comprehensions
people=['Tony','Isaac','Tanya','Newton']
names=[]
for person in people:
    names.append(person)
print(names)
names=[person+" loves too much!" for person in people]
print(names)

movie_ratings={'Titaninc':7,'Scorpion':9,'SpiderMan':4,'BatMan':2}
new_ratings=[]
for movie in movie_ratings:
    if movie_ratings[movie]>6:
        new_ratings.append(movie)
print(new_ratings)    

new_ratings1=[movie for movie in movie_ratings if movie_ratings[movie]>6]
print(new_ratings1)

#Dictionaries
phone_book={
    'grivine':{'number':'+2547000893524','email':'grive@gmail.com'}
    #'sandra' : {'number':'+2547999784567','email':'sandie@gmail.com'}
}
print(phone_book.get('grivine'))