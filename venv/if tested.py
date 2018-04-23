state = input('Enter state:')                 # Either CA, MN, or NY
purchase_amount = float(input('Enter purchase :'))                     # amount of purchase
result = ''
if state == 'CA':
    tax_amount = .075
    total_cost = purchase_amount*(1 + tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == 'MN':
    tax_amount = .095
    total_cost = purchase_amount*(1 + tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == 'NY':
    tax_amount = .089
    total_cost = purchase_amount*(1 + tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

print(result)
