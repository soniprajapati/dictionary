# dict1={"brand":"suzuki","modal":"desire","year":2020,}
# print(dict1)
# x=dict1["modal"]
# print(x)
# y=dict1.get("modal")
# print(y)

# dict1={"brand":"suzuki","modal":"desire","year":2020,}
# for x in dict1:
#     print(x)


# dict1={"brand":"suzuki","modal":"desire","year":2020,}
# for x in dict1:
#     print(dict1[x])

# dict1={"brand":"suzuki","modal":"desire","year":2020,}
# for x in dict1.values():
#     print(x)


# dict1={"brand":"suzuki","modal":"desire","year":2020,}
# for x,y in dict1.items():
#     print(x,y)


# Dict = {'ball' : 'green','Ball': 'red'}
# print(Dict['ball'])
# print(Dict['Ball'])
# print(Dict['bat'])


# city_population = {"NewYorkCity":8550405,"LosAngeles":3971883,"Toronto":2731571, "Chicago":2720546, "Houston":2296224, "Monteal":1704694,"Calgary":1239220, "Vancouver":631486,"Boston":667137
# }

# print(city_population["NewYorkCity"])
# print(city_population)
# print(type(city_population))


# student=dict(name= "Ravina",age= 20)
# print(student)


# my_dict = {1: 'apple', 2: 'ball'}
# print(my_dict)


# my_dict ={1: 'apple',2: 'ball'}
# print(my_dict)

# NASTED DICTIONARY
# Dic= {1: 'NAVGURUKUL',2: 'IN',  3:{'A' : 'WELCOME','B' : 'To', 'C' : 'DHARAMSALA'}
# }
# print(Dic)


# person={
#  'name':'jack',
#  'age':20,
#  'gender':'male',
#  4:'organisation'}

# result = person['age'] 
# x = person.get("gender")
# print(person[4])
# print(x)
# print(result)


# person={
#  'name':'jack',
#  'age':20,
#  'gender':'male',
#  4:{
#   'organisation':'navgurukul','place':'dharamsala'
#   }
#  }
# print(person['gender'])

# print(person[4])

# result = person[4]['place']

# print(result)

# students_DB={}
# while True:
#     line=input("please enter ID and name saparated by comma or q to exit:")
#     if line=="q":
#         break
#     id,name=line.split(",")
#     students_DB.update({id:name})
# for x,y in students_DB.items():
#     print(x,y)
# key=input("enter id to search:")
# if key in students_DB:
#     print("key=",key,"value=",students_DB[key])
# else:
#     print("key not found:")