def dict_func(person,key):
    return person[key]


dict= {'name': 'Alice','age':25, 'city':'New York'}
dict['job']='Engineer'

print(f'{dict.items()}\n\n\n\n')


for key,value in dict.items():
    print(f'The key is: {key} and the value is: {value}')


print(dict_func(dict,'age'))

dict.pop('city')
print(f'The updated dictionary is: {dict}')


def func_name(age,ID,name='lol'):
    print(age,ID)

func_name(ID=123456789,age=15)

