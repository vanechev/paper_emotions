resultados = open('../observaciones.csv')
datos = resultados.read()

new_resultados = open('observaciones.csv', "w")

def get_clase(emo):
    if(emo in ["tense","stressed"]):
        return 1
    elif(emo in ["happy","exalted"]):
        return 2
    elif(emo in ["depressed","boring"]):
        return 3
    elif(emo in ["calmed","serene"]):
        return 4
    return emo

def get_time(time):
    array_time = time.split(":")
    return (int(array_time[0]) * 60) + int(array_time[1]) 

i = 0;
for dato in datos.split("\n"):
    info = dato.split(";")
    get_time(info[0])
    if(info[4]):
        i = i + 1;
        new_resultados.write(str(i) + ";" + str(get_time(info[0])) + ";" + str(get_clase(info[4])) + ";" + "group" + info[3] + ";" + "R1" + "\n")
    if(info[5]):
        i = i + 1;
        new_resultados.write(str(i) + ";" + str(get_time(info[0])) + ";" + str(get_clase(info[5])) + ";" + "group" + info[3] + ";" + "R2" + "\n")
    if(info[6]):
        i = i + 1;
        new_resultados.write(str(i) + ";" + str(get_time(info[0])) + ";" + str(get_clase(info[6])) + ";" + "group" + info[3] + ";" + "R3" + "\n")
    if(info[7]):
        i = i + 1;
        new_resultados.write(str(i) + ";" + str(get_time(info[0])) + ";" + str(get_clase(info[7])) + ";" + "group" + info[3] + ";" + "R4" +  "\n")

resultados.close()
new_resultados.close()