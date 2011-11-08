grid = 1001
pos = [0]
jump = 2
# find the zero-based index in the list [1,2,3,...]
# of each corner in the spiral
while pos[-1] < grid * grid-1:
    ind = pos[-1] + jump
    pos.extend([ind, ind + jump, ind + 2 * jump, ind + 3 * jump])
    jump += 2

#numbers to sum are the indices + 1
print sum(pos) + len(pos)
