from fractions import Fraction

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:  
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def expected_days(W, G, L):
    if W <= G:
        return Fraction(0)

    dp = {}
    for x in range(G, W + 1):
        if x == G:
            dp[x] = Fraction(0)
        else:
            E_x_minus_1 = dp.get(x - 1, Fraction(0))
            E_x_plus_1 = dp.get(x + 1, Fraction(0))
            dp[x] = Fraction(1) + (E_x_minus_1 + E_x_plus_1) / 2

        if x > G + L:
            dp[x] = dp[x - 1] + 1

    return dp[W]

def solve(input_file, output_file):
    MOD = 998244353
    with open(input_file, 'r') as file:
        T = int(file.readline().strip())
        results = []
        for i in range(1, T + 1):
            W, G, L = map(int, file.readline().strip().split())
            expected = expected_days(W, G, L)
            p = expected.numerator
            q = expected.denominator
            p_inv = mod_inverse(q, MOD) 
            result = (p * p_inv) % MOD
            results.append(f"Case #{i}: {result}")

    with open(output_file, 'w') as out_file:
        out_file.write("\n".join(results))

if __name__ == "__main__":
    solve('input.txt', 'answer.txt')
