import subprocess
import json


command = '/Users/mischelle.massey/Desktop/Jupyter lab/Blockchain Tools/wallet/hd-wallet-derive/derive -g --mnemonic="order arrange soup change add security mouse emerge else erase puzzle stick" --cols=path,address,privkey,pubkey -g --format=json'

p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
p_status = p.wait()


keys=json.loads(output)
print(keys)

