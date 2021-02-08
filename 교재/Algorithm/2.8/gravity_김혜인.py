






# 틀린 풀이
# T = int(input())
# for i in range(T):
#     number_list = []
#     number_width = int(input())
#     number = list(map(int, input().split()))
#     number_list += number
#     max_num = number[0]
#     for j in number:
#         if j > max_num:
#             max_num = j
#
#     count_list = [0] * max_num
#
#     for k in range(max_num):
#         for num in number_list:
#             if num < (k+1):
#                 count_list[k] += 1
#
#     for count in count_list:
#         max_count = count_list[0]
#         if count > max_count:
#             max_count = count
#     print('#{} {}'.format(i+1, max_count))


















