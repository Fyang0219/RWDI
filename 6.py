# Make a file named "input.txt" and copy your input in that file.
# Now the code will run the input directly from that file.
f = open("input.txt","r")

#Reading the "input.txt" file. It reads the entire file as a single string. 
l = f.read()

ans = -1    #stores the final required index. 
for i in range(3, len(l)):  #traversing the given string from left to right to find the index of first-marker
    x = set()   #to store the charcaters. if the size is 4, then we know that the current index is start-of-packet-marker as the 4 characters ending at this index are distinct. 
    for j in range(4):  
        x.add(l[i-j])   #adding all 4 the characters taken from a 4 sized window ending at current index. 
    if(len(x)==4):  #this states that all 4 are free.
        ans = i+1   #because we need 1-based index as the result
        break #since we have found the index requred.

print(ans)