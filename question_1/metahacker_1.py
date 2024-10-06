import sys

def solve():
    input = sys.stdin.read
    data = input().splitlines()
    
    index = 0
    T = int(data[index]) 
    index += 1
    results = []
    
    for t in range(1, T + 1):
        N = int(data[index])
        index += 1
        
        max_lower_bound = 0
        min_upper_bound = float('inf')
        
        for i in range(1, N + 1):
            A, B = map(int, data[index].split())
            index += 1
            
            if B != 0:
                lower_bound = i / B
            else:
                lower_bound = float('inf')  

            if A != 0:
                upper_bound = i / A
            else:
                upper_bound = float('inf') 
            
            max_lower_bound = max(max_lower_bound, lower_bound)
            min_upper_bound = min(min_upper_bound, upper_bound)
        
        if max_lower_bound <= min_upper_bound:
            results.append(f"Case #{t}: {max_lower_bound:.6f}")
        else:
            results.append(f"Case #{t}: -1")
    
    with open("answer.txt", "w") as f:
        f.write("\n".join(results) + "\n")


with open("subsonic_subway_input.txt", "r") as f:
    sys.stdin = f
    solve() 
