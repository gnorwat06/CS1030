#Gavin Norwat
#700746314
#Assignemtn 2 / problem 2.5
#Description: Calculate tips

#Step 1: Obtain the subtotal and gratuity rate
subtotal = float(input("Enter the subtotal: "))
gratuityRate = float(input("Enter the gratuity rate: "))

#Step 2: Calculate the gratuity and total
gratuity = subtotal * (gratuityRate / 100)
total = subtotal + gratuity

#Step 3: Display results rounded to two decimal points
print("The gratuity is",int(gratuity * 100)/100,
      "and the total is",int(total *100)/100)




