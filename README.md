# 🎵 Billboard to Spotify Playlist Generator

A Python project that scrapes the **Billboard Hot 100** chart for a given date and automatically creates a **Spotify playlist** with those songs.  

Perfect for traveling back in time musically ⏳🎶  

---

## ✨ Features
- Scrapes **Billboard Hot 100** using BeautifulSoup.
- Uses **Spotify Web API** (via Spotipy) to search and match songs.
- Creates a **private Spotify playlist** with the top 100 tracks from that date.
- Handles API authentication with **OAuth 2.0**.
- Adds tracks in batches (Spotify’s 100-song limit per request).

---

## 🚀 Setup

### 1. Clone the repo
```bash
git clone https://github.com/Unnathie/Billboard-to-Spotify-Playlist-Generator.git
cd Billboard-to-Spotify-Playlist-Generator
````

### 2. Create a virtual environment (recommended)

```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install requests
pip install spotipy
pip install bs4
```

### 4. Spotify Developer App

1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
2. Create a new app.
3. Add the redirect URI:

   ```
   http://127.0.0.1:9090/callback
   ```
4. Copy your **Client ID** and **Client Secret**.

### 5. Environment variables

Create a `.env` file in the project root:

```
CLIENT_ID=your_spotify_client_id
SECRET=your_spotify_client_secret
```
---

## ▶️ Usage

Run the script:

```bash
python main.py
```

Enter a date in the format `YYYY-MM-DD`:

```
Which year do you want to musically travel to? Type the date in this format YYYY-MM-DD: 2002-07-08
```

✅ The script will:

* Scrape Billboard Hot 100 for that date.
* Search each track + artist on Spotify.
* Create a playlist in your Spotify account.
* Print a link to the new playlist.

---

## 📂 Example Output
![Untitled design (8)](https://github.com/user-attachments/assets/c6025bf0-8cc3-4d74-85ed-b2d50531580d)

```
Your Spotify username (id) is: 31ofczpdzugsr5bnyy4m2iigk7m4
✓ Found: Hot In Herre — Nelly
✓ Found: Without Me — Eminem
...
Created playlist: https://open.spotify.com/playlist/XXXXXXXXXXXX
✅ Playlist complete!
```

---

## ⚠️ Notes

* Some tracks may not be found (due to covers, remixes, missing metadata).
* A `not_found.txt` can be added to log missing songs.
* Requires a free [Spotify Developer account](https://developer.spotify.com/).

---

## 🛠️ Tech Stack

* [Python](https://www.python.org/)
* [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)
* [Spotipy](https://spotipy.readthedocs.io/en/latest/)
* [Requests](https://docs.python-requests.org/en/latest/)

---

## 📜 License

This project is licensed under the MIT License.
Feel free to fork, modify, and enjoy! 🎧

```
