import os
import csv


election_data_path=os.path.join("Resources","election_data.csv")

with open(election_data_path) as fileobj:
    election_reader=csv.reader(fileobj,delimiter=",")
    next(election_reader)

    rowcount,cand_count=0,0
    candidates=list()
    current_vote=str()
    bool= False

    for row in election_reader:
        rowcount+=1 
        current_vote=row[2] 

        for x in range(0,len(candidates)):
            if candidates[x] == current_vote:
                bool=True
                break
            else: bool=False
        
        if bool == False:
            candidates.append(current_vote)
        else: bool=False
        
    print(rowcount)
    print(candidates)

    fileobj.seek(0)
   
    tally=[]
    for y in range(0,len(candidates)):
        tally.append(0)

    for row in election_reader:
        current_vote=row[2]
        
        for person in candidates:
            if person == current_vote:
                tally_x=candidates.index(person)
                tally[int(tally_x)]=tally[int(tally_x)]+1
                break
            
print(candidates)
print(tally)

#list, then while loop, then for loop, ea loop, 
#use for letter in word idea, if index0 matches, the 
#turn off while loop (maybe swap whileand for loop?)
#possible to 