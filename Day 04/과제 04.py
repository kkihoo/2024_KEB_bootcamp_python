# 8.1
e2f = {"dog":'chien', 'cat' :'chat', 'walus':'morse'}

# 8.2
print(e2f['walus'])
print(e2f.get('walus'))

# 8.3 item()과 컴프리헨션 사용
f2e = {}
print({f2e:e2f for e2f,f2e in e2f.items()}) #comprehension

for eng,fra in e2f.items(): #for문 활용
    f2e[fra] = eng
print(f2e)

#8.4
print(f2e['chien'])
print([e2f for e2f,f2e in e2f.items() if f2e == 'chien'])
print({f2e:e2f for e2f,f2e in e2f.items() if f2e == 'chien'})

#8.5
print(e2f.keys())
print(list(e2f.keys()))

#8.6
life = {
    'animal': {
    'cat': 'Henri',
    'octopi' : 'Grumpy',
    'emus' : 'Lucy'
    },
    'plants': {
    },
    'other' : {
    }
}

#8.7
print(life.keys())
print(list(life.keys()))

#8.8
print(life['animal'].keys())
print(list(life['animal'].keys()))

#8.9
print(life['animal']['cat'])

#8.10
squares = {key: key*key for key in range(10)}
print(squares)
