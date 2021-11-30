#!/usr/bin/env python3

# Example API client
# Author: Aki Hakune
# Date: 2021-11-30

### Variables ###
host = "http://127.0.0.1:5000"
endpoint = "/api/profile"
apiKey = "test"
numberOfProfiles = 1
multiCultures = False
bigWaifu = False
faster = False
verbose = True
#################

import requests
import tempfile
import base64
import json
from typing import Dict


def save(data: Dict[str, str]) -> None:
    """Save the data to a file"""
    dirPath: str = tempfile.mkdtemp()
    log(f"[-] Saving data to {dirPath}")

    rawData: str = data["data"]
    for profile in rawData:
        log(f"[-] Saving {profile['name']}")
        with open(f"{dirPath}/{profile['name']}.png", "wb") as f:
            f.write(base64.b64decode(profile["image"]))
        log(f"[-] Saved {profile['name']}")

        profile.pop('image', None)
        log(f"Removed image key for {profile['name']}")

    log(f"[+] Saved all images to {dirPath}")
    
    log(f"[-] Saving profile details to {dirPath}/profile.json")
    with open(f"{dirPath}/profile.json", "w") as profileFile:
        json.dump(rawData, profileFile, ensure_ascii=False, indent=4)
    log(f"[+] Profile details saved")

    print(f"[+] Saved all data to {dirPath}")


def log(message):
    if verbose:
        print(message)


if __name__ == "__main__":
    # Create a dictionary with the data
    postData = {
        "api_key": apiKey,
        "number_of_profiles": numberOfProfiles,
        "multi_cultures": multiCultures,
        "big_waifu": bigWaifu,
        "faster": faster,
    }

    # Call the API
    log(f"[-] Sending data to {host}{endpoint}")
    response = requests.post(host + endpoint, data=postData)
    data = response.json()
    log(f"[+] Data received successfully")

    if data["status"] != "success":
        print("Error: " + data["message"])
        exit(1)

    save(data)