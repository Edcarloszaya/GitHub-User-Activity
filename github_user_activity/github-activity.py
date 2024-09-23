import argparse
from github_user_activity.git_api import USER

parser = argparse.ArgumentParser(description="Github-activity")
parser.add_argument("Username", type=str, help="Username from the git  ")

args = parser.parse_args()
user_name = args.Username

# instacia a classe 
user_api = USER()

if user_name:
    events = user_api.get_events(user_name)
    user_api.show_events(events)





