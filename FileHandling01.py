'''
Task 01
Read the file named server_log.txt.
Find every line that contains the word "ERROR".
Write only those lines into a new file called errors_only.txt.
Bonus: At the end, print how many errors were found
'''
#Taif AlQarni

#have two file read from server_log and create/write to errors.txt file
with open('server_log.txt', 'r') as s, open('errors.txt', 'w') as e:
    Errorlines = 0 #defining the counter for lines found
    for line in s:
        #for-loop here to read every line in the file and search for line start with word'ERROR'
        if line.startswith('ERROR'):
            e.write(line)
            Errorlines += 1 #to count all lines read using the loop


print('Errors Found: {}'.format(Errorlines))








