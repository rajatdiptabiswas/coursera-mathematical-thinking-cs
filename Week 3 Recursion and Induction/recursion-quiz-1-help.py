# Largest Amount that Cannot Be Paid with 5- and 7-Coins
# Answer -> 23


ans = []


def add_ans(val, times):
    global ans

    if times == 0:
        return

    if val not in ans:
        ans.append(val)

    add_ans(val+5, times-1)
    add_ans(val+7, times-1)


add_ans(0, 8)
print(sorted(ans))
