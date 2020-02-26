#using temporary variable
person1='Lauriene'
person2='Lady-Liza'
temp=person1
person1=person2
person2=temp
print(person2)
print(person1)

#without using a temporary variable
person1,person2=('Lauriene','Lady-Liza')
print(person1)
print(person2)
            #unpack the tutple
person1,person2=person2,person1
print(person1)
print(person2)