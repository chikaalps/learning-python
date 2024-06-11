currency= float(input("dollar"))
if currency > 500:
    print("please go to your local bank for this transaction")
elif currency <= 0:
    print("please enter a valid amount")

else:
    dollar_rate = float(input("enter rate"))
    amount_lcy = float(currency * dollar_rate)
    commission = 0.05
    total_return = amount_lcy - commission
    print("total return amount is ", total_return)










# jikjkmkmk


