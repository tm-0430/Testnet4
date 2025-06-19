import subprocess
import json
import time

FAUCET_AMOUNT = 100000  # in satoshis (e.g., 0.001 tBTC)
COOLDOWN = 24 * 3600  # 24 hours in seconds
last_request_time = {}

def rpc_call(method, params=[]):
    cmd = ['bitcoin-cli', '-testnet', method] + params
    result = subprocess.run(cmd, capture_output=True, text=True)
    return json.loads(result.stdout)

def send_faucet(address):
    now = time.time()
    if address in last_request_time and now - last_request_time[address] < COOLDOWN:
        print("Cooldown active. Please wait before requesting again.")
        return

    # Construct and send transaction logic here
    # This involves listing UTXOs, creating raw transaction, signing, and sending it
    # For brevity, pseudo-steps:
    # 1. List unspent outputs
    # 2. Create raw transaction to send FAUCET_AMOUNT to address
    # 3. Sign raw transaction
    # 4. Send raw transaction

    print(f"Sending {FAUCET_AMOUNT} sats to {address}")
    last_request_time[address] = now

if __name__ == "__main__":
    user_address = input("Enter your Testnet4 address: ")
    send_faucet(user_address)
