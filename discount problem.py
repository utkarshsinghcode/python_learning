# calculate fee discount

tution_fee = 1536

discount_offer = 10
# to calculate discount

discount = (tution_fee/100)*10    # (1536/100)*10

payment = (tution_fee - discount)   # fees after discount
                                    #1536-153.6=1382.4
print(payment)
