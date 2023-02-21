# Make a file named "input.txt" and copy your input in that file.
# Now the code will run the input directly from that file.
f = open("input.txt","r")

#Reading the "input.txt" file line by line. It reads all lines as strings as makes a list of it.
l = f.readlines()

ans = 0 #stores the final answer. 

for x in l:
    cur = x.split('\n')[0].split(' ')   #processing each input line to find the characters. 
    if(cur[1]=='X'):    #2nd person loses.
        ans+=0  #score for losing
        if(cur[0]=='A'):    #1st takes out rock: 2nd takes out scissor in order to lose, hence 3 score added
            ans+=3     
        elif(cur[0]=='B'):  #1st takes out paper: 2nd takes out rock in order to lose, hence 1 score added
            ans+=1
        else:   #1st takes out scissor: 2nd takes out paper in order to lose, hence 2 score added
            ans+=2
    elif(cur[1]=='Y'):  #draw
        ans+=3  #score for draw
        if(cur[0]=='A'):    #1st takes out rock: 2nd takes out rock in order to draw, hence 1 score added
            ans+=1      
        elif(cur[0]=='B'):  #1st takes out paper: 2nd takes out rock in order to paper, hence 2 score added
            ans+=2
        else:   #1st takes out scissor: 2nd takes out scissor in order to draw, hence 3 score added
            ans+=3
    else:   #2nd person wins
        ans+=6 #score for win
        if(cur[0]=='A'):    #1st takes out rock: 2nd takes out paper in order to win, hence 2 score added
            ans+=2  
        elif(cur[0]=='B'):  #1st takes out paper: 2nd takes out scissor in order to win, hence 3 score added
            ans+=3
        else:   #1st takes out scissor: 2nd takes out rock in order to win, hence 1 score added
            ans+=1

print(ans)