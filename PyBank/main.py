import os
import csv

budget_data_path=os.path.join("Resources","budget_data.csv")
PL,rowcount,Chg,prev_PL=0,0,0,0
Chg_List=[]
Date_List=[]

with open(budget_data_path) as fileobj:
    budget_reader=csv.reader(fileobj,delimiter=",")
    next(budget_reader)
        
    for row in budget_reader:
        rowcount+=1     

        PL=PL+int(row[1])

        current_PL=int(row[1])
        if rowcount>1:
            Chg=current_PL-prev_PL
            Chg_List.append(Chg)
            Date_List.append(row[0])
        prev_PL=current_PL
        
avg_Chg=sum(Chg_List)/len(Chg_List)

Max_P=max(Chg_List)
Max_Px=Chg_List.index(Max_P)

Max_L=min(Chg_List)
Max_Lx=Chg_List.index(Max_L)

print("""Financial Analysis
-------------------------------""")
print(f'Total Months: {rowcount}')
print(f'Profit/Loss: ${PL:,.0f}'.replace('$-', '-$'))
print(f'Average Change: ${avg_Chg:,.0f}'.replace('$-', '-$'))
print(f'Greatest Profits: {Date_List[Max_Px]} (${Max_P:,.0f})')
print(f'Greatest Losses: {Date_List[Max_Lx]} (${Max_L:,.0f})')

