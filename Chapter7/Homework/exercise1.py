"""
@Time ：06/04/2024 14:30
@Auth ：LIN Tianyuan
@File ：exercise1.py
@Motto：ABC(Always Be Coding)
"""


def indexMax(n_list):
    max_number = n_list[0]
    for i in range(7):
        if max_number < n_list[i]:
            max_number = n_list[i]
    return n_list.index(max_number)


number_list = [5, 8, 2, 1, 9, 3, 6, 7]
print(indexMax(number_list))

