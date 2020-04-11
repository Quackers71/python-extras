def get_budgets(lst):
	result = [ sub['budget'] for sub in lst ]
	return sum(result)


get_budgets = [
  { "name": "John", "age": 21, "budget": 23000 },
  { "name": "Steve",  "age": 32, "budget": 40000 },
  { "name": "Martin",  "age": 16, "budget": 2700 }] 
  # 65700

get_budgets = [
  { "name": "John",  "age": 21, "budget": 29000 },
  { "name": "Steve",  "age": 32, "budget": 32000 },
  { "name": "Martin",  "age": 16, "budget": 1600 }] 
  # 62600

result = [ sub['budget'] for sub in get_budgets ]

#print(sum(result))

#print(get_budgets(lst))
    
