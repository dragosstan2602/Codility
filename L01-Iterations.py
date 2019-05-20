def solution(N):
    n_bin = bin(N)[2:]
    print(n_bin)
    l1 = []
    l2 = []
    for i in range(0, len(n_bin)):
        if n_bin[i] == '1':
            l1.append(i)

    if len(l1) in [0, 1]:
        return 0
    else:
        for j in range(1, len(l1)):
            l2.append(l1[j]-l1[j-1]-1)
        return max(l2)


print("N = {}".format(solution(2107403647)))