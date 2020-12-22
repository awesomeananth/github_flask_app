from num2words import num2words
import requests
import pandas
import sys


def get_user_input():
    #import pdb; pdb.set_trace()
    repo_list = sys.argv[1:]
    print (repo_list)
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
    except requests.exceptions.Timeout:
        print ('Error: Connection Timeout')
    except requests.exceptions.TooManyRedirects:
        print ('Error: Too Many Redirects')
    except Exception as e:
        print(e)


get_user_input()
