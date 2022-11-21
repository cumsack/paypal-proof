email = input("Email: ")
amount = input("Amount: ")

with open(f"output.html", "w") as file:
    file.write(open("template.html", "r").read().replace("AMOUNT", amount).replace("EMAILHERE", email))

print("Final Result In output.html")
os.system("pause >nul")
