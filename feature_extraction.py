import statistics
from scipy.stats import linregress
import numpy as np

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

data = open('./all_features.csv', "w")
data.write("registro;eda_mean;eda_std;percentile_20;percentile_80;quartile_deviation;slope;intercept;hr_mean;hr_std;quartile_deviation;slope;intercept;class\n")
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

    #print(len(data_eda))
    #print(data_hr)

    slope_eda = list(linregress(list(range(41))[-40:], data_eda))
    slope = list(linregress(list(range(11))[-10:], data_hr))

    data.write(
        info[0] + ";"
        + str(statistics.mean(data_eda)) + ";" + str(statistics.stdev(data_eda)) + ";"
        + str(np.percentile(data_eda, 20)) + ";" + str(np.percentile(data_eda, 80)) + ";" + str(np.percentile(data_eda, 75) - np.percentile(data_eda, 25)) + ";" + str(slope_eda[0]) + ";" + str(slope_eda[1]) + ";"
        + str(statistics.mean(data_hr)) + ";" + str(statistics.stdev(data_hr)) + ";"
        + str(np.percentile(data_hr, 75) - np.percentile(data_hr, 25)) + ";" + str(slope[0]) + ";" + str(slope[1]) + ";"
        + info[2]
        + "\n")

    file_hr.close()
    file_eda.close()

data.close()
resultados.close()