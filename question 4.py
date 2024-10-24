def func(numb):
    num =1
    print(f'The perfect numbers below {numb} are:')
    for num in range(1, numb):
        sum =0
        for n in range(1, num):
            if num %n ==0:
                sum += n
        if sum ==num:
            print(f"{num} \n")
            
nun = 1000000
func(nun)