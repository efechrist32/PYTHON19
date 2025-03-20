def multiply_single_iteration(N, M):
    return N * M

def multiply_n_iterations(N, M):
    result = 0
    for _ in range(N):
        result += M
    return result

N = 5
M = 3

print("Single iteration result:", multiply_single_iteration(N, M))
print("N iterations result:", multiply_n_iterations(N, M))