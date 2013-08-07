if __name__ == '__main__':
	source = '''if __name__ == '__main__':
	source = {1}{0}{1}
	print(source.format(source, "{2}", r"{2}", r"{3}"))'''
	print(source.format(source, "\'\'\'", r"\'\'\'", r"\\\\'\\\\'\\\\'"))