import speedtest

def teste():
    speed=speedtest.Speedtest()
    download= f"{'{:.2f}'.format(speed.download()/1024/1024)} Mb/s"
    upload= f"{'{:.2f}'.format(speed.upload()/1024/1024)} Mb/s"
    print(download,upload)


speed=speedtest.Speedtest()
download= f"{'{:.2f}'.format(speed.download()/1024/1024)} Mb/s"
upload= f"{'{:.2f}'.format(speed.upload()/1024/1024)} Mb/s"
print(download,upload)

