def soda_price():#defining the function
    bot_num = int(input('Enter the number of bottles you want: '))#prompting the number of bottles
    price = int(input('Enter your coin in denomination 25, 10, 5: '))#prompting for the price
    if price == 10 or price == 25 or price == 5:
        r_price = bot_num * 50 #required price
        ret = 0 #change
        bt = bot_num + 1

        for bot in range(1, bt): #checking if the price is equal to the required price
            if price > r_price:
                ret = price - r_price #calculating the change
                print(f'Thank you for your payment of {bot_num} bottles, enjoy your drink! Your change is: {ret} coins ') #thanking the customer and informing them the change
            elif price == r_price:
                print(f'Thank you for your payment of {bot_num} bottles, enjoy your drink!') #thanking the customer
                break

            else:
                while price < r_price:
                    p = int(input(f'You have insufficient coins for the number of bottles you want, Please add {r_price - price} more coins:')) #prompting the user to meet the required price
                    if p == 10 or p == 25 or p == 5:
                        price += p
                    else:
                        print('Invalid denomination, please try again!') #an invalid input

    else:
        print('Invalid denomination, please try again!')

soda_price()#calling the function
