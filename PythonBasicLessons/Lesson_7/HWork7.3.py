# Substring search
### Var #1:
def second_index(ryad_1, ryad_2):
    s_index = 0
    ryad_iter = ryad_1
    if ryad_1.count(ryad_2) <= 1:
        s_index = None
    elif 1 < ryad_1.count(ryad_2) <= 2:
        k1 = ryad_iter.index(ryad_2)
        k2 = (ryad_iter).index(ryad_2,k1+1)
        s_index = k2
    return s_index
rd_1 = "Hello, hello"
rd_2 = "lo"

print("==", second_index(rd_1, rd_2))

#########################################################################
### Var #2(first difficult variant):
# def second_index(ryad_1, ryad_2):
#     num_index = 0
#     s_index = 0
#     ryad_iter = list(ryad_1)
#     if ryad_1.count(ryad_2) <= 1:
#         s_index = None
#     elif 1 < ryad_1.count(ryad_2) <= 2:
#         while num_index <= 2:
#             if num_index == 2:
#                 return s_index
#                 break
#             s_index = ("".join(ryad_iter)).index(ryad_2)
#             if ryad_2 in ("".join(ryad_iter)):
#                 if len(ryad_2) == 1:
#                     del ryad_iter[s_index]
#                     ryad_iter.insert(s_index, "1")
#                 elif len(ryad_2) > 1:
#                     del ryad_iter[s_index:s_index+2]
#                     for i in range(len(ryad_2)):
#                         ryad_iter.insert(s_index, "1")
#             num_index += 1
#     # else:
#     #     return s_index
#
# rd_1 = "Hello, hello"
# rd_2 = "lo"

# print("==", second_index(rd_1, rd_2))

