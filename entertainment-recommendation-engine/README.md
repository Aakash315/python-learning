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

   ->   git clone https://github.com/Aakash315/python-learning.git

   ->   cd python-learning/entertainment-recommendation-engine
2. **Install dependencies**

(Requires requests library)

    ->    pip install requests

3. **Run the App**

   ->   python project.py

## **🔑 API Keys Required**

To use the app, you'll need to register for:

* OMDb API Key from http://www.omdbapi.com/apikey.aspx
* Last.fm API Key from https://www.last.fm/api/account/create

**Replace the default placeholders in the code:**

 ->    api_key = 'YOUR_OMDB_API_KEY'

 ->    api_key = 'YOUR_LASTFM_API_KEY'

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

├── project.py                  # Entry point & all features

├── user_profile.json        # Auto-saved user data

└── README.md                # This documentation🙌 Acknowledgements

## 🧠 How It Works

* Movie and music data is fetched using  **real-time APIs** .
* Favorite items are stored in a JSON file locally.
* Recommendations are calculated based on  **genre overlap** ,  **listening/viewing patterns** , and **shared interests** with other users.


## Menu Options and Expected Outputs

### Main Menu Interface

=== ENTERTAINMENT RECOMMENDATION ENGINE ===

1. Search Movies
2. Search Music
3. Add to Favorites
4. Get Movie Recommendations
5. Get Music Recommendations
6. View Profile
7. Find Similar Users
8. Exit

Choose an option:


**Option 1: Search Movies**

=== MOVIE SEARCH ===

Enter movie title: avengers

🎬 Search Results:

1. The Avengers (2012)
   Genre: Action, Adventure, Sci-Fi
   Rating: 8.0/10 | Runtime: 143 min
   Plot: Earth's mightiest heroes must come together...
2. Avengers: Endgame (2019)
   Genre: Action, Adventure, Drama
   Rating: 8.4/10 | Runtime: 181 min
   Plot: After the devastating events of Infinity War...
3. Avengers: Infinity War (2018)
   Genre: Action, Adventure, Sci-Fi
   Rating: 8.4/10 | Runtime: 149 min
   Plot: The Avengers and their allies must be willing...

Select movie to add to favorites (0 to go back) : 1

✅ "The Avengers (2012)" added to your favorites!


**Option 2: Search Music**

=== MUSIC SEARCH ===

Enter artist or song: coldplay

🎵 Search Results:

1. Coldplay - Yellow
   Album: Parachutes (2000)
   Genre: Alternative Rock
   Duration: 4:29
2. Coldplay - Fix You
   Album: X&Y (2005)
   Genre: Alternative Rock
   Duration: 4:54
3. Coldplay - Viva La Vida
   Album: Viva la Vida (2008)
   Genre: Alternative Rock
   Duration: 4:01

Select song to add to favorites (0 to go back) : 2

✅ "Fix You" by Coldplay added to your favorites!


**Option 3: Add to Favorites**

=== MANAGE FAVORITES ===

Current Favorites:
Movies: 5 items
Music: 8 items

1. View Movie Favorites
2. View Music Favorites
3. Remove from Favorites
4. Back to Main Menu

Choose option: 1

🎬 Your Favorite Movies:

1. The Avengers (2012) - Action, Adventure, Sci-Fi
2. Inception (2010) - Action, Sci-Fi, Thriller
3. The Dark Knight (2008) - Action, Crime, Drama
4. Interstellar (2014) - Adventure, Drama, Sci-Fi
5. Pulp Fiction (1994) - Crime, Drama


**Option 4: Get Movie Recommendations**

=== MOVIE RECOMMENDATIONS FOR YOU ===

Based on your favorites...

🎬 Top Recommendations genres based on your favorites: Action, Sci-Fi

1. Last Action Hero (1993)
   Genre: Action, Adventure, Comedy
   Rating: 6.5/10 | Duration: 130 min mins
   ImdbID: tt0107362
   Why: Similar to Last Action Hero based on genre and themes
2. Back in Action (2025)
   Genre: Action, Comedy
   Rating: 5.9/10 | Duration: 114 min mins
   ImdbID: tt21191806
   Why: Similar to Back in Action based on genre and themes
3. Looney Tunes: Back in Action (2003)
   Genre: Animation, Adventure, Comedy
   Rating: 5.8/10 | Duration: 91 min mins
   ImdbID: tt0318155
   Why: Similar to Looney Tunes: Back in Action based on genre and themes
4. An Action Hero (2022)
   Genre: Action, Comedy, Crime
   Rating: 7.0/10 | Duration: 130 min mins
   ImdbID: tt15600222
   Why: Similar to An Action Hero based on genre and themes

Add any to favorites? (0 to go back): 1

✅ Added "Last Action Hero" to favorites!


**Option 5: Get Music Recommendations**

=== MUSIC RECOMMENDATIONS FOR YOU ===

Based on your favorite tracks...

🎧 Top Recommendations based on: My Universe

1. My Universe - SUGA's Remix - Coldplay
   Album: Unknown
   Duration: N/A mins
   Listeners: Unknown
2. My Universe - Instrumental - Coldplay
   Album: Unknown
   Duration: N/A mins
   Listeners: Unknown

Add any to favorites? (0 to go back): 1

✅ Added "My Universe - SUGA's Remix" by Coldplay to favorites!


**Option 6: View Profile**

=== YOUR PROFILE ===

👤 User: Alex

📊 Statistics:
Movies Favorited: 7
Songs Favorited: 12
Recommendations Used: 15

🎭 Favorite Genres:
Movies: Action (35%), Sci-Fi (28%), Drama (22%), Crime (15%)
Music: Alternative Rock (45%), Pop Rock (25%), Rock (30%)

🏆 Achievements:
✅ Movie Buff - 10+ favorite movies
✅ Music Lover - 15+ favorite songs
✅ Explorer - Tried 5+ new recommendations

🤝 Similar Users:

1. MovieFan2025 (78% similarity)
2. MusicLover92 (65% similarity)
3. SciFiAddict (61% similarity)


**Option 7: Find Similar Users**

=== FIND SIMILAR USERS ===

Analyzing your preferences...

🤝 Users with Similar Tastes:

1. MovieFan2025 (78% similarity)
   Common interests: Marvel movies, Christopher Nolan films
   Their unique favorites: Mad Max, Blade Runner
2. MusicLover92 (65% similarity)
   Common interests: Coldplay, alternative rock
   Their unique favorites: Arctic Monkeys, Kings of Leon
3. SciFiAddict (61% similarity)
   Common interests: Interstellar, sci-fi genre
   Their unique favorites: Arrival, Ex Machina

View recommendations from similar user? (Enter number): 1

🎬 MovieFan2025's Recommendations for You:

1. Mad Max: Fury Road (2015) - Action thriller
2. Blade Runner (1982) - Classic sci-fi
3. Thor: Ragnarok (2017) - Marvel comedy

Add any to your watchlist? (Enter numbers): 1,3
✅ Added 2 movies to your watchlist!


**Option 8: Exit**

=== RECOMMENDATION ENGINE ===

Saving your preferences...
✅ Data saved to user_profile.json

Thanks for using the Entertainment Recommendation Engine!
Keep discovering amazing movies and music! 🎬🎵

Program terminated.
