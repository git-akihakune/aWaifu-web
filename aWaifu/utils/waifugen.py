import os
import json
import base64
import tempfile
from aWaifu.utils import Waifus


def generate(
    numberOfProfiles: int = 4,
    multiCultures: bool = True,
    bigWaifu: bool = False,
    faster: bool = False,
    verbose: bool = False
) -> dict:

    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        if verbose: print(f"[-] Working at {os.getcwd()}")
        waifuGen = Waifus(
            numberOfProfiles=numberOfProfiles,
            multiCultures=multiCultures,
            bigWaifu=bigWaifu,
            faster=faster,
            verbose=False,
        )

        waifuGen.generateProfiles()
        if verbose: print(f"[!] Successfully init waifuGen object, getting data from {os.path.join(os.getcwd(), waifuGen.dataPath)}")
        data = _readProfiles(waifuGen.dataPath)

        # Update images to base64 encode of generated images
        for profile in data:
            with open(profile['image'], 'rb') as imageFile:
                profile['image'] = base64.b64encode(imageFile.read()).decode('utf-8')
                
        waifuGen.cleanUpPreviousRuns()
        if verbose: print("[-] All data cleaned up.")

    return data
    

def _readProfiles(dataPath:str) -> dict:
    profilePath:str = os.path.join(dataPath, 'profile.json')
    with open(profilePath, 'r') as profileFile:
        data = json.load(profileFile)
    for entry in data:
        entry.pop('representative_color', None) # remove not-suitable field
    return data