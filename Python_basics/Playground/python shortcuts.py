# a= 'meh'
#
# # they do this
# if a == 'count_in_this_way':
#     result = 'count_in_this_way'
# elif a == 'that_way':
#     result = 'that_way'
# elif a == 'another_way':
#     result = 'another_way()'
# else:
#     result = 'standard_way'()
#
# print(result)
# print()
# # instead of this
# ways_to_count = {
#     'count_in_this_way': 'count_in_this_way',
#     'that_way': 'that_way',
#     'another_way': 'another_way'
# }
# result = ways_to_count.get(a, 'standard_way')
# print(result)
################
print()
# they do this
common = []
foo = [1, 2, 3, 5, 6, 9]
bar = [2, 4, 5, 6, 10]
for a in foo:
    if a in bar:
        common.append(a)
print(type(common))
print(common)
print()
# instead of this
foo = [1, 2, 3, 5, 6, 9]
bar = [2, 4, 5, 6, 10]
common = set(foo) & set(bar)
print(type(common))
print(common)
