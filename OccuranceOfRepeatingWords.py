"""
Enter the number of words
"""

#Reading number
numb=0
while ((numb < 1) or (numb >= 10^5)): 
 print ("Please enter numb between 1 and 10^5")
 numb=int(input("How many words that you want to enter? \n"))


#Feed those many words
a=[]
while(numb > 0):
 word=input('')
 #print (word, end='\n')
 a.append(word)
 numb-=1
print (a)

#Finding repeated words
b={}
control=[]
print (len(a))
for i in a:
 cnt=a.count(i)
 if i not in b:
  b[i]=cnt
  print (cnt, end=' ')
 else:
  continue 