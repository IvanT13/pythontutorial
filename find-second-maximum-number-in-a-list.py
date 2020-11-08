#Challenge https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    maks = max(arr)
    x = 1
    for i in range(0,n):
        if(arr[i] == maks):
            x = x + 1
    print (arr[n-x])