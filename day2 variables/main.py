# variable = A container for a value (string,integer,float,boolean)
# A variable behaves as if it was the value it contains

# Strings

first_name = "Bro"
food = "pizza"
email = input ("enter your email: ")

print(first_name,"code")
print(f"hello {first_name}")
# print(f"teacher {first_name}")
print(f"you like {food}")
print(f"your email is {email}")


# Integers

age = int(input("enter your age: "))

if age>=18:
    print(f"you can vote {age}")

else:
    print(f"sorry age is not valid {age}")


# Float

a = float(input("enter first number: "))
b = float(input("enter second number: "))
operator = input("+,-,*,/,gst: ")

if operator == "+":
    print(f"sum of {a} {b} is {a+b}")
elif operator == "-":
        print(f"sum of {a} {b} is {a-b}")
elif operator == "*":
        print(f"sum of {a} {b} is {a*b}")
elif operator == "/":
        print(f"sum of {a} {b} is {a/b}")
        
elif operator == "%":
        print(f"Percentage of {a} out of {b} is {(a/b)*100}%")

elif operator == "gst":
       gst = (a*18)/100
       print(f"GST amount: ₹{gst}") 
       print(f"Final price: ₹{a+gst}")

else :
       print("wrong input")


#boolean

age =int(input("Enter your age: "))

has_license = age>=18

if has_license:
    print("You are eligible to apply of a driving liences")

else:
    print("you are not eligible yet.")


