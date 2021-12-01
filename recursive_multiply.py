#output:- {1: 1, 2: 4, 3: 27, 4: 256, 5: 3125, 6: 4665}

def mul(end_number):
    dict={}
    i=1
    while i<=end_number:
        dict[i]=i**i
        i=i+1
    return dict 
num=int(input('Enter number'))
print(mul(num))