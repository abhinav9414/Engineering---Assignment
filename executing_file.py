# commands to demonstrate CRD SYSTEM how to access and perform operations on a main file

#"key doesnot exist" if key_name was mis-spelt or deleted earlier
#"File memory limit reached" if file memory exceeds 1GB
import threading
import main as a #importing the main file(as a library)
from threading import*
import time
from time import sleep


#create a key , no time-to-live property
a.create("froast",80)



a.create("adam",[100,90],3600)
# create a key with key_name,value given and with time-to-live property value given(number of seconds)

a.create("zeus",[100,213,90],3600)

a.create("eve",[100,75,90],3600)
print(a.read("froast"))
#here we had returned the value of the respective key in Jasonobject format 'key_name:value'

print(a.read("adam"))
#use delete operation and recreate it
#"invalidkey" if key_length is greater than 32 or key_name contains any numeric,special characters etc.,


#it deletes the respective key and its value from the database(memory is also freed)
a.delete("froast")




#a.print1()



#we can access these using multiple threads like
t1=Thread(target=(a.create),args=("m",213,32)) #as per the operation
t1.start()
time.sleep(2)
t3=Thread(target=(a.read),args=("k")) #as per the operation
t3.start()
time.sleep(4)


t1.join()
t3.join()
a.delete("adam")





