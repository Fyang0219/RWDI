# Make a file named "input.txt" and copy your input in that file.
# Now the code will run the input directly from that file.
f = open("input.txt","r")

#Reading the "input.txt" file line by line. It reads all lines as strings as makes a list of it.
l = f.readlines()

ans = 0 #stores the final answer
cur = 0 #at every instant, it will store the calories of a particular elf that we are working on at that moment. 
for x in l: 
    if(x=='\n'):    #This is the case where there is an empty line and so we know that the items for the current elf have finishid.
        ans = max(ans,cur)  
        cur = 0     #set calories to 0 for new elf.
        continue
    val = int(x.split('\n')[0]) #just processing the string read as input to convery it into integer value.
    cur+=val    #adding to calories of current elf.

ans = max(ans,cur)  #for the last elf, because there will be no empty line after his entry and so this case will have not been tackled in the loop. 
print(ans)