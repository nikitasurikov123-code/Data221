def x_to_power_of_y(x, y):
    #returns x^y
    return x**y
pairs_xy = [[2,2], [3,3], [4,4], [5, -5]]
#new list of computated values of x^y
completed_computation = []
#loops through each x,y pair in the list to see if y < 0, then skips it if y < 0
for x,y in pairs_xy:
    if y < 0:
        continue
    #computes x^y then adds it to the empty list completed_computation
    completed_computation.append(x_to_power_of_y(x,y))
print(completed_computation)