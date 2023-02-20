# Make a file named "input.txt" and copy your input in that file.
# Now the code will run the input directly from that file.
f = open("input.txt","r")

#Reading the "input.txt" file line by line. It reads all lines as strings as makes a list of it.
l = f.readlines()


#preprocessing the input data

blank = -1  # this will store the index of the empty line in the input. It will be used to divide input in 2 parts. given stacks and the commands
for i in range(len(l)):
    if(l[i]=='\n'): #empty line is found
        blank = i
        break

data = []   #it will be a 2-D array where each array is a character array representing a stack. so in test case there are 3 arrays. so it will have 3 arrays. 
for i in range (len(l[blank-1])):
    if(l[blank-1][i]==' ' or l[blank-1][i]=='\n'):     #empty spaces between stacks)columns)
        continue
    else:   #when a new stack is found
        cur = []
        for j in range(blank-2,-1,-1):  #reading each character for a stack from bottom to up one by one.
            if(i>=len(l[j]) or l[j][i]==' '):   
                continue
            cur.append(l[j][i])
        data.append(cur)
#preprocessing done


# executing each command given one by one
for i in range(blank+1,len(l),1):
    cur = l[i].split('\n')[0].split(' ')
    amount = int(cur[1])    #the number of elements you need to shift
    st = int(cur[3])    #the starting column
    ed = int(cur[5])    #the ending column
    st-=1
    ed-=1
    for j in range(amount): #shifting the number of required elements in this particular command.
        ele = data[st].pop()
        data[ed].append(ele)

ans = ""    #will store final answer

for x in data:
    ans+= x[-1] #adding top of each column to the answer.
print(ans)
