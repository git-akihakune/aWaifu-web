import waifulabs
import time
import os
import requests
import shutil
import json
import random
from .config import RACE_NAMES
from typing import Dict


class Waifus:
    def __init__(
        self,
        dataPath: str = "waifus/",
        numberOfProfiles: int = 10,
        verbose: bool = False,
        multiCultures: bool = True,
        bigWaifu: bool = False,
        faster: bool = False,
    ):
        self.dataPath = dataPath if dataPath[-1] == "/" else dataPath + "/"
        self.numberOfProfiles: int = numberOfProfiles
        self.verbose = verbose
        self.multiCultures = multiCultures
        self.bigWaifu = bigWaifu
        self.timeLimitBreak = faster

    def cleanUpPreviousRuns(self) -> None:
        """Delete data from previous executions"""
        defaultDataDir: str = self.dataPath
        shutil.rmtree(defaultDataDir, ignore_errors=True)

    def download(self) -> None:
        """Download every generated information under zipped format"""
        try:
            dataPathName: str = self.dataPath - '/'
            shutil.make_archive(dataPathName, "zip", dataPathName)
            print(f"Files successfullly archived in '{dataPathName}.zip'")
        except FileNotFoundError:
            print("Please make sure that you have generated 'waifus' directory first.")
            return None

    @staticmethod
    def getRandomAge() -> None:
        """Generate completely random age"""
        return random.choice(
            [
                random.randint(3, 25),  # age of human waifu
                random.randint(10 ** 3, 10 ** 5),  # age of non-human waifu
            ]
        )

    @staticmethod
    def getRandomRace(age: int) -> str:
        """Randomizing a race"""
        humanHighestAge: int = 25

        NON_HUMAN_RACES = RACE_NAMES

        if age > humanHighestAge:
            return random.choice(NON_HUMAN_RACES)

        return random.choice(["Human", random.choice(NON_HUMAN_RACES)])

    def _vbose(self, contextType: str, context) -> None:
        """Logging, verbose messages and image showing"""
        if self.verbose:
            if contextType == "text":
                print(context, end="\n")
            elif contextType == "dictionary":
                print(json.dumps(context, indent=4, ensure_ascii=False))
                print()
            else:
                print(f"Unknown type logging: {context}")

    def _getRandomProfile(self, imagePath: str):
        """Generate random profile"""

        profileDataPath: str = self.dataPath + "profile.json"

        # Using free, no-authentication Name Fake API
        apiHost: str = "https://api.namefake.com"

        if self.multiCultures:
            endPoint: str = apiHost + "/random/female"
        else:
            endPoint: str = apiHost + "/japanese-japan/female"

        call = requests.get(endPoint)
        rawData = call.json()

        # Because randomizing race depends on life span
        waifuAge = self.getRandomAge()
        waifuRace = self.getRandomRace(waifuAge)

        waifuData: Dict[str:str] = {
            "image": imagePath,
            "name": rawData["name"],
            "code_name": rawData["email_u"],
            "age": waifuAge,
            "race": waifuRace,
            "current_location": rawData["address"].replace("\n", " "),
            "birthday": rawData["birth_data"][5:],
            "representative_color": rawData["color"],
            "blood_type": rawData["blood"],
        }

        self._vbose("dictionary", waifuData)

        with open(profileDataPath, "a+") as f:
            f.write(json.dumps(waifuData, indent=4, ensure_ascii=False))
            f.write("\n\n\n")

    def _getRandomImages(self, filename: str) -> None:
        """Getting waifu images from waifulabs"""

        if self.bigWaifu:
            waifu = waifulabs.GenerateWaifu().GenerateBigWaifu()
        else:
            waifu = waifulabs.GenerateWaifu()

        waifu.save(self.dataPath + filename)
        self._vbose("text", f"Image generated at {self.dataPath + filename}")

    def generateProfiles(self) -> None:
        """Generate full waifu profiles"""

        # Set up data directory the first run
        if not os.path.isdir(self.dataPath):
            os.mkdir(self.dataPath)

        for i in range(self.numberOfProfiles):
            self._vbose("text", f"ID: {i + 1}/{self.numberOfProfiles}\n")

            if not self.timeLimitBreak:
                time.sleep(0.75)  # try not to DOS Waifulab's servers