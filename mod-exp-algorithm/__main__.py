from mod_exp import mod_exp

RANGE = 600

total = 0
right = 0
wrong = 0

for i in range(10, RANGE):
    print('starting', i)
    for j in range(10, RANGE):
        for k in range(10, RANGE):
            total += 1
            _pow = pow(i, j, k)
            _mod_exp = mod_exp(i, j, k)
            if(_pow == _mod_exp):
                right += 1
            else:
                wrong += 1

print('total', total)
print('right', right)
print('wrong', wrong)
