
def diagonalDifference(arr, n):

    first_dia_sum = sum(arr[i][i] for i in range(n))
    second_dia_sum = sum(arr[i][n - 1 - i] for i in range(n))
    #for finiding absolute difference use abs(a-b) function.
    return abs(first_dia_sum - second_dia_sum)

n = int(input().strip())
arr = [list(map(int, input().strip().split()))[:n] for i in range(n)]
print(diagonalDifference(arr, n))


