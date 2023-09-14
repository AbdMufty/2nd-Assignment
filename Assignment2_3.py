num = input("Enter the seconds: ")
num = int(num)
hour = num/3600
#print(int(hour))
minute = ((num%3600)/60)
#print(int(minute))
#second = (num-((hour*3600)+(minute*60)))~ why this is not working? 
#second= ((num%3600)) - (minute*60)~ why this is not working?
second = num%60
second= int(second)
#print(second)
print(num,"seconds = ",int(hour),"hours",int(minute),"minutes",second,"seconds")