# Day_2 Take an input character from user and check wheather it is an alphabet or not

  # fisrtway
# c=input("Enter a Character :")
# if(c.isdigit()):   #c.isalpha()
#     print("Not an alphabet")
# else:
#     print('Alphabet')

    #another way
c=input("Enter a Character :")
if("A"<=c<='Z'or 'a'<=c<='z'):
    print('Alphabet')
else:
    print("not an alphabet")
#iam running lte