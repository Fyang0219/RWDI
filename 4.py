# Make a file named "input.txt" and copy your input in that file.
# Now the code will run the input directly from that file.

f = open("input.txt","r")

#Reading the "input.txt" file line by line. It reads all lines as strings as makes a list of it.
l = f.readlines()

ans = 0 #stores the final answer

for x in l:
    cur = x.split('\n')[0]
    intervals = cur.split(',')  #for every test case, intervals is a list which contains both intervals as a list of strings. 
    p = []  #will store the intervals as list or integer arrays. [[1,2],[4,5]] for example
    for y in intervals: #processing each interval to convert from string to int and append in list p.
        now = y.split('-')
        temp = []
        temp.append(int(now[0]))
        temp.append(int(now[1]))
        p.append(temp)
    if( (p[0][0]>=p[1][0] and p[0][1]<=p[1][1]) or (p[1][0]>=p[0][0] and p[1][1]<=p[0][1])):    #cehcking if one interval contains the other.
        ans+=1
    

print(ans)