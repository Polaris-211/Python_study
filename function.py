print("Hello GaGa, welcome to DaoDun bank, please chose the operation：")
print("balance inquary, input [1]")
print("deposit, input [2]")
print("withdrawal, input [3]")
print("quit, input [4]")



def BalanceInquary():
    global inquary
    inquary = 50000
    print(f"Your inquary is {inquary}")

def deposit():
    deposit = 50000
    inquary += deposit
    print(f"Your have deposit{deposit}, now you have {inquary}")

def withdrawal():
    withdrawal = 5000
    inquary -= withdrawal
    print(f"Your have withdrawal{withdrawal}, now you have {inquary}")

def quit():
    exit()

num=int(input())
if num == 1:
    BalanceInquary()
elif num == 2:
    deposit()
elif num == 3:
    withdrawal()
elif num == 4:
    quit()


