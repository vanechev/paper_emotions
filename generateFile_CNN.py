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

class_dimensional = {
    1: "HALV",
    2: "HAHV",
    3: "LALV",
    4: "LAHV",
}

data = open('./data_CNN.csv', "w")
data.write("group;nurse;hr_rate;eda;class;time\n")
i = 0

def convert(seconds): 
    seconds = seconds % (24 * 3600) 
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%02d:%02d" % (minutes, seconds) 

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

    data_eda = eda[(seg - 20): (seg + 20)]
    data_hr = hr[(seg_hr - 5): (seg_hr + 5)]

    #print(data_eda)
    #print(data_hr)

    for x in range(10):
        data.write(
            info[3][-1] + ";"
            + info[4][-1] + ";"
            + str(statistics.mean(data_eda[(x * 4): ((x * 4) + 4)])) + ";"
            + str(data_hr[x]) + ";"
            + class_dimensional.get(int(info[2])) + ";"
            + convert(seg_hr - 5 + x)
            + "\n")

    file_hr.close()
    file_eda.close()

data.close()
resultados.close()