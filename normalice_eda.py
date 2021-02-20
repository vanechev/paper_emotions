files = [
    "group1/R1",
    "group1/R2",
    "group1/R3",
    "group1/R4",
    "group2/R1",
    "group2/R2",
    "group3/R1",
    "group3/R2",
    "group3/R3"
]

for file in files:
    url = './old/' + file + "/EDA.csv"
    print(url)
    file_eda = open(url)
    eda = file_eda.read().split("\n")

    max_e = max(eda)
    min_e = min(eda)

    new_eda = open('./new/' + file + "/EDA.csv", "w")

    for e in eda:
        corrected_EDA = abs(float(e) - float(max_e)) / abs(float(max_e) - float(min_e))
        new_eda.write(str(corrected_EDA), "\n")

    new_eda.close();

    file_eda.close()