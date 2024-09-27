result = 4 / 2
message = ("When you divide two numbers the result will always be a float: "
    f"4 / 2 = {result}\n")
print(message)

message2 = (
    "If you mix integers and floats in any operation, the result will "
    "always be a float: \n"
    f"\t1 + 2.0 = {1 + 2.0}\n"
    f"\t2 * 3.0 = {2 * 3.0}\n"
    f"\t3.0 ** 2 = {3.0 ** 2}\n"
)
print(message2)

message3 = (
    "You can group digits using underscores to make large numbers more "
    "readable: \n"
    f"\t14_000_000_000 = {14_000_000_000}\n"
    f"\t14_000_000_000 / 1_000_000 = {14_000_000_000 / 1_000_000}\n"
    f"\t1_000, 10_00, 100_0 👉 {1_000}, {10_00}, {100_0}\n"
)
print(message3)
