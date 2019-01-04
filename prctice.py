

def main():
	n=5
	def func(x):
		print('x is', x)

	func(n)
	print(func(func(n)))

if __name__ == "__main__":
    main()
        