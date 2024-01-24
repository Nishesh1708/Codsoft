import random 
required_length=int(input("Enter the required length of password ="))
digits=['0','1','2','3','4','5','6','7','8','9']
uppercase_alphabets=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lowercase_alphabets=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
special_characters=['!','@','#','$','%','^','&','_','?','/','~','.','-']
total_characters=uppercase_alphabets + lowercase_alphabets + special_characters
rand_digits=random.choice(digits)
rand_upper=random.choice(uppercase_alphabets)
rand_lower=random.choice(lowercase_alphabets)
rand_characters=random.choice(special_characters)
x=rand_digits + rand_lower + rand_upper + rand_characters
for i in range(required_length-4):
    x=x+random.choice(total_characters)
    password=list(x)
    random.shuffle(password)
print("Your password is ",x)