function FibonacciSequence()
{
    var Arr = []
    var Num = parseInt(prompt("Enter how many numbers: "));
    if (Num > 0)
    {
        if (Num == 1)
        {
            Arr = [0];
        }
        else if (Num == 2)
        {
            Arr = [0, 1];
        }
        else
        {
            Arr = [0, 1];
            for(var i = 2; i < Num; i++)
                {
                    var temp = Arr[i-2] + Arr[i-1];
                    Arr.push(temp);
                }
        }
        if (confirm(Arr + "\nTry again?"))
        {
            FibonacciSequence();
        }
    }
    else
    {
        if (confirm("Wrong Entry!\nTry again?"))
        {
            FibonacciSequence();
        }
    }
}


FibonacciSequence();