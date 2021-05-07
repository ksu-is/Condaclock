
import datetime #importing datetime allows the program to recongnize dates as objects on my machine
from playsound import playsound #playsound allows us to play sound in python by installing with pip 

alarm_hour= int(input('What hour would you like to wake up?: ')) #this takes the hour you want to wake up using user input
alarm_minute = int(input('What minute would you like to wake up?: ')) #this takes the minute you want to wake up using user input
am_pm = str(input('am or pm?: ')) #this asks the user whether the time they entered is am or pm

print('Alarm activated!!', alarm_hour, alarm_minute, am_pm) 
#this tells the user the alarm is activated and calls the variables listed above. The variables are ran and ask for user input.

def snake_alarm(shour, sminute, ampm): 
    if (ampm == "pm"):    #this if statement says that if the user enters pm then 12 hours will be added to the hour. 
        shour = shour +12 #this is done to convert form 24hr time to regular time. 
    while (1==1):         
        if(shour == datetime.datetime.now().hour and 
        sminute == datetime.datetime.now().minute) : #see if what user input is the time on my machine then the alarm will sound
            print('WAKE UPPPPP!!!!') #when the alarm sounds then wake upp will print
            playsound(r"C:\Users\Dylan\Downloads\snakehiss2.mp3") #this is the path to the file that emits the sound of the snakes
            playsound(r"C:\Users\Dylan\Downloads\snakehiss2.mp3")
            playsound(r"C:\Users\Dylan\Downloads\snakehiss2.mp3")  
            break

snake_alarm(alarm_hour, alarm_minute, am_pm)
#this is simply calling the above function





