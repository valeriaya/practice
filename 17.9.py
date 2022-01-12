def check(lst)->bool:
    for a in range(len(lst)):
        try:
            lst[a] = float(lst[a])
        except:
            return False
    return True

def sort(lst):
    for i in range(len(lst)):
        idx_min = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[idx_min]:
                idx_min = j
        if i != idx_min:
            lst[i], lst[idx_min] = lst[idx_min], lst[i]


def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] < element and array[middle+1]>=element:
        return middle
    elif element <= array[middle]:
        return binary_search(array, element, left, middle)
    else:
        return binary_search(array, element, middle + 1, right)


sequence = input("Введите последовательность чисел через пробел: ").split()
try:
    element = float(input('Введите любое число в пределах последовательности: '))
except:
    print('Введено неверное значение. Введите число еще раз: ')
else:
    if check(sequence):
        sort(sequence)
        idx = binary_search(sequence,element,0,len(sequence)-1)
        if  idx != False:
            print(sequence)
            print(f'Индекс элемента списка, удовлетворяющий условию: {idx}')
        else:
            print(f'Элемент списка, удовлетворяющий условию отсутствует')
    else:
        print('Введены неверные значения в последовательности чисел')
