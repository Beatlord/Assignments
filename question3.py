def vow_omit():#defining the function to omit vowels
    user_str = input('Enter your string: ')#prompting for user input
    f_str =" "
    for str in user_str:#checking for vowels
        if str =='a' or str =='e' or str =='i' or str =='o' or str =='u' or str =='A' or str =='E' or str =='I' or str == 'O' or str =='U':
            continue
        else:
            f_str = f_str + str #final string initialisation

    print('Your string in short form is:'+f_str)#printing the output to the user

vow_omit()