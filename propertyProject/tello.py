def homeLoanApplication():
    # granted = True
    # rejected = True
    print("Hi there I'm Andile, your cash on cash digital assistance :D...")
    # property_first_expense = float(input("Enter your property first expense: ")) # gross income * 40%
    purchase_price = float(input("What is the purchase price of the property: "))
    annual_gross_propertyIncome = float(input("Now enter the total annual gross rent income : "))
    
    print("Thanks for using the cash on cash propery app.")
    
    
    deposit_downpament = float(input("What have you put down as downpayment for the property: ")) # ratio 1/3
    current_interestRate = float(input("What is the current interest rate: "))
    

    property_first_expense = float(0.4 * annual_gross_propertyIncome)
    
    
   
    bond_amount = purchase_price - deposit_downpament
    
    # max_instalments at 7.5% interest rate for 20 years mortgage
    # answer = float((bond_amount * (1 / 160)))
    # monthly_instalment_debt = (float(answer / 0.77582582) * 12)
    
     # max_instalments at 7.5% interest rate for 20 years mortgage
    # top_layer = float((current_interestRate / 100) /12)
    top_layer = float(((current_interestRate) * 0.0008333333))
    
    answer = float(bond_amount * top_layer)
    monthly_instalment_debt = float(answer / (0.7866915794 ))
    print(monthly_instalment_debt)
    
    # top_layer = float((current_interestRate / 100) /12)

    # answer = float((bond_amount * (top_layer)
    # monthly_instalment_debt = float(answer / (1 - (1 + (top_layer) ** -240))
    
    
    # monthly_instalment_debt =  

    
    cash_On_Cash = (annual_gross_propertyIncome - property_first_expense - monthly_instalment_debt) 
    cash_On_Cash_percentage = cash_On_Cash /  deposit_downpament * 100
    
    
    

    
    print("Property proccesing status : granted")
     
    print(F"The Cash on cash Amount: R{cash_On_Cash}")
    print(F"Percentage of Cash on cash return annually : {cash_On_Cash_percentage}%")
    
    print("Press Any Key to continue... ")
    
    
    
    
    property_rehabUs = float(input("Now enter your property rehab per unit in $ : ")) # eg 5000 dollar 
    # is equal to R75000 per unit * 25% divide by 12
    number_of_units = float(input("Enter the number of units: "))
    exchange_rate = float(input("Now enter the USA/RSA exchange rate "))
    original_rentUnit = float(input("What is the original rent per unit: "))
    
    
    # the rehab app
   
    total_RehabRand = number_of_units * property_rehabUs * exchange_rate
    property_priceRehabUnit = property_rehabUs * 0.25 / 12 * exchange_rate # exchange rate , usa and RSA
    rent_increased = original_rentUnit + property_priceRehabUnit
    property_Noi = annual_gross_propertyIncome - property_first_expense 
    property_Cape_Rate = property_Noi / purchase_price
    valueAdded = property_priceRehabUnit * 12 * number_of_units * property_Cape_Rate
    newValueProperty = purchase_price + valueAdded
    
    all_property_expense = property_first_expense + property_rehabUs + deposit_downpament
    all_propCapRate = rent_increased * number_of_units - all_property_expense / purchase_price
    
    print("Property proccesing status : granted")
     
    print(F"The total spend in Rands : R{total_RehabRand}")
    print(F"The rehab will get an increase of : R{property_priceRehabUnit}")
    print(F"The new rent will now be...  : R{rent_increased}")
    print(F"the rent has increse by 25% + : {cash_On_Cash_percentage}% ")
    
    
    print(F"The all rehab total and expense Cap rate: R{all_propCapRate}")
    
    print(F"The new value added to the property  : R{valueAdded}")
    print(F"The value of the property after rehab for refinacing: R{newValueProperty}")
    
    
    print("Press Any Key to continue... ")
    
    

    
    
   
   
    
    
    
print(homeLoanApplication())