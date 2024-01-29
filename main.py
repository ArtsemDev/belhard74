# print(3, 5, 4, "hello", sep="-|-", end=" finish! ")
# print(5, 4, 3)

# text = input("Enter some text: ")
# print(text)
# a = None
# a = -3.14159
# b = round(a, 2)
# print(b)
# c = abs(a)
# print(c)
# a = 100_000_000_000
# print(a)
# a = "-23_423"
# c = 4545.9999
# b = int(c)
# print(b)

# a = "-34.34_2323"
# b = float(a)
# print(b)
# print(float("inf"))
# print(float("nan"))
# print(float("-inf"))
# print(float("-nan"))

# a = "FFFF"
# print(int(a, 16))
# a = 126
# print(oct(a))

# print(bool(" "))
# text = "Hello world\vpython"
# print(text)
# a = len(text)
# print(a)
# text = "Python"
# print(text[0])
# print(text[-6])
# [-len:len)
# reversed_text = text[::-1]
# print(text)
# print(reversed_text)

# print(str(True))
# print(str(None))
# print(str(2345))


# path = r"C:\\Users\n\t\n\a\rewforlder"
# print(path)


name = "Alex"
age = 34

# text = "Hello " + name + " " + str(age)
# print(text)
# data = {"first_name": name, "user_age": age}
# text = "Hello %(first_name)s %(user_age)s %(user_age)s" % data
# print(text)
# text = "Hello {first_name} {user_age}".format(first_name=name, user_age=age)
# print(text)
# text = f"Hello {name} {age + 2}"
# print(text)

# a = 42
# b = str(a)
# c = f"{a}"

# text = "привет мир".encode()
# print(len(text))
# text2 = "привет мир"
# print(len(text2))
# text = u"hello мир"
# print(text)

# emoji = "fire"
# text = f"\N{fire} {emoji}"
# print(text)

# text = f"{3.587:.5f}"
# text2 = f"{round(3.587, 2)}"
# print(text)
# print(text2)

# text = "hello WORLD python  ß"
# print(text.capitalize())
# print(text.lower())
# print(text.upper())
# print(text.swapcase())
# print(text.casefold())
# print(text.title())

# text = "Hello---WoWoWorld---Python"
# print(text.find("Wo"))
# print(text.rfind("Wo"))
# print(text.index("Wo1"))
# print(text.rindex("Wo1"))
# words = text.split(sep="---")
# text2 = "-|-".join(words)
# print(text2)
# words2 = text.rsplit(sep="---", maxsplit=1)
# print(words)
# print(words2)
# print(text.islower())
# print(text.isupper())
# print(text.istitle())
# print(text.isalpha())
# print(text.isdigit())
# print(text.isdecimal())
# print(text.isnumeric())
# print(text.isalnum())
# print(text.isspace())
# print(text.isascii())
# print(text.isidentifier())
# print(text.isprintable())
# text = "Hello python python world"
# print(text.partition("Python"))
# print(text.rpartition("Python"))

# text = "Hello python world"
# print(text.replace(" ", ""))

# text = "Hello world"
# print(text.endswith("rld"))
# print(text.startswith("Hel", 1, 7))

# text = "Hello world"
# print(text.removeprefix("Hell"))
# print(text.removesuffix("rld"))

# text = "Hello world"
# if text.startswith("Hell"):
#     text = text.replace("Hell", "", 1)

# text = "./././--,,Hello...///World,.,.,/./,,"
# print(text.rstrip(",./-"))
# print(text.lstrip(",./-"))
# print(text.strip(",./-"))
# text = "Hello\twor\tpyt"
# print(text.expandtabs(tabsize=4))

# text = "Hell"
# print(text.center(10, "-"))
# print(text.ljust(10, "-"))
# print(text.rjust(10, "-"))
# print(text.zfill(10))

# print(bin(12)[2:].zfill(8))
# print("Hello".encode().decode())
# str


# print("Hello world".count("ell", 5))


# print("hello" not in "Hello world")

# a = 3600
# b = 60 * 60
# print(a is b)
# print("hello" < "hello world")
# print(bin(15))
# print(bin(14))
# print(15 ^ 14)


# n = 128
# print((n & (n-1) == 0) and n != 0)
# print(bin(15))
# print(bin(~15))

# print(~-800)

# text = "Hello world"
# print(text[2], text[~2])
print(bin(13))
print(bin(13 >> 2))
print(bin(13 << 2))
