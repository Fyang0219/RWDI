# Make a file named "input.txt" and copy your input in that file.
# Now the code will run the input directly from that file.
f = open("input.txt","r")

#Reading the "input.txt" file line by line. It reads all lines as strings as makes a list of it.
l = f.readlines()

ans = 0 #stores the final answer

for i in range(0,len(l),3):
    count = {}   #dictionary to store the occurence of characters for each group of three. 1-> only in 1 out of 3. 2-> occurs in 2 out of 3. 3-> occurs in all 3.
    
    for j in range(3):
        now = {}    #dictionary to keep track of characters that occur in a particular string
        for x in l[i+j]:    #finding all characters that exist in particular string
            if(now.get(x,-1)==-1):
                now[x]=1
        for x in now.keys():    # adding the occurenct to the main dictionary for this group
            if(count.get(x,-1)==-1):
                count[x]=1
            else:
                count[x]+=1
    cur = ""    #will store the badge type for this group
    for x in count.items():
        if(x[1]==3 and x[0]!='\n'): #if number of occurence is 3->this is the badge. 
            if(x[0]>='a' and x[0]<='z'):       #adding the priority of the character which is the badge.
                ans+=(ord(x[0])-ord('a')+1)
            else:
                ans+=(ord(x[0])-ord('A')+27)
            break   #because it is given that only one character is the badge for the entire group
print(ans)

