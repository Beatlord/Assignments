user_input=input('enter name in camalCase:')
def convert_to_snake(user_input):
    word = " "
    snake = " "
    
    for n in range(len(user_input)):
        
        if user_input[n].isupper():
            snake += "_" +user_input[n].lower()
            
        else:
            snake += user_input[n]
        
    print(f'The snake case of your camal case is {snake}')
   

convert_to_snake(user_input)