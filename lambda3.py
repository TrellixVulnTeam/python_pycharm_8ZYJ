attack ={'quick':(lambda :print("quick attack")),
         'power': (lambda : print("power attack")),
         'miss':(lambda :print("missed attack"))}
attack['quick']()

import random
attackKey=random.choice(list(attack.keys()))

attack[attackKey]()