import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pizzeria.settings")

import django
django.setup()

from pizzas.models import Pizza


pizzas = Pizza.objects.all()

'''
print(pizzas)

for p in pizzas:
    print(p.pizza_name)
'''
p = Pizza.objects.get(id=3)
print(p)

#Refer to django 2 lecture for more info