def fibonacci(n):
    if n <= 0:
        return []

    sequence = [0, 1]
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence

n = int(input("Digite o número de termos da sequência de Fibonacci desejados: "))
fibonacci_sequence = fibonacci(n)
print(fibonacci_sequence)
