import random

def mid(A, l_mark, r_mark):
    flag = A[l_mark]
    l = l_mark
    r = r_mark+1
    while(l + 1 != r):
        if(A[l+1] <= flag):
            l += 1
        else:
            if(A[r-1] >= flag):
                r -= 1
            else:
                l += 1
                r -= 1
                A[l], A[r] = A[r], A[l]

    A[l_mark], A[l] = A[l], A[l_mark]
    return l


def fastsort(array, left, right):
    if(left < right):
        m = mid(array, left, right)
        fastsort(array, left, m-1)
        fastsort(array, m + 1, right)
    return array
    # if(left == right):
        # return array

if __name__ == '__main__':
    A = list(map(lambda x: random.randint(1, 500000), [y for y in range(10000)]))
    # print(A)
    # print(mid(A, 0, len(A)-1))
    # print(A)

    print(fastsort(A, 0, len(A)-1))
    print(A)
