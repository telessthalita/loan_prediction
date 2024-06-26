def calculate_accuracy(matrix):
    VP, FP, FN, VN = map(int, matrix)
    accuracy = (VP + VN) / (VP + FP + FN + VN) if (VP + FP + FN + VN) != 0 else 0
    precision = VP / (VP + FP) if (VP + FP) != 0 else 0
    return accuracy, precision

def best_performance(matrices):
    best_index = -1
    best_accuracy = 0
    best_precision = 0

    for index, matrix in enumerate(matrices):
        accuracy, precision = calculate_accuracy(matrix)
        performance_index = (accuracy + precision) / 2

        if performance_index > (best_accuracy + best_precision) / 2:
            best_index = index
            best_accuracy = accuracy
            best_precision = precision

    return best_index, best_accuracy, best_precision

n = int(input().strip())
matrices = []

for _ in range(n):
    matrix = input().strip().split(',')
    matrices.append(list(map(int, matrix)))

best_index, best_accuracy, best_precision = best_performance(matrices)

print(f"Índice: {best_index + 1}")
print(f"Acurácia: {best_accuracy:.2f}")
print(f"Precisão: {best_precision:.2f}")
