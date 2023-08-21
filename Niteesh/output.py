import os
import pandas as pd

dir_path = "C:/Log Analysis/Input"

file_list = [file for file in os.listdir(dir_path) if (".log") in file]

for file in file_list:
    data = []
    with open(os.path.join(dir_path, file), "r") as f:
        for line in f:
            l = line.strip().split(" ")
            l = [i.replace('[','').replace(']','') for i in l]
            if len(l) > 3:
                date = l[0]
                time = l[1]
                status = l[2]
                message = " ".join(l[3:])
                data.append([date, time, status, message])

        df = pd.DataFrame(data, columns=["date", "time", "status", "message"])

        warning = df[df["status"]=="WARN"]
        error = df[df["status"]=="ERROR"]
    
    path = f"C:/Log Analysis/Output/{file}.xlsx"
    with pd.ExcelWriter(path) as s:
        error.to_excel(s, sheet_name='error')
        warning.to_excel(s, sheet_name='warning')







