def merge(arr, lf, mid, rg):
    if len(arr) == 1:
        return arr
  
    left = merge(arr[0 : len(arr)//2], 0, 0, 0)
    right = merge(arr[len(arr)//2 : len(arr)], 0, 0, 0)

    result = [0] * len(arr)

    l, r, k = 0, 0, 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result[k] = left[l]
            l += 1
        else:
            result[k] = right[r]
            r += 1
        k += 1

    while l < len(left): 
        result[k] = left[l]
        l += 1
        k += 1  
    while r < len(right): 
        result[k] = right[r]
        r += 1
        k += 1

    return result


def merge_sort(arr, lf, rg):
    result = merge(arr[lf:rg], 0, 0, 0)

    while rg < len(arr):
        result.append(arr[rg])

    for i in range(len(result)):
        arr[i] = result[i]


def test():
	a = [1, 4, 9, 2, 10, 11]
	b = merge(a, 0, 3, 6)
	expected = [1, 2, 4, 9, 10, 11]
	assert b == expected
	c = [1, 4, 2, 10, 1, 2]
	merge_sort(c, 0 , 6)
	expected = [1, 1, 2, 2, 4, 10]
	assert c == expected
