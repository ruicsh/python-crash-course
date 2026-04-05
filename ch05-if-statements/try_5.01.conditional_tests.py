car = "subaru"
print("Is car == 'subaru'? I predict True.")
print(car == "subaru")
print("Is car == 'audi? I predict False.")
print(car == "audi")

car = "bmw"
print("Is car == 'bmw'? I predict True")
print(car == "bmw")
print("Is car == 'ford'? I predict False")
print(car == "ford")

var = None
print("Is var == None? I predict True")
print(var is None)
print("Is var == 'False'? I predict False")
print(var is False)


var = []
print("Is var == []? I predict True")
print(var == [])
print("Is var == () I predict False")
print(var == ())

var = ["foo"]
print("Is var == ['foo']? I predict True")
print(var == ["foo"])
print("Is var == ['bar']? I predict False")
print(var == ["bar"])

var = "Foobar"
print("Is var.lower() == 'foobar'? I predict True")
print(var.lower() == "foobar")
print("Is var.lower() == 'Foobar'? I predict False")
print(var.lower() == "Foobar")

var = ["foo", "bar", "baz"]
print(f"Is 'bar' in {var}? I predict True")
print("bar" in var)
print(f"Is 'quz' in {var}? I predict False")
print("quz" in var)

var = ["foo", "bar", "baz"]
print(f"Is 'quz' not in {var}? I predict True")
print("quz" not in var)
print(f"Is 'foo' not in {var}? I predict False")
print("foo" not in var)
