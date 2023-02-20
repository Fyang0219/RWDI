# Make a file named "input.txt" and copy your input in that file.
# Now the code will run the input directly from that file.
f = open("input.txt","r")

#Reading the "input.txt" file line by line. It reads all lines as strings as makes a list of it.
l = f.readlines()

ans = 0 #stores the final answer. 

for x in l:
    cur = x.split('\n')[0].split(' ')   #processing each input line to find the characters. 
    if(cur[1]=='X'):    #2nd person whose score we are calculating takes out rock
        ans+=1  #score for taking out rock given to 2nd person
        if(cur[0]=='A'):    #1st also takes out rock
            ans+=3      
        elif(cur[0]=='C'):  #1st takes out scissor
            ans+=6
    elif(cur[1]=='Y'):  #2nd person whose score we are calculating takes out paper
        ans+=2  #score for taking out paper given to 2nd person
        if(cur[0]=='B'):    #1st takes out paper
            ans+=3      
        elif(cur[0]=='A'):  #1st takes out rock
            ans+=6
    else:   #2nd person whose score we are calculating takes out scissor
        ans+=3  #score for taking out scissor given to 2nd person
        if(cur[0]=='C'):    #1st takes out scissor
            ans+=3  
        elif(cur[0]=='B'):  #1st takes out paper
            ans+=6

print(ans)