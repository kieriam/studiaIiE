def calculate_loan(loan_amount, year, annual_interest, type):
    if type == "staly":
        r = annual_interest / 100 / 12
        n = year *12
        q = 1+r
        installment = loan_amount *(q**n*(q-1))/(q**n-1)
        print(installment)

    elif type == "malejacy":
        n = year * 12
        r = annual_interest / 100 / 12
        for i in range(1, n+1):
            capital_part = loan_amount / n
            remaining = loan_amount - (i -1) * capital_part
            intrest = remaining * r
            installment = capital_part + intrest
            print(f"Rata {installment}")

calculate_loan(10000,5,3,"staly")
calculate_loan(4000,2,17,"staly")
