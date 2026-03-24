"""This script helps to parse the log of log.txt and detect suspicious count"""
alert_count=0  # for different key word cpunt
word_count=0
word_count_unauthorised=0
word_count_failed=0
with open('log.txt')  as f: # open file to read log.txt
   for i, j in enumerate(f, start=1):   # iterating through lines and assigning numbers
      j=j.strip() 
      dict_add={i:j}
      for values in dict_add.values():
         list_values=[values] # convert the values to list
         for lvalue in list_values: 
            splitvalue=lvalue.split() # to split the each word in a list
            if 'IP' in splitvalue: # check of for IP word index
               indexip=splitvalue.index('IP')
               indexip_add=indexip+1 # get ip_Add index
               words=['ERROR','UNAUTHORIZED','FAILED']
               if any(w in splitvalue for w in words):  # check for specific keywords are present in the list
                  alert_count+=1 # get the total alert count
               if 'ERROR' in splitvalue: # individual key word count
                     word_count+=1
               if 'UNAUTHORIZED'in splitvalue:
                  word_count_unauthorised+=1
               if 'FAILED' in splitvalue:
                  word_count_failed+=1                                                              # count the number of times they have occured
               print('ALERT!',splitvalue[indexip],splitvalue[indexip_add],'These ips are suscpicious')
                                          
print('Therefore, the total number of alerts are :', alert_count)   
print('ERROR has occured: ',word_count)
print('UNAUTHORIZED has occured',word_count_unauthorised)
print('FAILED has occured',word_count_failed)                

      
      
