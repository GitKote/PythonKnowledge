Existing_loan=(88657,309974)
New_loan=int(input(" Enter HOW MUCH to take from ICICI\n"))

final_settlement=0

for loan in Existing_loan:
 Tax=loan*(2.0/100)
 GST=Tax*(18.0/100)
 print (Tax)
 print (GST)
 final_settlement=loan+Tax+GST+final_settlement
 print (final_settlement)

old_loan_final_settlement=final_settlement

if (New_loan >= 1000000):
 Take_home_new_loan=New_loan-4999
else:
 Take_home_new_loan=New_loan-New_loan*(0.99/100)

before_hdfc=(Take_home_new_loan)-(old_loan_final_settlement)
after_hdfc=before_hdfc-322478

print ("Old loan final is",old_loan_final_settlement)
print ("Take_home is", before_hdfc)
print ("After HDFC is", after_hdfc)
