import json

with open(os.path.join(cfg.data_path, 'playlists.json'), 'w') as out:
    # pretty print
    json.dump(playlists, out, indent=2)
