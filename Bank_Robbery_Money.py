print()
cash = 19867324678987.99

print("19 trillion dollars divided amongst five robbers is...")
print("$", "{:,}".format(cash / 5))
print()

print("Why tf not? Let's try it a weird way too!")
print("$", "{:.10f}".format(cash / 5).replace(".", ","))
print()

print("Let's try it another weird way too!")
cashA = list(str(19867324678987.99 / 5))
cashA.insert(3, ",")
print(cashA)
print()

print("And that soon becomes...")
cashB = "".join(cashA)
print("$", cashB)
print()

print("And, finally, the desired result! ...")
cashA.insert(9, ",")
cashB = "".join(cashA)
print("$", cashB)
print()

print("And, just for the Hell of it...")
cashA.insert(1, ".")
cashA.insert(4, " * 10 ^ 13")
cashB = "".join(cashA[0:5])
print("$", cashB)
print()