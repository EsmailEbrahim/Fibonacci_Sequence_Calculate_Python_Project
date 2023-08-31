import os

def FibonacciSequence():
    os.system("cls")
    Arr = []
    Num = int(input("Enter how many numbers: "))
    if (Num > 0):
        if (Num == 1):
            Arr = [0]
        
        elif (Num == 2):
            Arr = [0, 1]

        else:
            Arr = [0, 1]
            for i in range(2, Num):
                Temp = Arr[i-2] + Arr[i-1]
                Arr.append(Temp)
        Choice = input(f"{Arr}\n\nTry again?\t1- Yes\t0- No ")
        if (Choice == "1"):
            FibonacciSequence()
        else:
            exit()

    else:
        Choice = input("Wrong Entry!\n\nTry again?\t1- Yes\t0- No ")
        if (Choice == "1"):
            FibonacciSequence()
        else:
            exit()


FibonacciSequence()
