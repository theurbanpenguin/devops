import redis

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

def update_score(user, score):
    r.zadd('leaderboard', {user: score})

def get_leaderboard():
    return r.zrevrange('leaderboard', 0, -1, withscores=True)

# Update scores
update_score('Alice', 100)
update_score('Bob', 150)
update_score('Charlie', 120)

# Get leaderboard
leaderboard = get_leaderboard()
print("Leaderboard:")
for user, score in leaderboard:
    print(f"{user.decode('utf-8')}: {score}")
