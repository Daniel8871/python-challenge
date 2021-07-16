import os
import csv

# Specify the file to read
budget_data_path=os.path.join("Resources","budget_data.csv")

PL,rowcount,Chg,prev_PL=0,0,0,0

#List of Profit/Loss month to month, with date list matching index of those values
Chg_List=[]
Date_List=[]

# Open the file using reader mode. Specify the variable to hold the contents
with open(budget_data_path) as fileobj:

    #initialize the reader
    budget_reader=csv.reader(fileobj,delimiter=",")
    next(budget_reader)
        
    for row in budget_reader:
        #count the dates (as 'rowcount')
        rowcount+=1     

        # calculating Profit/Loss
        PL=PL+int(row[1])

        current_PL=int(row[1])

        # calculating monthly Profit/Loss, and storing value with associated date
        if rowcount>1:
            Chg=current_PL-prev_PL
            Chg_List.append(Chg)
            Date_List.append(row[0])
        prev_PL=current_PL
        
avg_Chg=sum(Chg_List)/len(Chg_List)

# largest Profit
Max_P=max(Chg_List)

# Finding index of largest Profit in list
Max_Px=Chg_List.index(Max_P)

# largest Loss
Max_L=min(Chg_List)

# Finding index of largest Loss in list 
Max_Lx=Chg_List.index(Max_L)

print("""Financial Analysis
-------------------------------""")
print(f'Total Months: {rowcount}')
print(f'Profit/Loss: ${PL:,.0f}'.replace('$-', '-$'))
print(f'Average Change: ${avg_Chg:,.0f}'.replace('$-', '-$'))
print(f'Greatest Profits: {Date_List[Max_Px]} (${Max_P:,.0f})')
print(f'Greatest Losses: {Date_List[Max_Lx]} (${Max_L:,.0f})')

# Specify the file to write
output_path=os.path.join("Resources","budget_data_summary.csv")

# Open the file using writer mode. Specify the variable to hold the contents
with open(output_path,'w',newline='') as writeobj:

    # Initialize the writer
    csvwriter=csv.writer(writeobj,delimiter=',')

    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['Total Months',rowcount])
    csvwriter.writerow(['Profit/Loss',f'${PL:,.0f}'.replace('$-', '-$')])
    csvwriter.writerow(['Average Change',f'${avg_Chg:,.0f}'.replace('$-', '-$')])
    csvwriter.writerow(['Greatest Profits',f'{Date_List[Max_Px]} (${Max_P:,.0f})'])
    csvwriter.writerow(['Greatest Losses',f'{Date_List[Max_Lx]} (${Max_L:,.0f})'.replace('$-', '-$')])