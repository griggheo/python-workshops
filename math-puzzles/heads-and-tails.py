import random
import matplotlib.pyplot as plt

results = {}
for i in range(100):
    r = random.randrange(100)
    if r%2:
        #print(f'Got {r}, marking tails')
        results['tails'] = results.get('tails', 0) + 1
    else:
        #print(f'Got {r}, marking heads')
        results['heads'] = results.get('heads', 0) + 1

heads = results['heads']
tails = results['tails']
print(f'Heads came out {heads} times')
print(f'Tails came out {tails} times')

plt.bar(range(2), 
    [results['heads'], results['tails']], 
    align='center', color=['red', 'blue'])
plt.xticks(range(2), ['Heads', 'Tails'])

plt.show()
