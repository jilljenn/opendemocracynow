import csv
def get_profile(user):
    vote = []
    with open('votes.csv', 'r', encoding='utf-8') as f:
        db = csv.DictReader(f, delimiter='\t')
        for row in db:
            if row['username'] == user:
                vote.append([row['vote'], row['article_link']])
    return vote

print(get_profile("vincentreverdy"))

