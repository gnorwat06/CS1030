#Description: Obtain the current time (GMT) and compute the seconds, minutes,
#and hours

#import the time module
import time

#obtain the current time by invoking the time function
currentTime = time.time()
print(currentTime)

#Obtain the total seconds
totalSeconds = int(currentTime)
print(totalSeconds)

#Compute the current seconds from our total
currentSeconds = totalSeconds % 60

#Obtain the total minutes
totalMinutes = totalSeconds // 60

#Compute the current minutes from that
currentMinutes = totalMinutes % 60

#Obtain the total hours
totalHours = totalMinutes // 60

#Compute the current hour
currentHours = totalHours % 24

#Display the results
print("Current Time is " + str(currentHours) + ":" + str(currentMinutes) + ":"
      + str(currentSeconds) + " GMT!")
