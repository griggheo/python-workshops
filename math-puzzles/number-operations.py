numbers = [2, 3, 4, 5, 7]
operations = ['+', '-', '*', '/']
#counter = 0
results = {}
for n1 in numbers:
    for n2 in numbers:
        if n2 == n1:
            continue
        for n3 in numbers:
            if n3 in [n1, n2]:
                continue
            for n4 in numbers:
                if n4 in [n1, n2, n3]:
                    continue
                for n5 in numbers:
                    if n5 in [n1, n2, n3, n4]:
                        continue
                    #print(f'{n1} {n2} {n3} {n4} {n5}')
                    for op1 in operations:
                        for op2 in operations:
                            for op3 in operations:
                                for op4 in operations:
                                    expression = f'{n1}{op1}{n2}{op2}{n3}{op3}{n4}{op4}{n5}'
                                    result = eval(expression)
                                    if type(result) is int and result > 0:
                                        #print(f'{expression}={result}')
                                        results.setdefault(result, []).append(expression)
                                        #counter += 1
#print(f'Counter; {counter}')

keys = results.keys()
for key in sorted(keys):
    print(key)

for i in range(1,101):
    if i not in keys:
        print(f'Did not find a way to obtain {i}')

for item in sorted(results, key=lambda k: len(results[k]), reverse=True):
    l = len(results[item])
    print(f'{item} can be obtained in {l} ways:')
    print(results[item])