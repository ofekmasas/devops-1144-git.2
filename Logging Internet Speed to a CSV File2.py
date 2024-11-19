import os
import speedtest
import datetime
import time

#ping=speedtest.Speedtest.ping    

def Logging_Internet_Speed_to_a_CSV_File(filepath):
    if not os.path.exists(filepath):
        filepath= open(filepath,'x')
        filepath=open(filepath,'a')
        filepath.write("Timestamp,Download Speed (Mbps),Upload Speed (Mbps)\n")
    else:
        filepath=open(filepath,'a') 

    counter=0
    while True:
        st = speedtest.Speedtest()
        st.get_best_server()
        download=round(st.download() / 1000000, 2)
        upload=round(st.upload() / 1000000 , 2)
        filepath.write(f"{datetime.datetime.now()},{str(download)},{str(upload)}\n")
        counter+=1
        print(f"cycle: {counter}\ndownload: {download}\nupload: {upload}")
        time.sleep(5)

Logging_Internet_Speed_to_a_CSV_File('speed log.csv')


