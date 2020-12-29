
import time
import sys
import json
import os
dictionary={}
#'dictionary' is the dictionary in which we store data

#for create operation 
#use syntax "create(key_name,value,timeout_value)" timeout is optional you can continue by passing two arguments without timeout

def create(key,value,timeout=0):
    if key in dictionary:
        print("error: this key already exists") #error message1
    else:
        if(key.isalpha()):
            if len(dictionary)<(1024*1020*1024) and sys.getsizeof(value)<=(16*1024*1024): #constraints for file size less than 1GB and Jasonobject value less than 16KB
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: #constraints for input key_name capped at 32chars
                    dictionary[key]=l
                print("file data successfully created  key -",key,value)
            else:
                print("error: Memory limit exceeded!! ")#error message2
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")#error message3
    a_file = open("data.json", "w")
    json.dump(dictionary, a_file)
    a_file.close()



#for delete operation
#use syntax "delete(key_name)"

def delete(key):
    if key not in dictionary:
        print("error: given key does not exist in database. Please enter a valid key") #error message4
    else:
        b=dictionary[key]
        if b[1]==0:
            del dictionary[key]
            print("key is successfully deleted")
        else:
            if time.time()<b[1]: #comparing the current time with expiry time
                del dictionary[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") #error message5

    os.remove("data.json")
    a_file = open("data.json", "w")
    json.dump(dictionary, a_file)
    a_file.close()

# for read operation
# use syntax "read(key_name)"

def read(key):
    a_file = open("data.json", "r")
    output = a_file.read()
    #print("output is",output)
    if key not in dictionary:
        print("error: given key does not exist in database. Please enter a valid key")  # error message4
    else:
        b = dictionary[key]
        if b[1] != 0:
            if time.time() < b[1]:  # comparing the present time with expiry time
                stri = str(key) + ":" + str(b[0])  # to return the value in the format of JasonObject i.e.,"key_name:value"
                return stri
            else:
                print("error: time-to-live of", key, "has expired")  # error message5
        else:
            stri = str(key) + ":" + str(b[0])
            return stri







