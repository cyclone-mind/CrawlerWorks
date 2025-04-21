import subprocess

def forward_port():
    subprocess.getoutput("adb forward tcp:27042 tcp:27042")
    subprocess.getoutput("adb forward tcp:27043 tcp:27043")

if __name__ == '__main__':
    forward_port()