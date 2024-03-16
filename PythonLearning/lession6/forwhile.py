
def list_while_func():
    my_list = ["hello", "world", "Python"]

    index = 0
    while index < len(my_list):
        element = my_list[index]
        print(f"列表的元素:{element}")
        index += 1


def list_for_func():
    my_list = [1, 2, 3, 4, 5]
    for element in my_list:
        print(f"列表中的元素有: {element}")


list_while_func()
list_for_func()

