import csv
import jinja2
import json

with open('neighbors.json') as f:
    neighbors = json.load(f)

def get_votes(username):
    votes = []
    with open('votes.csv', 'r', encoding='utf-8') as f:
        db = csv.DictReader(f, delimiter='\t')
        for row in db:
            if row['username'] == username:
                votes.append([row['article_title'], row['article_link'], row['vote']])
    return votes

def get_neighbors(username):
    return neighbors[username]

def make_profile(username):
    votes = get_votes(username)
    neighbors = get_neighbors(username)
    with open('web/profile/%s.html' % username, 'w') as f:
        f.write(jinja2.Template(open('profile.html').read()).render({'votes': votes, 'neighbors': neighbors}))


# make_profile("vincentreverdy")
usernames = ["reyrobert", "meyermichel", "emmameunier", "brohanmickael", "alexmaluhia", "laurent6", "voltz", "dangienarnaud", "hersonjerome", "danielgohaud", "pierreemmanuelgr", "amenysbentabak", "johnrose", "hugoblanzat", "cedricblanchard"]
for username in usernames:
    print(make_profile(username))