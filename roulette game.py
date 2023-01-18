import random
Max_Bet=100
Min_Bet=1
Max_Lines=3
ROWS=3
COLUMNS=3



symbol_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8
    
    }


symbol_values={
    "A":8,
    "B":6,
    "C":4,
    "D":2
    
    }

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for i in range(symbol_count):
            all_symbols.append(symbol)
    columns=[]
    for col in range(cols):
        column=[]
        curSlot=all_symbols.copy()
        for row in range(rows):
            value=random.choice(curSlot)
            curSlot.remove(value)
            column.append(value)
        columns.append(column)
    return columns
    
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,col in enumerate(columns):
            if i!=len(columns):
                print(col[row],end=" | ")
            else:
                print(col[row],end="|")
        print()
            
def check_winnings(columns,lines,bet,values):
    winning_line=[]
    winnings=0
    for line in range(lines):
        symbol=columns[0][line]
        for col in columns:
            symbol_to_check=col[line]
            if symbol!=symbol_to_check:
                break
        else:
            winnings+=values[symbol]*bet
            winning_line.append(line+1)
        
    return winnings,winning_line
    
    
    
    
def deposit():
    while True:
        depos=input("enter amount to deposit :$")
        if depos.isdigit():
            money=int(depos)
            if money>0:
                break
            else:
                print("Deposit must be greater than 0")
        else:
            print("enter valid digit")
        
    return money


def lines_to_bet():
    while True:
        lines=input("Enter number of lines (between 1 -"+str(Max_Lines)+") -")
        if lines.isdigit():
            lines=int(lines)
            if 0<lines<4:
                break
            else:
                print("Entered number of lines should be between 1 to "+str(Max_Lines)+" You entered "+str(lines)+ ".")
        
        else:
            print("Enter valid Digit, you entered "+lines)
    return lines
    
def bet():
    while True:
        bet=input("Enter bet (between "+str(Min_Bet)+"- "+str(Max_Bet)+") -")
        if bet.isdigit():
            bet=int(bet)
            if Min_Bet<=bet<=Max_Bet:
                break
            else:
                print("Entered bet should be between " +str(Min_Bet)+" to "+str(Max_Bet)+" You entered "+str(bet)+ ".")
        
        else:
            print("Enter valid Digit, you entered "+bet)
    return bet
    
    
def game(balance):
    lines_bet=lines_to_bet()
    
    while True:
        amount_bet=bet()
        total_bet=lines_bet*amount_bet
        if total_bet>balance:
            print(f"You don't have enough balance to bet. The current balance is ${balance} and the bet placed is ${total_bet}")
        else:
            break
    
    print(f"You are depositing ${balance} \nYou have placed on {lines_bet} lines \nYou are betting ${amount_bet} \nThus the total bet is ${total_bet}")
    
    slots=get_slot_machine_spin(ROWS, COLUMNS, symbol_count)
    print_slot_machine(slots)
    winnings,winning_line=check_winnings(slots, lines_bet, bet, symbol_values)
    print(f"you won ${winnings}")
    print("you won on line - ",*winning_line)
    return winnings-total_bet
    
def main():
    balance=deposit()
    while True:
        print("current balance is $",balance)
        spinning=input("Press Enter to spin \nPress q to quit")
        if spinning=="q":
            break
        balance+=game(balance)
        
    
    
main()