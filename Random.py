import random
random_Integer =random.randint(1,10)
print(random_Integer)
random_number0To10 = random.random()*10
print(random_number0To10)
random_float = random.uniform(1,10)
print(random_float)
ra_HeadsAndTails = random.randint(0,1)
if ra_HeadsAndTails == 0:
    print("Its Heads!!")
else:
    print("Tails!!")