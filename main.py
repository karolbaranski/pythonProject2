import os
import time
from imdb import IMDb

def rename_folders(volume_name):
    ia = IMDb()
    folder_path = volume_name
    subfolders = os.listdir(folder_path)
    for i, subfolder in enumerate(subfolders):
        subfolder_path = os.path.join(folder_path, subfolder)
        if os.path.isdir(subfolder_path):
            try:
                movie_name = subfolder.replace("_", " ")
                movie = ia.search_movie(movie_name)[0]
                ia.update(movie)
                new_name = movie["long imdb title"]
                age_restriction = movie["certificate"]
                imdb_rating = movie["rating"]
                if age_restriction:
                    new_name = new_name + " [" + age_restriction + "]"
                if imdb_rating:
                    new_name = new_name + " [" + str(imdb_rating) + "/10]"
                new_path = os.path.join(folder_path, new_name)
                os.rename(subfolder_path, new_path)
                print("Renamed " + subfolder + " to " + new_name)
            except:
                print(f"Error renaming {subfolder}")
        if i % 10 == 0:
            time.sleep(5)


volume_name = input("Enter the name of the volume containing the movie folders: ")
rename_folders(volume_name)
