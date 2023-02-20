# Make a file named "input.txt" and copy your input in that file.
# Now the code will run the input directly from that file.
f = open("input.txt","r")

#Reading the "input.txt" file line by line. It reads all lines as strings as makes a list of it.
l = f.readlines()

ans = 0 #stores the final answer
cur = 0 #at every instant, it will store the calories of a particular elf that we are working on at that moment. 
data = [] #this will store the calories of each elf.
for x in l: 
    if(x=='\n'):    #This is the case where there is an empty line and so we know that the items for the current elf have finishid.
        data.append(cur) 
        cur = 0     #set calories to 0 for new elf.
        continue
    val = int(x.split('\n')[0]) #just processing the string read as input to convery it into integer value.
    cur+=val    #adding to calories of current elf.
data.append(cur)    #for the last elf.
data.sort(reverse=True) #sorting in descending order to find the elves with largest calories.
ans = data[0]+data[1]+data[2]  
print(ans)