import string
import random
if __name__ == "__main__":
    s1=string.ascii_lowercase
    s2=string.ascii_uppercase
    s3=string.digits
    s4=string.punctuation
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    for i in range(101):
        n=8
        random.shuffle(s)
        print('---------------------------------------------------------------------------')
        print(''.join(s[0:n]))
        p=input('type')
        if p=='q':
            exit()