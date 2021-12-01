# Ek function likho jo ki ek argument le jo number ho or dictionary return karega jisme keys 1 se lekar argument ke number tak hogi aur values unke squares honge.jaisa ki niche dikhaya gaya hai.

# Input :- 20

def make_square(end_number):
    dict = {}
    i=1
    while i<=end_number:
        dict[i]=i*i
        i=i+1
    return dict
print(make_square(20))