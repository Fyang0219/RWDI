# Make a file named "input.txt" and copy your input in that file.
# Now the code will run the input directly from that file.
f = open("input.txt","r")

#Reading the "input.txt" file line by line. It reads all lines as strings as makes a list of it.
l = f.readlines()

ans = 0 #stores the final answer

for x in l:
    left = {}   #dictionary to store the characters of the left part of the string
    n = len(x)  #size of the the string

    for i in range(n//2):
        left[x[i]]=1    #making entries in dictionary for all the characters in the left of the string.
    for i in range(n//2,n): #traversing the right part of string now.
        if(left.get(x[i],-1)!=-1):  #when we find a character in the right part which is already in the dictionary for the left part also. 
            if(x[i]>='a' and x[i]<='z'):       #adding the priority of the character which is in both parts
                ans+=(ord(x[i])-ord('a')+1)
            else:
                ans+=(ord(x[i])-ord('A')+27)
            break   #because it is given that only one character is present in both left and right parts and we have found one. 
print(ans)

