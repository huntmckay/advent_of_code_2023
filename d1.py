#On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

fname = "d1_input"

with open(fname) as f:
    content = f.readlines()

why = [int(x[0] + x[1]) for x in [[x[0],x[-1]] for x in [[x for x in i if x.isdigit()] for i in [x.strip('\n') for x in content]]]]
print(sum(why))
