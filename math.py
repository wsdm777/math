def solve(k_start, k_final, n_start, n_final):
    answer = 0
    for k in range(k_start, k_final + 1):
        res = 1
        for n in range(n_start, n_final + 1):
            res *= n / k
        answer += res * k
    return answer


print(solve(4, 10, 1, 5))
