from movies import get_movies
from tweet import send_tweet,send_tweet_fake
import json

import urllib.request




def update():
    db=open('movies.json','r+')
    
    new_movies=get_movies()
    movies=[]

    if(db.read()==""):
        print("DB is empty")
        db.seek(0)
        db.write(json.dumps(new_movies))
        return
    else:
        db.seek(0)

        movies=json.loads(db.read())
    
    if(movies[0]!=new_movies[0]):
        db.seek(0)
        db.write(json.dumps(new_movies))
        movie=new_movies[0]
        message="{} releasing on {} \n date : {} \n ".format(movie['name'],movie['platforms'],movie['date'])
        urllib.request.urlretrieve(movie['image'],'temp.jpg')
        send_tweet(message)

    else:
        print('No Difference')
    db.close()


if __name__=="__main__":
    update()