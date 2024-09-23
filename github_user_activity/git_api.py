import os
import http.client
import json


class USER:
    def __init__(self) -> None:
        self.api_url_git = "api.github.com"

    def get_events(self, username):
        # conexao
        connect = http.client.HTTPSConnection(self.api_url_git)

        # hearders
        headers = {"User-Agent": "Python Script"}

        # requisicao
        connect.request(
            "GET", f"https://api.github.com/users/{username}/events", headers=headers
        )

        # dados
        response = connect.getresponse()

        if response.status == 200:
            data = response.read()
            events = json.loads(data.decode())

            # retorna dados
            return events

        else:
            print(
                f"\nRequest failed: {response.status} {response.reason}\ncheck if the username was typed wrong \n"
            )


    def show_events(self,events):
         if events:
         
            for event in events:
                event_type = event['type']
                repo_name = event['repo']['name']

                if event_type == "PushEvent":
                    commits = len(event['payload']['commits'])
                    print(f"- Pushed {commits} commits to {repo_name}")
                
                elif event_type == "IssuesEvent":
                    action = event['payload']['action']
                    print(f"- Opened a new issue in {repo_name}")
                
                elif event_type == "WatchEvent":
                    print(f"- Starred {repo_name}")
