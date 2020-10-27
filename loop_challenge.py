#loop challenge for QA consulting

#user can alter the range 
limit = int(input("Enter the limit: "))
for i in range(0, limit):

	print(i, i**2)

	if i**2 > 200:
		print("Limit exceeded")
		break


# #Alternatively user can alter value limit
# limit = int(input("Enter the limit: "))
# for i in range(0, 101):

# 	j = i**2
# 	print(i, j)
# 	if j > limit:
# 		print("Limit exceeded")
# 		break
		
