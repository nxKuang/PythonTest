# Add your code here to run in your startup task
from datetime import datetime
import subprocess
import os.path
datestamp = datetime.now().strftime("%Y%m%d")
game_path = "H:\Game\wow\WTF\Account\KUANGNX\\"
archive_path = "H:\Game\wow\WTF\wow_account_archive\\"
filename = archive_path+"KUANGNX_"+datestamp+".rar"
if not os.path.isfile(filename):
    subprocess.call(["rar","a","-r",filename,game_path])

def main():
    for i in range(10000):
        s = make_dot_string(i)
        print(s)

if __name__ == "__main__":
    sys.exit(int(main() or 0))

