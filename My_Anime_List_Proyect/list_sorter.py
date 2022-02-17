a = 1
b = 2
c = 3

sort_list = [a, c, b, 8, 14, 82, 90]

def list_sorter(element_list: list, iterations):
    iterations -= 1
    try:
        counter = 0
        while counter < len(element_list):
            iter_1 = element_list[counter]
            iter_2 = element_list[counter + 1]

            if iter_1 >= iter_2:
                element_list[counter] = iter_1
            else:
                element_list[counter] = iter_2
                element_list[counter + 1] = iter_1

            counter += 1

        return list_sorter(element_list, iterations)

    except IndexError:
        if iterations > 0:
            return list_sorter(element_list, iterations)
        else:
            return element_list

new_list = list_sorter(sort_list, len(sort_list))
print(new_list)