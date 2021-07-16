import os
import csv

# Specify the file to read
budget_data_path=os.path.join("Resources","budget_data.csv")

#List of Profit/Loss month to month, with date list matching index of those values
Date_List=[]
PL_List=[]
Change_List=[None,None]

# Open the file using reader mode. Specify the variable to hold the contents
with open(budget_data_path) as fileobj:

    #initialize the reader
    budget_reader=csv.reader(fileobj,delimiter=",")
        
    for row in budget_reader:
        Date_List.append(row[0])
        PL_List.append(row[1])

# Set first 'Profit/Losses' value to Row 2
FirstPL=PL_List[1]

# Set PL variable for use in the for loop
PL=int(FirstPL)
for x in range(2,len(PL_List)):
    
    SecondPL=PL_List[x]
    Change=int(SecondPL)-int(FirstPL)

    # Build Change_List
    Change_List.append(Change)

    # Calculate overall PL
    PL=PL+int(SecondPL)

    # Reset variable
    FirstPL=SecondPL

# Set Total variable for use in the for loop
Total=0
for y in range(2,len(Change_List)):
    Total=Total+int(Change_List[y])

# Calculate average PnL
Average=Total/int(len(Change_List)-2)

# Number of months
Months=len(Date_List)-1

# Overall Profit/Loss
PL

# PROFITS
# largest Profit
Max_P=max([i for i in Change_List if i is not None])
# Finding index of largest Profit in list
Max_Px=Change_List.index(Max_P)

# LOSSES
# largest Loss
Max_L=min([i for i in Change_List if i is not None])
# Finding index of largest Loss in list 
Max_Lx=Change_List.index(Max_L)

print("""Financial Analysis
-------------------------------""")
print(f'Total Months: {Months}')
print(f'Profit/Loss: ${PL:,.0f}'.replace('$-', '-$'))
print(f'Average Change: ${Average:,.0f}'.replace('$-', '-$'))
print(f'Greatest Profits: {Date_List[Max_Px]} (${Max_P:,.0f})')
print(f'Greatest Losses: {Date_List[Max_Lx]} (${Max_L:,.0f})')

# Specify the file to write
output_path=os.path.join("Resources","budget_data_summary.csv")

# Open the file using writer mode. Specify the variable to hold the contents
with open(output_path,'w',newline='') as writeobj:

    # Initialize the writer
    csvwriter=csv.writer(writeobj,delimiter=',')

    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['Total Months',Months])
    csvwriter.writerow(['Profit/Loss',f'${PL:,.0f}'.replace('$-', '-$')])
    csvwriter.writerow(['Average Change',f'${Average:,.0f}'.replace('$-', '-$')])
    csvwriter.writerow(['Greatest Profits',f'${Max_P:,.0f}',f'{Date_List[Max_Px]}'])
    csvwriter.writerow(['Greatest Losses',f'${Max_L:,.0f}'.replace('$-', '-$'),f'{Date_List[Max_Lx]}'])