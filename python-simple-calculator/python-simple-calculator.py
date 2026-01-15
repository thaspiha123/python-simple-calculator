def number():
  #ask user for input
   num1 = int(input("Enter the First Number:"))
   num2 = int(input("Enter the Second Number:"))
  #show choices
   print("Choices:")
   print("2.SUBTRACT")
   print("3.MULTIPLY")
   print("4.DIVIDE")
  #ask user to select choices
   choices= int(input("Enter any one choices (1-4):"))
      
   if choices==1:
      print("result=",num1 + num2)
   elif choices==2:
      print("result=",num1 - num2)
   elif choices==3:
      print("result=",num1 * num2)
   elif choices==4:
        if num2==0:
            print("Error")
        else:
            print("result=",num1 / num2)
number()