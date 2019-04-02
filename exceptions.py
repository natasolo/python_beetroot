def divide(a: int, b: int):
	return a / b

try:
	a = int(input("a="))
	b = int(input("b="))
	print(divide(a, b))
except Exception as e:
	print(e)
