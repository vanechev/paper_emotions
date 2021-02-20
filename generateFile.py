import statistics

resultados = open('./observaciones.csv')
datos = resultados.read()

files = {
    "group1/R1": -14,
    "group1/R2": -14,
    "group1/R3": -14,
    "group1/R4": -14,
    "group2/R1": 79,
    "group2/R2": 79,
    "group3/R1": 5,
    "group3/R2": 5,
    "group3/R3": 5
}

data = open('./data.csv', "w")
i = 0

for dato in datos.split("\n"):
    info = dato.split(";")
    url = './new/' + info[3] + "/" + info[4] + "/EDA.csv"
    
    file_eda = open(url)
    eda = file_eda.read().split("\n")
    
    for i in range(0, len(eda)):
        eda[i] = float(eda[i])

    url = './new/' + info[3] + "/" + info[4] + "/HR.csv"
    file_hr = open(url)
    hr = file_hr.read().split("\n")
    
    for i in range(0, len(hr)):
        hr[i] = float(hr[i])

    seg_hr = (int(info[1]) + files.get(info[3] + "/" + info[4]))
    #seg_hr = int(info[1])
    seg = seg_hr * 4

    data_eda = eda[(seg - 20):(seg + 20)]
    data_hr = hr[(seg_hr - 5):(seg_hr + 5)]

    #print(data_eda)
    #print(data_hr)

    data.write(
        info[0] + ";"
        + str(statistics.mean(data_eda)) + ";" + str(statistics.stdev(data_eda)) + ";"
        + str(statistics.mean(data_hr)) + ";" + str(statistics.stdev(data_hr)) + ";"
        + info[2]
        + "\n")

    file_hr.close()
    file_eda.close()

data.close()
resultados.close()