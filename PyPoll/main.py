import os
import csv

election_data_path=os.path.join("Resources","election_data.csv")

#Open election data file object.
with open(election_data_path) as fileobj:
    election_reader=csv.reader(fileobj,delimiter=",")
    next(election_reader)

    # Create lists and set variables for collecting the names of the candidates & vote count
    # in the first pass through data file.
    rowcount,cand_count=0,0
    candidates=list()
    current_vote=str()
    bool= False

    for row in election_reader:
        rowcount+=1 #votecount
        current_vote=row[2] 

        # Using For Loop, If statement and Boolean to build the list of unique names in data set.
        for x in range(0,len(candidates)):
            if candidates[x] == current_vote:
                bool=True
                break
            else: bool=False
        
        # This is the tool for collecting all the candidates
        # If there were only two candidates (for example) it
        # would be possible to avoid this section by just counting the votes 
        # based on the pre-known candidate names
        if bool == False:
            candidates.append(current_vote)
        else: bool=False

    print("Election Results")
    print("--------------------------")        
    print(f'Total Votes: {rowcount}')
    print("--------------------------")

    # Restart from top. Second pass on data set now that list of candidates is collected.
    # (to count the vote for each of the now-identified candidates)
    fileobj.seek(0)
   
   # tally list, index of the vote tally will match the index of the 
   # associated candidate in the candidate list
    tally=list()
    
    # p_list - used later for calculating percentage
    p_list=list()

    # Creating the vote tally list for each candidate 
    # (starting with 0 votes for each)
    for y in range(0,len(candidates)):
        tally.append(0)

    # Cycling through list now to collect votes
    for row in election_reader:
        current_vote=row[2]
        
        # For each row, cycling through the candidates and 
        # Attaching the vote to the associated candidate.
        for person in candidates:
            if person == current_vote:

                # Once the candidate is identified, attach a vote to the
                # tally of that candidates votes (via indexed list position)
                tally_x=candidates.index(person)
                tally[int(tally_x)]=tally[int(tally_x)]+1
                break

# From the vote tally, calculating it's percentage of the total (and saving to list).
for z in range(0,len(candidates)):
    p=tally[int(z)]/rowcount
    p_list.append(p)
    print(f'{candidates[int(z)]}: {p:.2%} ({tally[int(z)]})')

# Printing results to terminal.
print("--------------------------")
winner=candidates[tally.index(int(max(tally)))]
print(f'Winner: {winner}')
print("--------------------------")

# Saving results to .csv file.
output_path=os.path.join('analysis','PyPoll_summary.csv')
with open(output_path,'w',newline='') as fileobj_w:

    election_writer=csv.writer(fileobj_w,delimiter=',')
    election_writer.writerow(["Election Results"])
    election_writer.writerow(["Total Votes:",rowcount])
    for zz in range(0,len(candidates)):
        election_writer.writerow(["Candidate:",candidates[int(zz)],f'{p_list[int(zz)]:.2%}',tally[int(zz)]])
    election_writer.writerow(["Winner:",winner])
