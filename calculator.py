def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("Choose the following,\n1.Add\n2.Subrtact\n3.Multiply\n4.Divide")

while True:
    choice=input("Enter one of 4 numbers:")
    if choice in ('1','2','3','4'):
       try:
          num1 = float(input("Enter the primary number:"))
          num2 = float(input("Enter the secondary number:"))
       except ValueError:
          print("Invalid input, enter a number")
          continue
       if choice == '1':
          print(add(num1,num2))
       elif choice == '2':
          print(subtract(num1,num2))
       elif choice == '3':
          print(multiply(num1,num2))
       elif choice == '4':
          print(divide(num1,num2))
       break
    else:
       print("Invalid")
