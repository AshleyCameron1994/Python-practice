#function that sums numbers from a list 
#list1 = [3, 4, 34, 98, 56]

# sumb = 0
# def sum_numbers():
# 	sumb = 0
# 	for x in list1:
# 		sumb += x
# 	return sumb
	
# print(sum_numbers())


#finds largest and smallest number in list
# print("Largest is:", max(list1), "Smallest is:", min(list1))


#program that prints out multiple version of the same string
# str1 = "abc"
# print(str1*3)

#check if inputted value from user is even or odd
# value = int(input("Please enter a value: "))

# if value % 2 == 0:
# 	print("This is an even number")
# else:
# 	print("This is an odd number")


#Program that prints list with evens from numbers list and stops after a certain value

# numbers = [    
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527
#     ]

# numbers2 = []

# for value in numbers:
# 	if value % 2 == 0 and value<237:
# 		numbers2.append(value)

# print(numbers2)


#Temperature converter
# temp = input("Input temperature you want converted(ie. 40C or 234F etc.): ")
# t_value = int(temp[:-1])
# t_unit = temp[-1]

# if t_unit.casefold() == "c":
# 	f = 32 + (9/5)* t_value
# 	print(temp, " is", f, "in Farenheit")
# elif t_unit.casefold() == "f":
# 	c = (5/9)*(t_value - 32)
# 	print(temp, " is", f, "in Celsius")
# else:
# 	print("Please input in the correct format")


#Printing out letter E in asterisks

# e_string = ""

# for row in range(0, 5):
# 	for column in range(0, 5):
# 		if column == 0 or ((column == 1 or column == 2) and ( row == 0 or row == 2 or row == 4)):
# 			e_string = e_string + "*"  
# 		else:
# 			e_string = e_string + ""
# 	e_string = e_string + "\n"
# print(e_string)

#Printing the letter M

# m_string = ""

# for row in range(0, 5):
# 	for col in range(0, 5):
# 		if (col == 0 or col == 4 or (row == 1 and (col == 1 or col == 3)) or (col == 2 and row == 2)):
# 			m_string = m_string + "*"
# 		else:
# 			m_string = m_string + " "
# 	m_string = m_string + "\n"
# print(m_string)

#Converting human years to dog years
# H_age = int(input("How long has your doggo been around in human years?: "))

# if H_age <= 2:
# 	D_age = H_age * 10.5
# 	print("Your doggo is ", D_age, " in dog years")
# else:
# 	D_age = (2*10.5) + (H_age - 2) * 4
# 	print("Your doggo is ", D_age, " in dog years")


#Program that sums integers unless they fall within certain value constraints

# a = 5
# b = 67

# if 15 < a * b < 20:
# 	print("20")
# else:
# 	print(a * b)


#Program that checks if string is integer
# str1 = input("Enter string: ")

# if all(str1[i] in "0123456789" for i in range(len(str1))):
# 	print("This is an integer")
# else:
# 	print("This is not an integer")

#Password checker

# d = a = s = 0
# pw1 = input("Enter password: ")

# for i in pw1:
# 	if i.isdigit():
# 		d += 1
# 	elif i.isalpha():
# 		a += 1
# 	else:
# 		s += 1

# if len(pw1) < 6 and len(pw1) > 17:
# 	print("Must be between 6 and 16 characters!")

# elif d == 0 or a == 0 or s == 0:
# 	print("Not the right amount of characters!")

# else:
# 	print("Password accepted")

#Print numbers in range with only even entries using search method
# import re

# a = "1"
# b = "3"
# c = "5"
# d = "7"
# e = "9"

# for i in range(100, 401):
# 	if (re.search(a, str(i))) or (re.search(b, str(i))) or (re.search(c, str(i))) or (re.search(d, str(i))) or (re.search(e, str(i))):
# 		#print("Odd number detected!")
# 		continue
# 	else:
# 		print(i)

#Same as above but print in a list
# items = []

# for i in range(100, 401):
# 	s = str(i)
# 	if (int(s[0]) % 2 != 0) or (int(s[1]) % 2 != 0) or (int(s[2]) % 2 != 0):
# 		continue
# 	else:
# 		items.append(i)
# print(items)



#Check whether letter is consonant or vowel
# vowels = ["a", "e", "i", "o", "u"]
# letter = str(input("Enter your letter pls: "))

# if len(letter) >= 2:
# 	print("Please enter ONE letter!")

# if letter.casefold() in vowels:
# 	print("This is a vowel")
# else:
# 	print("This value is a consonant")


# number = int(input("Enter number please: "))

# for i in range(1, 11):

# 	result = i * number
# 	print(number, " x ", i, " = ", result)



#Dividing binary numbers
# lst = []
# data = [num for num in input().split(",")]

# for p in data:
# 	num = int(p, 2)
# 	if not num % 5:
# 		lst.append(num)

# print(lst)


#Calculating sum and average of inputted list of numbers 

# data = [num for num in input().split(",")]
# sumb = 0
# index = 0
# for num in data:
# 	sumb += int(num)
# 	index += 1

# average = (sumb)// index 

# print("Sum is: ", sumb)
# print("Average is: ", average)

#Calculating tomorrows date

# year = int(input("Please enter the current year: "))
# month = int(input("Please enter the current month: "))
# day = int(input("Please enter the day: "))


# if month in (1,3,5,7,8,10,12):
# 	day_length = 31 
# elif month == 2:
# 	day_length = 28
# else:
# 	day_length = 30

# month_length = 12


# if day == day_length:
# 	month += 1
# 	day = 1
# else:
# 	day += 1
# 	if month == month_length:
# 		year += 1
# 		month = 1

# 	print("Please input correct date!")

# print("Tomorrows date will be [yyyy-mm-dd]:%d-%d-%d." % (year, month, day))



#Create number pattern
# count = 0

# for i in range(10):
# 	for j in range(i):
# 		print(count, end="")
# 	count += 1
# 	print()



#Calulates product of each sequence pairs and produces the distinct and odd values
# items = []

# def distinct(a):
# 	for i in a:
# 	 	for j in a:
# 	 		b = i*j
# 	 		if b % 2 != 0: 
# 	 			items.append(b) 
# 	 		else:
# 	 			continue
# 	#print(items)
# 	new = set(items)
# 	print(list(new))
# distinct([1, 3, 5, 7, 9, 10])


#Calculate sum of cubed integers lower than given integer
# def cube_sum(a):
# 	sumb = 0
# 	for i in range(a):
# 		sumb += i**3
# 	return sumb

# print(cube_sum(5))

# converting integers to binary
# binarystring = bin(12)
# print(binarystring)


#Check if string is palindrome
# string1 = input().casefold()

# if string1 == string1[::-1]:
# 	print("Is palindrome")
# else:
# 	print("Not palindrome")

# from itertools import permutations
# perm = permutations
#Check if two words are anagrams to each other
# str1 = input().casefold()
# str2 =input().casefold() 

# perm = permutations(str1)

# for i in perm:
# 	if tuple(str2) == i:
# 		print("This is an anagram")
# 		break

#Check if word is anagram to given word
# str1 = "dormitory"
# str2 = input("Enter a word that is an anagram of dormitory: ").casefold()

# for i in perm(str2):
# 	if tuple(str1) != i:
# 		continue
# 	else:
# 		print("This is anagram of dormitory")
# 		break

