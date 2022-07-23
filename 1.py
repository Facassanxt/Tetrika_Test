# Дан массив чисел, состоящий из некоторого количества подряд идущих единиц,
# за которыми следует какое-то количество подряд идущих нулей: 111111111111111111111111100000000.
# Найти индекс первого нуля (то есть найти такое место, где заканчиваются единицы, и начинаются нули)
# def task(array):
#     pass

# print(task("111111111110000000000000000"))
# # >> OUT: 11

def task0(array): #Быстрый алгоритм
    return array.find("0")

def task1(array): #Быстрый алгоритм
    try:
        return array.index("0")
    except ValueError:
        return -1

def task2(array):
    for i, symbol in enumerate(array):
        if symbol == "0":
            return i
    return -1

def task3(array):
    for i in range(len(array)):
        if array[i] == "0":
            return i
    return -1

def task4(array): #Быстрый алгоритм
    c = array.count("1")
    if len(array) > c:
        if array[c+1] == "0":
            return c
    return -1

if __name__ == "__main__":
    array = "111111111110000000000000000"
    for i in range(5):
        function = globals()['task' + str(i)](array)
        print(f"{i+1}: {function}")
