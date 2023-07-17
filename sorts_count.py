# Author: Joe Storto
# Github Username: Jstorto21
# Date: 7/16/2023
# Description: Program counts comparisons and exchanges in bubble and insertion sort methods


def bubble_count(a_list):
    comparisons = 0
    exchanges = 0

    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):
            comparisons += 1
            if a_list[index] > a_list[index + 1]:
                temp = a_list[index]
                a_list[index] = a_list[index + 1]
                a_list[index + 1] = temp
                exchanges += 1
    return print(comparisons, exchanges)


def insertion_sort(a_list):
    comparisons = 0
    exchanges = 0

    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        comparisons += 1
        while pos >= 0 and a_list[pos] > value:
            a_list[pos + 1] = a_list[pos]
            exchanges += 1
            pos -= 1
            comparisons += 1
        a_list[pos + 1] = value
    return print(comparisons, exchanges)
