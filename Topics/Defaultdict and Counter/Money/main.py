transactions = [(38177, 34.38), (876, 999.99), (654276, 653678), (54366, 0.99),
                (546, 987.65), (876, 3456), (654276, 0.55), (38177, 876.75), (876, 98.7)]

# create transaction_dict
transaction_dict = {}
for tuple_ in transactions:
    # set the default value to 0
    transaction_dict.setdefault(tuple_[0], [])
    # increment the value by 1
    transaction_dict[tuple_[0]].append(tuple_[1])
