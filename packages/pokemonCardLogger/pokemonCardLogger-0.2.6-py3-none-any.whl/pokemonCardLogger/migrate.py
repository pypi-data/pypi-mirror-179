import json
import os
import sys
import pickle

pltfrm = sys.platform
home = os.environ["HOME"]
if pltfrm == "linux":
    prog_data = os.path.join(os.path.join(home, ".config"), "POKEMON_TCG_LOG")
elif pltfrm in ["win32", "cygwin", "darwin"]:
    prog_data = os.path.join(os.path.join(home, "Documents"), "POKEMON_TCG_LOG")
else:
    print("your system is not supported. quitting")
    quit(1)


def migrate_to_pickle(json_file: str, pickle_file: str):
    if not os.path.exists(json_file):
        raise FileNotFoundError
    with open(json_file) as f:
        log_dict = json.load(f)
    with open(pickle_file, "wb") as f:
        pickle.dump(log_dict, f)


def migrate_to_json(pickle_file: str, json_file: str):
    if not os.path.exists(pickle_file):
        raise FileNotFoundError
    with open(pickle_file, "rb") as f:
        log_dict = pickle.load(f)
    with open(json_file, "w") as f:
        json.dump(log_dict, f)


def main():
    print("will you migrate from pickle or json, 1 for pickle 2 for json")
    mode = input(">>> ")
    other = ""
    if mode not in ("1", "2"):
        print("invalid input. try again")
        return main()
    if mode == "1":
        mode = ".pcllog"
        other = ".json"
    elif mode == "2":
        mode = ".json"
        other = ".pcllog"
    print("please enter the name of the user you wish to migrate")
    user = input(">>> ")
    active_file_user = f"{user}{mode}"
    new_file_user = f"{user}{other}"
    new_file_user = os.path.join(prog_data, new_file_user)
    active_file_user = os.path.join(prog_data, active_file_user)
    if not os.path.exists(active_file_user):
        print("file not found. try again")
        return main()
    if mode == ".pcllog":
        migrate_to_json(active_file_user, new_file_user)
    else:
        migrate_to_pickle(active_file_user, new_file_user)


if __name__ == "__main__":
    main()
