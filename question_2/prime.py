def sieve_of_eratosthenes(limit):
    """ Generate all primes up to limit using the Sieve of Eratosthenes """
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False 
    for start in range(2, int(limit**0.5) + 1):
        if sieve[start]:
            for i in range(start * start, limit + 1, start):
                sieve[i] = False
    primes = [num for num, is_prime in enumerate(sieve) if is_prime]
    prime_set = set(primes)
    return primes, prime_set

def count_subtractorizations(N, primes, prime_set):
    """ Count how many N-subtractorizations exist """
    count = 0
    for p in primes:
        if p > N:
            break
        for q in primes:
            if q > p:
                break
            if (p - q) in prime_set:
                count += 1
                break  
    return count

def solve(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    T = int(lines[0]) 
    cases = [int(lines[i].strip()) for i in range(1, T + 1)]
    max_N = max(cases)
    primes, prime_set = sieve_of_eratosthenes(max_N)

    results = []
    for i, N in enumerate(cases, 1):
        result = count_subtractorizations(N, primes, prime_set)
        results.append(f"Case #{i}: {result}")
    
    with open(output_file, 'w') as out_file:
        out_file.write("\n".join(results))

if __name__ == "__main__":
    solve('inpu.txt', 'answer.txt')
