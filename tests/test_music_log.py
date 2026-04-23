from lib.music_log import *

"""
Given an empty string
#display returns an empty list
"""
def test_given_no_tracks_return_empty_list():
    music_log = MusicLog()
    result = music_log.display()
    assert result == []

"""
Given 1 track
#display returns a list of that 1 track
"""
def test_given_1_track_display_returns_list_of_track():
    music_log = MusicLog()
    music_log.add("Track 1")
    result = music_log.display()
    assert result == ["Track 1"]

"""
Given 2 tracks
#display returns a list of that 2 tracks
"""
def test_given_2_tracks_display_returns_list_of_tracks():
    music_log = MusicLog()
    music_log.add("Track 1")
    music_log.add("Track 2")
    result = music_log.display()
    assert result == ["Track 1", "Track 2"]

"""
Given 2 tracks of the same name
#display returns a list of that track name once
"""
def test_given_2_same_tracks_display_returns_list_of_track_once():
    music_log = MusicLog()
    music_log.add("Track 1")
    music_log.add("Track 1")
    result = music_log.display()
    assert result == ["Track 1"]