import pulp

# Створення проблеми лінійного програмування
prob = pulp.LpProblem("Production_Optimization", pulp.LpMaximize)

# Змінні для кількості виробленого лимонаду та фруктового соку
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Continuous')

# Цільова функція: максимізація загальної кількості продуктів
prob += lemonade + fruit_juice, "Total Products"

# Обмеження на ресурси
prob += 2 * lemonade + fruit_juice <= 100, "Water"
prob += 1 * lemonade <= 50, "Sugar"
prob += 1 * lemonade <= 30, "Lemon Juice"
prob += 2 * fruit_juice <= 40, "Fruit Puree"

# Розв'язування задачі
prob.solve()

# Виведення результатів
print("Статус:", pulp.LpStatus[prob.status])
print("Кількість виробленого лимонаду:", pulp.value(lemonade))
print("Кількість виробленого фруктового соку:", pulp.value(fruit_juice))
print("Загальна кількість продуктів:", pulp.value(prob.objective))
