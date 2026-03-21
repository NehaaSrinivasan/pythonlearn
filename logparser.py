"""This script helps to parse the log of log.txt and detect suspicious count"""
alert_count=0
with open('log.txt')  as f: # open file to read log.txt
   for i, j in enumerate(f, start=1):   # iterating through lines and assigning numbers
      j=j.strip()                       # remove spacing
      if "ERROR" in j or "UNAUTHORIZED" in j or "FAILED" in j:  # check for specific keywords
         alert_count+=1                                               # count the number of times they have occured
         print('ALERT!', i, j)                                  # alert message
print(' total number of alerts is :', alert_count)                    # total count of alerts

      
      
