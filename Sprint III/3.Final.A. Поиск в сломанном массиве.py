# Идентификатор успешной посылки - 52206322

# -- ПРИНЦИП РАБОТЫ --
# Сначала производится бинарный поиск "головы" закольцованного массива, т.е. наименьший элемент массива.
# Затем производится вычисление, в какой части массива следует искать элемент
# (путем сравнения с концом и началом массива и относительно "головы").
# Последним шагом выполняется бинарный поиск самого элемента в нужном отрезке массива.
#
# -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
# В рамках задачи требовалось реализовать поиск элемента в массиве, который выполняется за O(log n)
# и так как в решении использовался бинарный поиск, данное условие выполняется.
#
# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
# Бинарный поиск "головы" массива выполняется за O(log n). Затем поиск непосредственно самого элемента тоже O(log n).
# В сумме получаем - O(log n).
#
# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
# Сложность в худшем случае будет равна O(logn) для хранения стека вызова функций.

def broken_search(nums, target) -> int:
    if target == nums[0]:
        return 0
    if target == nums[-1]:
        return len(nums) - 1

    head = head_binary_search(nums, 0, len(nums) - 1)

    if target == nums[head]:
        return head

    left = 0
    right = len(nums) - 1
    if head == 0:
        left = 1
    elif head == len(nums) - 1:
        right = len(nums) - 2
    elif nums[head] < target < nums[-1]:
        left = head + 1
    else:
        right = head - 1

    result = binary_search(nums, target, left, right)
    return result


def head_binary_search(nums, left, right):
    if left == right:
        return left

    mid = (right + left) // 2

    if nums[mid] > nums[right]:
        if right - mid == 1:
            return right
        else:
            return head_binary_search(nums, mid + 1, right)
    else:
        return head_binary_search(nums, left, mid)


def binary_search(nums, target, left, right):
    if right >= left:
        mid = (right + left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return binary_search(nums, target, left, mid - 1)
        else:
            return binary_search(nums, target, mid + 1, right)
    else:
        return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
