import json
from os import environ
from ast import literal_eval
from datetime import datetime
from utils.config import validatorToolbox
from utils.shared import loadVarFile, stringStars
from utils.toolbox import shardStats
from subprocess import PIPE, run

if __name__ == "__main__":
    loadVarFile()
    timeNow = datetime.now()
    ourShard = environ.get("SHARD")
    ourNetwork = environ.get("NETWORK_SWITCH")
    remote_shard_0 = [f'{validatorToolbox.hmyAppPath}', 'blockchain', 'latest-headers', f'--node=https://api.s0.{ourNetwork}.hmny.io']
    result_remote_shard_0 = run(remote_shard_0, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    remote_data_shard_0 = json.loads(result_remote_shard_0.stdout)
    remote_shard = [f'{validatorToolbox.hmyAppPath}', 'blockchain', 'latest-headers', f'--node=https://api.s{ourShard}.{ourNetwork}.hmny.io']
    try:
        result_remote_shard = run(remote_shard, stdout=PIPE, stderr=PIPE, universal_newlines=True)
        remote_data_shard = json.loads(result_remote_shard.stdout)
    except (ValueError, KeyError, TypeError):
        print(f'Remote API not responding')
        raise SystemExit(0)
    local_shard = [f'{validatorToolbox.hmyAppPath}', 'blockchain', 'latest-headers']
    try:
        result_local_shard = run(local_shard, stdout=PIPE, stderr=PIPE, universal_newlines=True)
        local_data_shard = json.loads(result_local_shard.stdout)
    except (ValueError, KeyError, TypeError):
        print(f'Local client not running')
        raise SystemExit(0)
    
    # print out
    
    if int(ourShard) > 0:
        print(f"""
    {stringStars()}
    * Current Date & Time: {timeNow}
    *
    {stringStars()}
    * Current Status of our server {validatorToolbox.serverHostName} currently on Shard {environ.get('SHARD')}:
    *
    * Shard 0 Sync Status:
    * Local Server  - Epoch {local_data_shard['result']['beacon-chain-header']['epoch']} (Always 1 epoch behind Remote Server) - Shard 0 not required on Shard {environ.get('SHARD')}
    * Remote Server - Epoch {remote_data_shard_0['result']['shard-chain-header']['epoch']} - Shard {remote_data_shard_0['result']['shard-chain-header']['shardID']} - Block {literal_eval(remote_data_shard_0['result']['shard-chain-header']['number'])}
    *
    {stringStars()}
    """)
    else:
        print(f"""
    {stringStars()}
    * Current Date & Time: {timeNow}
    *
    {stringStars()}
    * Current Status of our server {validatorToolbox.serverHostName} currently on Shard {environ.get('SHARD')}:
    *
    * Shard 0 Sync Status:
    * Local Server  - Epoch {local_data_shard['result']['beacon-chain-header']['epoch']} - Shard {local_data_shard['result']['beacon-chain-header']['shardID']} - Block {literal_eval(local_data_shard['result']['beacon-chain-header']['number'])}
    * Remote Server - Epoch {remote_data_shard_0['result']['shard-chain-header']['epoch']} - Shard {remote_data_shard_0['result']['shard-chain-header']['shardID']} - Block {literal_eval(remote_data_shard_0['result']['shard-chain-header']['number'])}
    *
    {stringStars()}
    """)

    shardStats(ourShard)