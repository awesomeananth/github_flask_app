from num2words import num2words
import requests
import pandas

def get_input(text):
    return input(text)


def get_user_input():
    repo_list = []
    repo_count = get_input("Please enter the number of repositories for which you want to see stargazer count: ")
    while repo_count.isdigit() != True:
        repo_count = get_input("It's not an Integer value!!, Please enter the number of repositories for which you want to see stargazer count: ")
    for num, count in enumerate(range(int(repo_count))):
        repo = get_input("Please Enter %s repository in format organization/repository: "%num2words(num+1, to="ordinal_num"))
        while '/' not in repo:
            repo = get_input("You need to Enter details in organization/repository format, Lets try once again \nPlease Enter %s repository in format organization/repository: "%num2words(num+1, to="ordinal_num"))
        repo_list.append(repo)
    data = {"repository_name": repo_list}
    try:
        stargazer_api_resp = requests.post(url="http://0.0.0.0:5000/post", json=data)
        if stargazer_api_resp.status_code == 200:
             df = pandas.DataFrame(stargazer_api_resp.json())
             print(df)
             return stargazer_api_resp.status_code
        elif stargazer_api_resp.status_code == 403:
             print('API rate limit exceeded')
        elif stargazer_api_resp.status_code == 404:
             print('Error 404: Repo not found')
        elif stargazer_api_resp.status_code == 500:
             print('Error 500: Internal Server Error')
    except Exception as e:
        print(e)


get_user_input()
