#Description: Obtain minutes and remaining seconds from the user
#input total seconds

#Prompt the user to input a value for seconds
seconds = int(input("Enter a integer for seconds: "))

#Get minutes and remaining seconds
minutes = seconds // 60
remainingSeconds = seconds % 60

#Display the results
print(seconds,"seconds is", minutes,"minutes and",
      remainingSeconds,"Seconds")
