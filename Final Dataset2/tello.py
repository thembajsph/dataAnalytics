def homeLoanApplication():
    Granted = True
    Rejected = True
    gross_salary = float(input())
    Purchase_Price = float(input())
    credit_score = float(input())
    canAfford = 0.3 * gross_salary
    deposit = 0
    bond_amount = Purchase_Price - deposit
    monthy_instalment = bond_amount * 0.0785
    has_good_salary = canAfford > monthy_instalment


#  1. The instalment of a home loan should be no more than 30% of a customer’s gross salary.
#     2. The home loan percentage granted is determined by the credit score as below:

#     • 800 and above = 110% loan.
    if has_good_salary and credit_score >= 800:
        
       
       
       #   Percentage_Home_Loan_granted = 110%
        print(F"Loan application status : ${Granted}")
        print(F"Percentage Home Loan granted : 110%")
        deposit = Purchase_Price * 0
        print(F" How much deposit is required : ${deposit}")
        print(F"Down payment : ${monthy_instalment}")
#
   
    


   #     • 750-799 = 100% loan.
    elif has_good_salary and credit_score >= 750 and credit_score <= 799:
       
        # Percentage_Home_Loan_granted = 100%
         print(F"Loan application status : ${Granted}")
         print(F"Percentage Home Loan granted : 100%")
         deposit = Purchase_Price * 0
         print(F" How much deposit is required : ${deposit}")
         print(F"Down payment : ${monthy_instalment}")
       
   


#     • 700-749 = 95% loan.
    elif has_good_salary and credit_score >= 700 and credit_score <= 749:
       
    # Percentage_Home_Loan_granted = 95%
        print(F"Loan application status : ${Granted}")
        print(F"Percentage Home Loan granted : 95%")
        deposit =Purchase_Price * 0.05
        print(F" How much deposit is required : ${deposit}")
        print(F"Down payment : ${monthy_instalment}")


#     • 650-699 = 90% loan.
    elif has_good_salary and credit_score >= 650 and credit_score <= 699:
    # Percentage_Home_Loan_granted = 90%
        print(F"Loan application status : ${Granted}")
        # print(F"Down payment : ${downpayment}")
        print(F"Percentage Home Loan granted : 90%")
        deposit =Purchase_Price * 0.1
        print(F" How much deposit is required : ${deposit}")
        print(F"Down payment : ${monthy_instalment}")


#     • 5.  600-649 = 85% loan.
    elif has_good_salary and credit_score >= 600 and credit_score <= 649:
       
       

    # Percentage_Home_Loan_granted = 85%
        print(F"Loan application status : ${Granted}")
        # print(F"Down payment : ${downpayment}")
        print(F"Percentage Home Loan granted : 110%")
        deposit = Purchase_Price * 0.15
        print(F" How much deposit is required : ${deposit}")
        print(F"Down payment : ${monthy_instalment}")


#     • 6.  550-599 = 80% loan.
    elif has_good_salary and credit_score >= 550 and credit_score <= 599:
        
    # Percentage_Home_Loan_granted = 80%
        print(F"Loan application status : ${Granted}")
        # print(F"Down payment : ${downpayment}")
        print(F"Percentage Home Loan granted : 80%")
        deposit = Purchase_Price * 0.2
        print(F" How much deposit is required : ${deposit}")
        print(F"Down payment : ${monthy_instalment}")


#     • 7. 549 and below = rejected.
    else:
        print(F"Loan application status : ${Rejected}")
        
        
        
        
print(homeLoanApplication())        
        
        

 
