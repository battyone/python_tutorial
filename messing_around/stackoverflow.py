import pandas as pd


def download_survey():
    import os
    import shutil
    import zipfile
    import requests

    # https://insights.stackoverflow.com/survey
    request = requests.get(
        "https://drive.google.com/uc?export=download&id=1_9On2-nsBQIw3JiY43sWbrF8EjrqrR4U")

    with open("survey.zip", "wb") as file:
        file.write(request.content)

    with zipfile.ZipFile("survey.zip") as zip:
        zip.extractall("survey")

    shutil.move("survey/survey_results_public.csv", "mysurvey.csv")
    shutil.rmtree("survey")
    os.remove("survey.zip")


if __name__ == "__main__":
    # download_survey()

    totals = {}
    data = pd.read_csv("mysurvey.csv", encoding="latin1")

    print(data.size)
