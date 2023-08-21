def calculate(a,b):
    print('Addition of {} and {} is = {} '.format(a,b,(a+b)))
    print('Substraction of {} and {} is = {} '.format(a,b,(a-b)))
    print('Multipliction of {} and {} is = {} '.format(a,b,(a*b)))
    print('Division of {} and {} is = {} '.format(a,b,(a//b)))
    print('Modulo of {} and {} is = {} '.format(a,b,(a%b)))
    
    
    
    
    
if __name__ == '__main__':
    a=int(input("Enter the first number: "))
    b=int(input("Enter Second Number: "))
    calculate(a,b)