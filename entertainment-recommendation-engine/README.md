## 🎬🎵 Entertainment Recommendation Engine

A Python-based terminal application that helps users discover, favorite, and manage **movies** and **music** through real-time APIs and personalized recommendations.

Built using Python and powered by the OMDb and Last.fm APIs.


## 🚀 Features

- 🔍 **Search Movies** using the OMDB API
- 🎵 **Search Music** using the Last.fm API
- ❤️ **Add to Favorites** and manage your movie/music collections
- 🤖 **Personalized Recommendations** based on your preferences
- 🧑‍🤝‍🧑 **Find Similar Users** and see their unique picks
- 📊 **View Your Profile** with stats, genre trends & achievements
- 💾 **Auto-saves user data** locally via `user_profile.json`

## 🛠️ Technologies Used

* Python 3
* OMDb API
* Last.fm API
* JSON for persistent user data

## 📦 Installation

1. **Clone the repository**

->**    **git clone https://github.com/Aakash315/python-learning/entertainment-recommendation-engine.git

->**    **cd entertainment-recommendation-engine

2. **Install dependencies**

(Requires requests library)

->**    **pip install requests

3. **Run the App**

->**    **python project.py

## **🔑 API Keys Required**

To use the app, you'll need to register for:

* OMDb API Key from http://www.omdbapi.com/apikey.aspx
* Last.fm API Key from https://www.last.fm/api/account/create

**Replace the default placeholders in the code:**

** **-> api_key = 'YOUR_OMDB_API_KEY'

** **-> api_key = 'YOUR_LASTFM_API_KEY'

## **👥 User Flow**

1. Register or login to your profile.
2. Search for movies or songs to add to your favorites.
3. Get curated recommendations based on your genre preferences.
4. View your profile, track achievements, and find users with similar tastes.

## 🏆 Achievements

Movie Buff: Add 10+ favorite movies

Music Lover: Add 15+ favorite songs


## 📁 File Structure


📦 entertainment-recommendation-engine
├── main.py                  # Entry point & all features
├── user_profile.json        # Auto-saved user data
└── README.md                # This documentation🙌 Acknowledgements


## 🧠 How It Works

* Movie and music data is fetched using  **real-time APIs** .
* Favorite items are stored in a JSON file locally.
* Recommendations are calculated based on  **genre overlap** ,  **listening/viewing patterns** , and **shared interests** with other users.
