import csv
from collections import Counter
from knn import MangakiKNN
import json

with open('votes.csv', newline='') as csvfile:
    votes = csv.reader(csvfile, delimiter='\t', quotechar='"')

    articles_by_url = {}
    article_id = 0

    users_by_username = {}
    users = {}
    user_id = 0

    articles = {}

    for row in list(votes)[1:]:
        # Lire la ligne
        article_title, username, user_profile, vote_type, article_link, vote, date = row

        # Si cet article n'a jamais été vu, ça lui attribue un numéro
        if article_link not in articles_by_url:
            article_id += 1
            articles_by_url[article_link] = article_id

        # Idem pour l'utilisateur
        if username not in users_by_username:
            user_id += 1
            users_by_username[username] = user_id
            users[user_id] = username

        # On inscrit la paire (article_id, vote)
        articles.setdefault(user_id, []).append((article_id, vote))

    rating_values = {
        '1': 1,
        '-1': 1,
        '0': -1
    }

    nb_votes = Counter()

    X = []
    y = []
    for user_id in articles:
        nb_votes[user_id] = len(articles[user_id])
        for article_id, vote in articles[user_id]:
            X.append((user_id, article_id))
            y.append(rating_values[vote])

    for user_id, nb in nb_votes.most_common(5):
        print(users[user_id], nb)

    algo = MangakiKNN()
    algo.fit(X, y)
    
    """neighbors = algo.get_neighbors(users_by_username['vincentreverdy'])
    print(list(map(lambda user_id: users[user_id], neighbors)))"""

    neighbors = {}

    print('%d utilisateurs, %d articles' % (len(users), len(articles_by_url)))

    for user_id in users:
        neighbors[users[user_id]] = list(map(lambda user_id: users[user_id], algo.get_neighbors(user_id)))

    with open('neighbors.json', 'w') as f:
        f.write(json.dumps(neighbors))
