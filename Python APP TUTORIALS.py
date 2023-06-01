#STRING EXAMPLE
#A program to retrieve String in reverse as well as normal form
name = "NOTES"
length = len(name)
i = 0

for n in range(-1, (-length-1), -1):
    print(name[i], "\t", name[n])
    i += 1

#concatenation
str1 = "JAVA"
str2 = "notes!"
print(str1 + str2)

print("sipho" * 5)
print("Dav" * 7)

#STRING FUNCTION AND METHOD
#A function is a block of code to carry out a specific task

#def functionName(arg1, arg2):
    #........... .
    #function bodt

#a method is called by its name but it is associated to an object
#methods are associated with objects and classes

#class classNAME:
#    def method_name(self):

        #method body

#BUILT IN STRING METHODS

#capitalize() capitalizes the first of a string

s = "mitch"
print(s.capitalize())

s = "i love python tutorial"
print(s.count('o'))
print(s.count('o', 5))
print(s.count('t'))
print(s.count('t', 2, 9))

s = "i love python tutorial"
print(s.index('i'))
print(s.index('i', 2))
print(s.index('love'))
#print(s.index('love', 7))
print(s.index('i', 0, 10))
