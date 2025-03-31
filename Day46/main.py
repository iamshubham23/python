import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
# Client_Id="1c6379ff8de74437aaf96ccd0133db84"
# Client_Secret="7cd62711c87d4a1ea185e1875b3bd372"
# URL="https://www.billboard.com/charts/hot-100/"
user_choice=input("which year do you want to travel yyyy-mm-dd:" )
response=requests.get("https://www.billboard.com/charts/hot-100/"+user_choice)

soup=BeautifulSoup(response.text,"html.parser")
songs_names_span=soup.select("li ul li h3")
song_names=[song.getText().strip() for song in songs_names_span]
print(song_names)

OAUTH_TOKEN_URL="https://accounts.spotify.com/api/token"
sp=spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        Client_Id="1c6379ff8de74437aaf96ccd0133db84",
        Client_Secret="7cd62711c87d4a1ea185e1875b3bd372",
        redirect_uri="http://example.com",
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt"
    )   

)
user_id=sp.current_user()["id"]