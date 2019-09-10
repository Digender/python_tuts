from chef import Chef
from chinese_chef import ChineseChef

chef = Chef('Digender')
chineseChef =  ChineseChef('Digender', 'Chinese')

chef.can_make_food()
chineseChef.can_make_chinese_dish()

print('==============================')
print('after overriding method can_make_food()')
print('==============================')
chineseChef.can_make_food()

