"""
A module for obtaining repo readme and language data from the github API.

Before using this module, read through it, and follow the instructions marked
TODO.

After doing so, run it like this:

    python acquire.py

To create the `data.json` file that contains the data.
"""
import pandas as pd
import os
import json
from typing import Dict, List, Optional, Union, cast
import requests

from env import github_token, github_username

# TODO: Make a github personal access token.
#     1. Go here and generate a personal access token https://github.com/settings/tokens
#        You do _not_ need select any scopes, i.e. leave all the checkboxes unchecked
#     2. Save it in your env.py file under the variable `github_token`
# TODO: Add your github username to your env.py file under the variable `github_username`
# TODO: Add more repositories to the `REPOS` list below.

REPOS = [
    "sherlock-project/sherlock",
    "Greenwolf/social_mapper",
    "bonzanini/Book-SocialMediaMiningPython", 
    "qeeqbox/social-analyzer", 
    "anfederico/stocktalk", 
    "nygardk/react-share", 
    "720kb/angular-socialshare", 
    "msaad1999/KLiK-SocialMediaWebsite", 
    "noizwaves/bootstrap-social-buttons", 
    "Charles042/SocialMedia-App", 
    "lamthuyvo/social-media-data-scripts", 
    "lorey/social-media-profiles-regexs", 
    "emrade/flutter-social", 
    "nprapps/lunchbox", 
    "pablobarbera/social-media-workshop", 
    "konsav/social-icons", 
    "jebmole/SocialMedia", 
    "StevenBlack/hosts", 
    "shamahoque/mern-social", 
    "openstream/open-social-media-monitoring", 
    "carlsednaoui/gitsocial", 
    "ScriptSmith/socialreaper", 
    "richardsonjf/shellphish", 
    "microverseinc/ror-social-scaffold", 
    "PacktPublishing/Python-Social-Media-Analytics", 
    "rixon-cochi/SMF", 
    "antontarasenko/smq", 
    "xbwei/Data-Mining-on-Social-Media", 
    "dbmi-pitt/SocialMediaDataScience", 
    "juanv911/SocialCounters", 
    "dipanjanS/learning-social-media-analytics-with-r", 
    "iatek/jquery-socialist", 
    "schneidmaster/socializer", 
    "JMSCHKU/Social", 
    "feednext/feednext", 
    "540co/yourTwapperKeeper", 
    "Esri/social-media-map-template-js", 
    "CrossGeeks/SocialMediaAuthenticationSample", 
    "vasani-arpit/Social-Media-Automation", 
    "rodrigoprimo/social-connect", 
    "vosonlab/SocialMediaLab", 
    "macx/SocialMediaEnhancer", 
    "janhuenermann/social-circles", 
    "codedamn/social-media-app-ionic4", 
    "shalinguyen/socialicious", 
    "ShekarMudaliyar/social_share", 
    "halolimat/Social-media-Depression-Detector", 
    "vinuthakaranth/SocialMediaAppForFoodies", 
    "zainudinnoori/faceconnect-social-media-application", 
    "the-javapocalypse/Social-Media-Scrapper", 
    "HoussemDellai/social-media-templates", 
    "maurobonfietti/social", 
    "shaikhsajid1111/social-media-profile-scrapers", 
    "Greenwolf/social_attacker", 
    "ozdemirburak/jquery-floating-social-share", 
    "PyThaiNLP/wisesight-sentiment", 
    "hltcoe/golden-horse", 
    "ahm3tcelik/SocialText", 
    "Nick-Gottschlich/Social-Amnesia", 
    "thepanacealab/SMMT", 
    "smpo/socialmedia", 
    "FLiotta/ReactSocial", 
    "andrewkrug/repucaution", 
    "timhuisman/css-social-media-buttons", 
    "chrismaddalena/ODIN", 
    "Data4Democracy/collect-social", 
    "rysmith/hashrobot", 
    "rixon-cochi/hacking-tool", 
    "ColombiaPython/social-media-automation", 
    "emrade/flutter-ghana-ui-challenge-week-1", 
    "nikoma/social_media_monitoring", 
    "zerofox-oss/SNAP_R", 
    "KetaniPhone/SocialMediaLogin", 
    "AnjaliSharma1234/SocialMediaProfileLauncher", 
    "ahmedadeltito/socialmediasignup", 
    "woj-ciech/SocialPath", 
    "tdh8316/Investigo", 
    "bachors/jQuery-Awesome-Sosmed-Share-Button", 
    "HDMA-SDSU/HDMA-SocialMediaAPI", 
    "gdraperi/SocialPath", 
    "ngageoint/social-media-picture-explorer", 
    "espresto/reclaim-social-media", 
    "rifqieh/social-media-app-completed", 
    "BotLibre/BotLibre", 
    "boy-jer/apphera", 
    "palratnesh05/LoginAndRegistrationWithSocialMedia", 
    "aws-samples/finding-missing-persons-using-social-media-and-amazon-rekognition", 
    "karanpratapsingh/Proximity", 
    "andyalam/django_instagram", 
    "mitmedialab/gobo", 
    "ScriptSmith/reaper", 
    "pownjs/whoarethey", 
    "toadlyBroodle/spam-bot-3000", 
    "snarfed/bridgy", 
    "ianozsvald/social_media_brand_disambiguator", 
    "niquejoe/Classification-of-Depression-on-Social-Media-Using-Text-Mining", 
    "abdulisik/Social-Media-Monitor", 
    "Runbhumi/Runbhumi", 
    "dch133/Social-Media-App", 
    "codeforamerica/social-media-handbook", 
    "chrisvxd/og-impact", 
    "SnaxFoundation/snax", 
    "fluquid/extract-social-media", 
    "jlengstorf/get-share-image", 
    "michaelbromley/angular-social-demo", 
    "dan-divy/spruce", 
    "divanov11/Mumble", 
    "nikoma/Old-Apphera-Dashboard", 
    "scalding-io/social-media-analytics", 
    "lrvick/hyve", 
    "httpstersk/social-media-icons", 
    "kayalshri/oauthlogin", 
    "microsoft/is-social", 
    "NHadi/HappySocialMedia", 
    "aronwc/mlsm", 
    "measuredvoice/ringsail", 
    "newscloud/open-social-media-toolkit", 
    "gboeing/social-media", 
    "socialmedia-class/socialmedia-class.github.io", 
    "lancopku/superAE", 
    "ReactNativeSchool/react-native-social-media-app", 
    "Resh1992/User-profiling-in-social-media", 
    "jamesgeorge007/Mini-Social-Media", 
    "loklak/loklak_server", 
    "MLH-Fellowship/Social-BERTerfly", 
    "globocom/share-bar", 
    "DakotaNelson/pushpin-web", 
    "Aravindha1234u/SocialScraper", 
    "ethicalhackingplayground/EvilPhisher", 
    "cyberdh/Text-Analysis", 
    "goshakkk/pabla", 
    "hasanfirnas/deadpool", 
    "dailybruin/meow", 
    "verbb/social-poster", 
    "jubins/MachineLearning-Detecting-Twitter-Bots", 
    "jabranr/socialmedia", 
    "predominant/cake_social", 
    "sr33/ares", 
    "seinecle/Umigon", 
    "vertica/Social-Media-Connector", 
    "AdaGold/react-timeline", 
    "tylersuehr7/social-text-view", 
    "coding-blocks-archives/Social_Media_Sample_Project_2020_May", 
    "OmarElGabry/Hashtegny", 
    "olafsulich/SocialDev-Firebase", 
    "boonebgorges/bp-social-media-profiles", 
    "TianBian95/BiGCN", 
    "wlin12/SMMTT", 
    "wikimedia/mediawiki-extensions-SocialProfile", 
    "glennjones/elsewhere-profiles"]

headers = {"Authorization": f"token {github_token}", "User-Agent": github_username}

if headers["Authorization"] == "token " or headers["User-Agent"] == "":
    raise Exception(
        "You need to follow the instructions marked TODO in this script before trying to use it"
    )


def github_api_request(url: str) -> Union[List, Dict]:
    response = requests.get(url, headers=headers)
    response_data = response.json()
    if response.status_code != 200:
        raise Exception(
            f"Error response from github api! status code: {response.status_code}, "
            f"response: {json.dumps(response_data)}"
        )
    return response_data


def get_repo_language(repo: str) -> str:
    url = f"https://api.github.com/repos/{repo}"
    repo_info = github_api_request(url)
    if type(repo_info) is dict:
        repo_info = cast(Dict, repo_info)
        if "language" not in repo_info:
            raise Exception(
                "'language' key not round in response\n{}".format(json.dumps(repo_info))
            )
        return repo_info["language"]
    raise Exception(
        f"Expecting a dictionary response from {url}, instead got {json.dumps(repo_info)}"
    )


def get_repo_contents(repo: str) -> List[Dict[str, str]]:
    url = f"https://api.github.com/repos/{repo}/contents/"
    contents = github_api_request(url)
    if type(contents) is list:
        contents = cast(List, contents)
        return contents
    raise Exception(
        f"Expecting a list response from {url}, instead got {json.dumps(contents)}"
    )


def get_readme_download_url(files: List[Dict[str, str]]) -> str:
    """
    Takes in a response from the github api that lists the files in a repo and
    returns the url that can be used to download the repo's README file.
    """
    for file in files:
        if file["name"].lower().startswith("readme"):
            return file["download_url"]
    return ""


def process_repo(repo: str) -> Dict[str, str]:
    """
    Takes a repo name like "gocodeup/codeup-setup-script" and returns a
    dictionary with the language of the repo and the readme contents.
    """
    contents = get_repo_contents(repo)
    readme_download_url = get_readme_download_url(contents)
    if readme_download_url == "":
        readme_contents = ""
    else:
        readme_contents = requests.get(readme_download_url).text
    return {
        "repo": repo,
        "language": get_repo_language(repo),
        "readme_contents": readme_contents,
    }


def scrape_github_data() -> List[Dict[str, str]]:
    """
    Loop through all of the repos and process them. Returns the processed data.
    """
    return [process_repo(repo) for repo in REPOS]


if __name__ == "__main__":
    data = scrape_github_data()
    json.dump(data, open("data.json", "w"), indent=1)
