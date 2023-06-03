def selectionSort(accounts):
    size = len(accounts)
    for i in range(size):
        smallest_index = i
        for j in range(i+1,size):
            if accounts[j][1] < accounts[smallest_index][1]:
                smallest_index = j
        accounts[i],accounts[smallest_index] = accounts[smallest_index],accounts[i]

def linear_search(accounts,target_balance):
    for account in accounts:
        if account[1] == target_balance:
            return account
    return None

if __name__ == '__main__':
    account_balance = [
        ("John", 500),
        ("Alice", 200),
        ("Bob", 1000),
        ("Eve", 800),
        ("Mike", 300)
    ]
    target_balance = int(input("Enter your balance to find: "))

    selectionSort(account_balance)

    found_account = linear_search(account_balance,target_balance)

    if found_account is not None:
        print(f'The account with balance {target_balance} is found for {found_account[0]}')
    else:
        print(f'No account with balance {target_balance} was found!')

