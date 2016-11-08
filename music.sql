DROP TABLE IF EXISTS artist;
DROP TABLE IF EXISTS album;
DROP TABLE IF EXISTS song;

CREATE TABLE artist(
    artist_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER
);

CREATE TABLE album(
    album_id INTEGER PRIMARY KEY,
    album_name TEXT,
    artist_id INTEGER
);

CREATE TABLE song(
    song_id INTEGER PRIMARY KEY,
    song_name TEXT,
    artist_id INTEGER,
    album_id INTEGER,
    track_num INTEGER,
    track_len INTEGER
);