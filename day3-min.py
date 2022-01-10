from statistics import multimode
# loading input
f = open("day3.dat", "r")

contents = f.read()
# split into lines
contents_split = contents.splitlines()



gamma = bin(int("".join(list(map(lambda x: max(multimode(map(lambda y: (y[x]), contents_split))), range(12)))),2))
epsilon = gamma - 1
print(gamma, epsilon)





#epsilon_rate_bin = "".join(list(map(lambda x: find_most_common_bit(list_from_pos(contents_split, x), True), range(number_bits))))