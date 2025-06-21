
#===== Imports =====
import json
import random
from re import sub
import re
import requests
from collections import Counter


#===== File I/O =====
# JSON File Functions
def save_to_json(allUser, filename="user_profile.json"):
    with open(filename, "w") as f:
        json.dump(allUser, f, indent=4)


def load_from_json(filename="user_profile.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        return data if isinstance (data, dict) else {}
    except FileNotFoundError:
        return {}
    

#===== Utility =====
def profileName(x):
    name = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', x.replace("-", " "))
    name = '_'.join(name.split()).lower()
    numberUser = str(random.randint(1000, 9999))
    return name+"_"+numberUser


#===== Feature: Movie Search =====
def searched_movie(current_user, allUser):
    print("===== MOVIE SEARCH =====")
    api_key = '5551114b'
    title = input("Enter Movie Title: ")
    url = f"http://www.omdbapi.com/?s={title}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    movie = data.get("Search", [])
    print("🎬 Search Results:")
    movie_list = []

    for i, movie in enumerate(movie, 1):
        detail_url = f"http://www.omdbapi.com/?i={movie["imdbID"]}&apikey={api_key}&plot=short"
        detail_response = requests.get(detail_url)
        details = detail_response.json()
        title = details.get("Title", "N/A")
        year = details.get("Year", "N/A")
        genre = details.get("Genre", "N/A")
        rating = details.get("imdbRating", "N/A")
        runtime = details.get("Runtime", "N/A")
        plot = details.get("Plot", "N/A")[:50] + "..."
        imdbid = details.get("imdbID", "N/A")
        print(f"{i}. {title} ({year})")
        print(f"   Genre: {genre}")
        print(f"   Rating: {rating}/10 | Runtime: {runtime}")
        print(f"   Plot: {plot}\n")
        movie_list.append({
            "title": title,
            "year": year,
            "genre": genre,
            "rating": rating,
            "imdb_id": imdbid
        })

    select = input("Select movie to add to favorites (0 to go back): ").strip().split()
    print("")

    if select == ["0"]:
        return

    selected_favorites = [movie_list[int(i)-1] for i in select if i.isdigit()]
    
    allUser[current_user].setdefault("favorite_movies", []).extend(selected_favorites)
    save_to_json(allUser)

    for fav in selected_favorites:
        print(f"✅ \"{fav["title"]} ({fav["year"]})\" added to your favorites!")


# ===== Feature: Music Search =====
def searched_music(current_user, allUser):
    print("===== MUSIC SEARCH =====")
    api_key = 'fed978f5587dde086bd2007db738d2c3'
    query = input("Enter artist or song: ")
    url = f"http://ws.audioscrobbler.com/2.0/?method=track.search&track={query}&api_key={api_key}&format=json&limit=3"
    response = requests.get(url)
    data = response.json()

    tracks = data["results"]["trackmatches"]["track"]
    print("🎵 Search Results:")
    music_list = []

    for i, track in enumerate(tracks, 1):
        detail_url = f"http://ws.audioscrobbler.com/2.0/?method=track.getInfo&artist={track['artist']}&track={track['name']}&api_key={api_key}&format=json"
        detail_response = requests.get(detail_url)
        details = detail_response.json()["track"]
        artist = track["artist"]
        title = details.get("name", track["name"])
        album = details.get("album", {}).get("title", "N/A")
        duration = details.get("duration", "N/A")
        durationSecondTotal = int(duration)//1000
        durationMinute = durationSecondTotal//60
        durationSecond = durationSecondTotal % 60
        fDuration = f"{durationMinute}:{durationSecond}"
        listeners = details.get("listeners", "N/A")
        flisteners = f"{int(listeners):,}"
        print(f"\n{i}. {artist} - {title}")
        print(f"   Duration: {fDuration} mins")
        print(f"   Album: {album}")
        print(f"   Listeners: {flisteners}")
        music_list.append({
            "artist": artist,
            "title": title,
            "duration": fDuration,
            "album": album,
            "listeners": flisteners
        })

    select = input("Select song to add to favorites (0 to go back): ").strip().split()
    print("")

    if select == ["0"]:
        return

    selected_favorites = [music_list[int(i)-1] for i in select if i.isdigit()]
    
    allUser[current_user].setdefault("favorite_musics", []).extend(selected_favorites)
    save_to_json(allUser)

    for fav in selected_favorites:
        print(f"✅ \"{fav["title"]}\" by {fav["artist"]} added to your favorites!")


# ===== Feature: Manage Favorites =====
def manage_favorites(current_user, allUser):
    while True:
        fav_movies = allUser[current_user].get("favorite_movies", [])
        fav_music = allUser[current_user].get("favorite_musics", [])

        print("===== MANAGE FAVORITES =====")
        print("")
        print("Current Favorites:")
        print(f"Movies: {len(fav_movies)} items")
        print(f"Music: {len(fav_music)} items")
        print("")

        print("1. View Movie Favorites")
        print("2. View Music Favorites")
        print("3. Remove from Favorites")
        print("4. Back to Main Menu")
        print("")

        choice = input("Choose option: ")
        print("")
        if choice == "1":
            print("🎬 Your Favorite Movies:")
            if fav_movies:
                for i, movie in enumerate(fav_movies, 1):
                    print(f"{i}. {movie['title']} ({movie['year']}) - {movie['genre']}")
                print("")
            else:
                print("No favorite movie")

        elif choice == "2":
            print("🎵 Your Favorite Movies:")
            if fav_music:
                for i, track in enumerate(fav_music, 1):
                    print(f"{i}. {track['title']} by {track['artist']} - Album: {track['album']}")
                print("")
            else:
                print("No favorite music")

        elif choice == "3":
            print("===== Remove From Favorites =====")
            print("")
            print("1. Remove From Movie Favorites")
            print("2. Remove From Music Favorites")
            print("3. Back To Menu")
            print("")

            sub_choice = input("Choose option: ")
            if sub_choice == "1" and fav_movies:
                print("=== Remove From Movie Favorites ===")
                for i, movie in enumerate(fav_movies, 1):
                    print(f"{i}. {movie['title']} ({movie['year']})")

                to_remove = input("Enter numbers to remove: ").strip().split()
                to_remove = sorted([int(i)-1 for i in to_remove if i.isdigit() and 0 < int(i) <= len(fav_movies)], reverse=True)
                for index in to_remove:
                    removed = fav_movies.pop(index)
                    print("")
                    print(f"❌ Removed \"{removed['title']} ({removed['year']})\" from favorites.")
                allUser[current_user]["favorite_movies"] = fav_movies
                save_to_json(allUser)
                print("")

            elif sub_choice == "2" and fav_music:
                print("=== Remove From Music Favorites ===")
                for i, track in enumerate(fav_music, 1):
                    print(f"{i}. {track['title']} by {track['artist']}")
                to_remove = input("Enter numbers to remove: ").strip().split()
                to_remove = sorted([int(i)-1 for i in to_remove if i.isdigit() and 0 < int(i) <= len(fav_music)], reverse=True)
                for index in to_remove:
                    removed = fav_music.pop(index)
                    print("")
                    print(f"❌ Removed \"{removed['title']}\" by {removed['artist']} from favorites.")
                allUser[current_user]["favorite_musics"] = fav_music
                save_to_json(allUser)
                print("")

            elif sub_choice == "3":
                continue

            else:
                print("Invalid selection Inputs")

        elif choice == "4":
            break

        else:
            print("Invalid option")


# ===== Feature: Movie Recommendation =====
def get_movie_recommendations(current_user, allUser):
    print("=== MOVIE RECOMMENDATIONS FOR YOU ===\n")
    print("Based on your favorites...\n")

    api_key = '5551114b'
    fav_movies = allUser[current_user].get("favorite_movies", [])

    if not fav_movies:
        print("You have no favorite movies yet. Add some to get recommendations!\n")
        return

    favorite_genres = []
    for movie in fav_movies:
        favorite_genres.extend(movie.get("genre", "").split(", "))

    genre_count = Counter(favorite_genres)
    top_genres = [genre for genre, _ in genre_count.most_common(2)]

    recommendations = []
    seen_titles = set(m["title"] for m in fav_movies)

    print(f"🎬 Top Recommendations genres based on your favorites: {', '.join(top_genres)}\n")

    for genre in top_genres:
        url = f"http://www.omdbapi.com/?s={genre}&apikey={api_key}&type=movie"
        response = requests.get(url)
        data = response.json()

        search_results = data.get("Search", [])
        for result in search_results:
            imdb_id = result.get("imdbID")
            if not imdb_id:
                continue

            # Get full details
            detail_url = f"http://www.omdbapi.com/?i={imdb_id}&apikey={api_key}&plot=short"
            detail_response = requests.get(detail_url)
            details = detail_response.json()

            title = details.get("Title")
            year = details.get("Year", "N/A")
            genre_data = details.get("Genre", "N/A")
            rating = details.get("imdbRating", "N/A")
            imdb_id = details.get("imdbID", "N/A")
            duration = details.get("Runtime", "N/A")

            if title in seen_titles or not title:
                continue

            recommendations.append({
                "title": title,
                "year": year,
                "genre": genre_data,
                "rating": rating,
                "imdb_id": imdb_id,
                "duration": duration
            })

            seen_titles.add(title)

            if len(recommendations) >= 10:
                break
        if len(recommendations) >= 10:
            break

    if not recommendations:
        print("No recommendations found at the moment. Try adding more favorites.\n")
        return

    for i, rec in enumerate(recommendations, 1):
        print(f"{i}. {rec['title']} ({rec['year']})")
        print(f"   Genre: {rec['genre']}")
        print(f"   Rating: {rec['rating']}/10 | Duration: {rec['duration']} mins")
        print(f"   ImdbID: {rec['imdb_id']}")
        print(f"   Why: Similar to {rec['title']} based on genre and themes\n")

    select = input("Add any to favorites? (0 to go back): ").strip()
    print("")

    if select == "0":
        return

    selected_indexes = [int(i.strip()) - 1 for i in select.split(",") if i.strip().isdigit()]
    selected_movies = [recommendations[i] for i in selected_indexes if 0 <= i < len(recommendations)]

    for rec in selected_movies:
        allUser[current_user].setdefault("favorite_movies", []).append(rec)

        allUser[current_user].setdefault("recommendation_score", {})
        score_dict = allUser[current_user]["recommendation_score"]
        score_dict[rec["imdb_id"]] = score_dict.get(rec["imdb_id"], 0) + 1

    save_to_json(allUser)

    if selected_movies:
        added_titles = [f"\"{m['title']}\"" for m in selected_movies]
        print(f"✅ Added {', '.join(added_titles)} to favorites!\n")


# ===== Feature: Music Recommendation =====
def get_music_recommendations(current_user, allUser):
    print("=== MUSIC RECOMMENDATIONS FOR YOU ===\n")
    print("Based on your favorite tracks...\n")

    api_key = 'fed978f5587dde086bd2007db738d2c3'
    fav_music = allUser[current_user].get("favorite_musics", [])

    if not fav_music:
        print("You have no favorite tracks yet. Add some to get recommendations!\n")
        return

    search_terms = [track.get("title", "") for track in fav_music if track.get("title")]
    search_count = Counter(search_terms)
    top_terms = [term for term, _ in search_count.most_common(2)]

    print(f"🎧 Top Recommendations based on: {', '.join(top_terms)}\n")

    recommendations = []
    seen_titles = set(t["title"] for t in fav_music)

    for term in top_terms:
        search_url = f"http://ws.audioscrobbler.com/2.0/?method=track.search&track={term}&api_key={api_key}&format=json&limit=5"
        response = requests.get(search_url)
        data = response.json()

        tracks = data.get("results", {}).get("trackmatches", {}).get("track", [])
        for track in tracks:
            title = track.get("name")
            artist = track.get("artist")

            if not title or title in seen_titles:
                continue

            info_url = f"http://ws.audioscrobbler.com/2.0/?method=track.getInfo&api_key={api_key}&artist={artist}&format=json"
            info_response = requests.get(info_url)
            info_data = info_response.json()

            track_info = info_data.get("track", {})
            duration_ms = int(track_info.get("duration", 0))
            duration = f"{duration_ms // 60000}:{(duration_ms % 60000) // 1000:02d}" if duration_ms else "N/A"
            album = track_info.get("album", {}).get("title", "Unknown")
            listeners = track_info.get("listeners", "Unknown")

            # url = track_info.get("url", "")

            recommendations.append({
                "artist": artist,
                "title": title,
                "duration": duration,
                "album": album,
                "listeners": listeners,
                # "url": url
            })

            seen_titles.add(title)

            if len(recommendations) >= 10:
                break
        if len(recommendations) >= 10:
            break

    if not recommendations:
        print("No music recommendations found at the moment. Try adding more favorites.\n")
        return

    for i, rec in enumerate(recommendations, 1):
        print(f"{i}. {rec['title']} - {rec['artist']}")
        print(f"   Album: {rec['album']}")
        print(f"   Duration: {rec['duration']} mins")
        print(f"   Listeners: {rec['listeners']}\n")
        # print(f"   🔗 Listen: {rec['url']}\n")

    select = input("Add any to favorites? (0 to go back): ").strip()
    print("")

    if select == "0":
        return

    selected_indexes = [int(i.strip()) - 1 for i in select.split(",") if i.strip().isdigit()]
    selected_tracks = [recommendations[i] for i in selected_indexes if 0 <= i < len(recommendations)]

    for rec in selected_tracks:
        allUser[current_user].setdefault("favorite_musics", []).append({
            "artist": rec["artist"],
            "title": rec["title"],
            "duration": rec["duration"],
            "album": rec["album"],
            "listeners": rec["listeners"]
        })

        allUser[current_user].setdefault("recommendation_score", {})
        score_dict = allUser[current_user]["recommendation_score"]
        unique_key = f"{rec['artist']} - {rec['title']}"
        score_dict[unique_key] = score_dict.get(unique_key, 0) + 1

    save_to_json(allUser)

    if selected_tracks:
        added_titles = [f"\"{m['title']}\" by {m['artist']}" for m in selected_tracks]
        print(f"✅ Added {', '.join(added_titles)} to favorites!\n")



# ===== Feature: Profile View =====
def profile_view(current_user, allUser):

    def extract_genres(items, key, is_music=False):
        genre_counts = Counter()
        for item in items:
            genres = item.get(key, "").split(",") if not is_music else item.get("genre", "").split(",")
            for g in genres:
                clean = g.strip().title()
                if clean:
                    genre_counts[clean] += 1
        return genre_counts

    def format_genre_distribution(genre_counts):
        total = sum(genre_counts.values())
        if total == 0:
            return "N/A"
        sorted_genres = genre_counts.most_common(4)
        return ', '.join([f"{genre} ({(count/total)*100:.0f}%)" for genre, count in sorted_genres])

    print("=== YOUR PROFILE ===\n")
    user_data = allUser[current_user]
    name = user_data.get("name", "N/A")
    fav_movies = user_data.get("favorite_movies", [])
    fav_music = user_data.get("favorite_musics", [])
    score_dict = allUser[current_user].get("recommendation_score", {})
    recommendation_score = sum(score_dict.values())

    print(f"👤 User: {name}\n")
    print("📊 Statistics:")
    print(f"Movies Favorited: {len(fav_movies)}")
    print(f"Songs Favorited: {len(fav_music)}")
    print(f"Recommendation Used: {recommendation_score}\n")

    movie_genres = extract_genres(fav_movies, "genre")
    music_genres = extract_genres(fav_music, "artist", is_music=True)  

    print("🎭 Favorite Genres:")
    print("Movies: " + format_genre_distribution(movie_genres))
    print("Music: " + format_genre_distribution(music_genres) + "\n")

    if len(fav_movies) >= 10 or len(fav_music) >= 15:
        print("🏆 Achievements:")
        if len(fav_movies) >= 10:
            print("✅ Movie Buff - 10+ favorite movies")
        if len(fav_music) >= 15:
            print("✅ Music Lover - 15+ favorite songs")
        print("")

    base_user = allUser[current_user]
    base_movies = set((m["title"], m["genre"]) for m in base_user.get("favorite_movies", []))
    base_music = set((m["title"], m["artist"]) for m in base_user.get("favorite_musics", []))

    similarity_scores = []

    for other_user, other_data in allUser.items():
        if other_user == current_user:
            continue

        other_movies = set((m["title"], m["genre"]) for m in other_data.get("favorite_movies", []))
        other_music = set((m["title"], m["artist"]) for m in other_data.get("favorite_musics", []))

        common_movies = base_movies & other_movies
        common_music = base_music & other_music

        total_common = len(common_movies) + len(common_music)
        total_unique = len(base_movies | other_movies) + len(base_music | other_music)

        if total_common == 0:
            continue

        similarity = (total_common / total_unique) * 100

        similarity_scores.append({
            "user": other_user,
            "similarity": round(similarity)
        })

    similarity_scores.sort(key=lambda x: x["similarity"], reverse=True)

    print("🤝 Similar Users:")
    for i, sim_user in enumerate(similarity_scores[:1], 1):
        print(f"{i}. {sim_user['user']} ({sim_user['similarity']}% similarity)")


# ===== Feature: Find Similar Users =====
def find_similar_users(current_user, allUser):
    print("=== FIND SIMILAR USERS ===\n")
    print("Analyzing your preferences...\n")
    print("🤝 Users with Similar Tastes:\n")

    base_user = allUser[current_user]
    base_movies = set((m["title"], m["genre"]) for m in base_user.get("favorite_movies", []))
    base_music = set((m["title"], m["artist"]) for m in base_user.get("favorite_musics", []))

    similarity_scores = []

    for other_user, other_data in allUser.items():
        if other_user == current_user:
            continue

        other_movies = set((m["title"], m["genre"]) for m in other_data.get("favorite_movies", []))
        other_music = set((m["title"], m["artist"]) for m in other_data.get("favorite_musics", []))

        common_movies = base_movies & other_movies
        common_music = base_music & other_music

        total_common = len(common_movies) + len(common_music)
        total_unique = len(base_movies | other_movies) + len(base_music | other_music)

        if total_common == 0:
            continue

        similarity = (total_common / total_unique) * 100

        unique_movies = other_movies - base_movies
        unique_music = other_music - base_music

        similarity_scores.append({
            "user": other_user,
            "similarity": round(similarity),
            "shared_movies": list(common_movies),
            "shared_music": list(common_music),
            "unique_movies": [m for m in other_data.get("favorite_movies", [])
                              if (m["title"], m["genre"]) in unique_movies],
            "unique_music": [m for m in other_data.get("favorite_musics", [])
                             if (m["title"], m["artist"]) in unique_music]
        })

    if not similarity_scores:
        print("No similar users found yet. Try adding more to your favorites!\n")
        return

    similarity_scores.sort(key=lambda x: x["similarity"], reverse=True)

    for i, sim_user in enumerate(similarity_scores[:5], 1):
        print(f"{i}. {sim_user['user']} ({sim_user['similarity']}% similarity)")

        common_interests = []
        if sim_user["shared_movies"]:
            movie_genres = {genre for _, genre in sim_user["shared_movies"]}
            movie_titles = {title for title, _ in sim_user["shared_movies"]}
            if movie_genres:
                common_interests.append(", ".join(movie_genres))
            if movie_titles:
                common_interests.append(", ".join(movie_titles))
        if sim_user["shared_music"]:
            music_artists = {artist for _, artist in sim_user["shared_music"]}
            if music_artists:
                common_interests.append(", ".join(music_artists))

        print("   Common interests:", "; ".join(common_interests) if common_interests else "None")

        unique_favorites = []
        if sim_user["unique_movies"]:
            unique_favorites.extend(m["title"] for m in sim_user["unique_movies"])
        if sim_user["unique_music"]:
            unique_favorites.extend(m["title"] for m in sim_user["unique_music"])

        print("   Their unique favorites:", ", ".join(unique_favorites) if unique_favorites else "None")
        print("")

    select = input("View recommendations from similar user? (Enter number, 0 to skip): ").strip()
    if select == "0" or not select.isdigit():
        return

    idx = int(select) - 1
    if idx < 0 or idx >= len(similarity_scores):
        print("Invalid selection.")
        return

    chosen_user = similarity_scores[idx]
    print(f"\n🎬 {chosen_user['user']}'s Recommendations for You:")

    base_movie_titles = {m["title"] for m in allUser[current_user].get("favorite_movies", [])}
    suggestions = [m for m in chosen_user["unique_movies"] if m["title"] not in base_movie_titles]

    if not suggestions:
        print("No new recommendations to suggest.\n")
        return

    for i, movie in enumerate(suggestions, 1):
        title = movie.get("title", "Unknown")
        year = movie.get("year", "N/A")
        genre = movie.get("genre", "N/A")
        print(f"{i}. {title} ({year}) - {genre}")


    print("")
    to_add = input("Add any to your watchlist? (Enter numbers, 0 to skip): ").strip()
    if to_add == "0":
        return

    selected = [int(x.strip()) - 1 for x in to_add.split(",") if x.strip().isdigit()]
    added = 0
    for i in selected:
        if 0 <= i < len(suggestions):
            allUser[current_user].setdefault("favorite_movies", []).append(suggestions[i])
            added += 1

    if added:
        print(f"✅ Added {added} movie{'s' if added > 1 else ''} to your watchlist!\n")

    save_to_json(allUser)


# ===== Program Start =====
def start_program():
    allUser = load_from_json()
    current_user = None

    while not current_user:
        print("Welcome to Movie/Music Recommendation Engine\n")
        print("1. Register\n2. Login\n")
        inputs = int(input("Choose An Option:"))

        if inputs == 1:
                print("===== Register =====\n")
                user = input("Enter Name:")
                userName = profileName(user)
                print("")
                print(f"Genrated Username: {userName}")
                allUser[userName] = {"name" : user}
                save_to_json(allUser)
                print("")
                print("✅ User Register Successfully")
                print("====================")
                print("")

        elif inputs == 2:
                print("===== Login =====\n")
                userName = input("Enter Username: ")
                if userName in allUser:
                    print(f"Welcome Back, {allUser[userName]["name"]}")
                    current_user = userName
                else:
                    print("User not found... Please register first.")

        else:
            print("Invalid input")
            break

    while True:
        print("\n===== ENTERTAINMENT RECOMMENDATION ENGINE =====\n")
        print("1. Search Movies")
        print("2. Search Music")  
        print("3. Add to Favorites")
        print("4. Get Movie Recommendations")
        print("5. Get Music Recommendations")
        print("6. View Profile")
        print("7. Find Similar Users")
        print("8. Exit\n")

        menu = int(input("Choose an option: "))

        match menu:
            case 1:
                # ===== MOVIE SEARCH =====
                searched_movie(current_user, allUser)
            case 2:
                # ===== MUSIC SEARCH =====
                searched_music(current_user, allUser)
            case 3:
                # ===== MANAGE FAVORITES =====
                manage_favorites(current_user, allUser)
            case 4:
                # ===== MOVIE RECOMMENDATIONS FOR YOU =====
                get_movie_recommendations(current_user, allUser)
            case 5:
                # ===== MUSIC RECOMMENDATIONS FOR YOU =====
                get_music_recommendations(current_user, allUser)
            case 6:
                # === YOUR PROFILE ===
                profile_view(current_user, allUser)
            case 7:
                # ===== FIND SIMILAR USERS =====
                find_similar_users(current_user, allUser)
            case 8:
                print("===== RECOMMENDATION ENGINE =====")
                print("\nSaving your preferences...")
                print("✅ Data saved to user_profile.json\n")
                print("Thanks for using the Entertainment Recommendation Engine!")
                print("Keep discovering amazing movies and music! 🎬🎵\n")
                print("Program terminated.")
                break
            case _:
                print("===== Invalid Inputs! =====")
        

# ===== Run Program =====
start_program()