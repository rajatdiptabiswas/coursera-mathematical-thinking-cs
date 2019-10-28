'''
Pay Any Large Amount with 5- and 7-Coins

Question 1

Develop a Python method change(amount) that for any integer amount in the range from 24 to 1000 returns a list consisting of numbers 5 and 7 only, such that their sum is equal to amount. For example, change(28) may return [7, 7, 7, 7], while change(49) may return [7, 7, 7, 7, 7, 7, 7] or [5, 5, 5, 5, 5, 5, 5, 7, 7] or [7, 5, 5, 5, 5, 5, 5, 5, 7].

To solve this quiz, implement the method change(amount) on your machine, test it on several inputs, and then paste your code in the field below and press the submit quiz button. Your submission should contain the change method only (in particular, make sure to remove all print statements).
'''

def change(amount):
    assert(amount >= 24)

    if amount == 24:
        return [5, 5, 7, 7]
    if amount == 25:
        return [5, 5, 5, 5, 5]
    if amount == 26:
        return [5, 7, 7, 7]
    if amount == 27:
        return [5, 5, 5, 5, 7]
    if amount == 28:
        return [7, 7, 7, 7]
    # if amount == 29:
    #     return [5, 5, 5, 7, 7]
    # if amount == 30:
    #     return [5, 5, 5, 5, 5, 5]
    # if amount == 31:
    #     return [5, 5, 7, 7, 7]

    coins = change(amount-5)
    coins.append(5)

    return coins
