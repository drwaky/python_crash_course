first_name = " john "
last_name = " doe "
message = ("Names:\n"
    f"\t {first_name} {last_name} \t👈 No stripping\n"
    f"\t {first_name.strip()} {last_name.strip()} \t👈 Stripping Both sides\n"
    f"\t {first_name.lstrip()} {last_name.lstrip()} \t👈 Stripping on the Left\n"
    f"\t {first_name.rstrip()} {last_name.rstrip()} \t👈 Stripping on the Right\n"
    f"\t {first_name.rstrip()} {last_name.lstrip()} \t👈 Stripping Right - Left\n"
    f"\t {first_name.lstrip()} {last_name.rstrip()} \t👈 Stripping Left - Right\n")
print(message)
