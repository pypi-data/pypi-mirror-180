# Импликация   'x → y'   'x <= y'
# Или          'x ∨ y'   'x or y'
# И            'x ∧ y'   'x and y'
# Не           ' ¬ x '   'not x'
# Эквиваленция 'x ≡ y'   'x == y'

from itertools import product

print('x y z w | sum |')
print('——————— + ——— +')

for x, y, z, w in product(range(2)):
    if ((x <= y) or (y == w)) and ((x or z) == w):
        print(x, y, z, w,'| ', sum([x, y, z, w]),' |')
