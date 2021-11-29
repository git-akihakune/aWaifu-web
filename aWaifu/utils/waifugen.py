import os
import json
import base64
from aWaifu.utils import Waifus


def generate(
    numberOfProfiles: int = 4,
    multiCultures: bool = True,
    bigWaifu: bool = False,
    faster: bool = False,
    verbose: bool = False
) -> dict:

    waifuGen = Waifus(
        numberOfProfiles=numberOfProfiles,
        multiCultures=multiCultures,
        bigWaifu=bigWaifu,
        faster=faster,
        verbose=False,
    )

    waifuGen.generateProfiles()
    if verbose:
        print(f"[!] Successfully init waifuGen object, getting data from {waifuGen.dataPath}")
    data = _readProfiles(waifuGen.dataPath)

    # Update images to base64 encode of generated images
    for profile in data:
        with open(profile['image'], 'rb') as imageFile:
            profile['image'] = base64.b64encode(imageFile.read()).decode('utf-8')
            
    waifuGen.cleanUpPreviousRuns()

    return data
    

def _readProfiles(dataPath:str) -> dict:
    profilePath:str = os.path.join(dataPath, 'profile.json')
    with open(profilePath, 'r') as profileFile:
        data = json.load(profileFile)
    return data