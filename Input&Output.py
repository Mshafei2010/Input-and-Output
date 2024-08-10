# Take user inputs
name = input("Enter your Name:")
age = int(input("Enter your Age:"))
height = float(input("Enter your Height:"))
gender = bool(int(input("Enter your Gender Male (1) or Female (0):")))

#Output each in line User Inputs
print("Name: ",name)
print("Age: ",age)
print("Height: ",height)
print("Gender: ",gender)

# print in one line
print("Name: ",name, end=", ")
print("Age: ",age, end=", ")
print("Height: ",height, end=", ")
print("Gender: ",gender)


#Output User Inputs
print("Name Type: ",type(name))
print("Age Type: ",type(age))
print("Height Type: ",type(height))
print("Gender Type: ",type(gender))