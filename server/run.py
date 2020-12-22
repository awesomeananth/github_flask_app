from flask import Flask, request, jsonify
from github import Github

app = Flask(__name__)

@app.route('/post', methods=['POST'])
def github_startgazers_count():
    if request.method == 'POST':
        data = request.get_json(force=True)
        repo_list = data['repository_name']
        app.logger.info(repo_list)
        stgazer_count_list = req_response_arch(repo_list)
        d = {'Repository Name' : repo_list, 'Stargazer Count' : stgazer_count_list}
        app.logger.info(d)
        return jsonify(d)



def req_response_arch(repo_list):
    stgazer_list = []
    ins = Github()
    for repo in repo_list:
        try:
             res = ins.get_repo(repo)
             stgazer_count = res.stargazers_count
        except Exception as e:
            #TODO: Additional exceptions for 200,404,500
           app.logger.error(e)
           #app.logger.info(e.status_code)
           stgazer_count = 'Repository not Found'
        stgazer_list.append(stgazer_count)
    return stgazer_list




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
