keywords = ["ERROR", "WARNING", "INFO"]

count = {
    "ERROR": 0,
    "WARNING": 0,
    "INFO": 0
}

with open("log.txt", "r") as file:
    for line in file:
        for key in keywords:
            if key in line:
                count[key] += 1

with open("summary.txt", "w") as output:
    output.write("Log File Summary\n")
    output.write("----------------\n")
    for key in count:
        output.write(f"{key}: {count[key]}\n")

print("Log analysis completed. Summary written to summary.txt")
