## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
class MusicLog():
    # User-facing properties:
    #   tracks: list

    def __init__(self, tracks):
        # Parameters:
        #   tracks: list
        # Side effects:
        #   Sets the tracks property of the self object
        pass # No code here yet

    def add(self, tracks):
        # Parameters:
        #   task: string representing a single track
        # Returns:
        #   List of track
        # Side-effects
        #   Saves the track to the self object
        pass # No code here yet

    def display(self):
        # Returns:
        #   A list displaying the user's listened to tracks
        # Side-effects:
        #   Throws an exception if no track is set
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
"""
Given no tracks
#display returns an empty list
"""
music_log = MusicLog()
music_log.display() # => []

"""
Given 1 track
#display returns a list of that 1 track
"""
music_log = MusicLog()
music_log.add("Track 1")
music_log.display() # => ["Track 1"]

"""
Given 2 tracks
#display returns a list of that 2 tracks
"""
music_log = MusicLog()
music_log.add("Track 1")
music_log.add("Track 2")
music_log.display() # => ["Track 1", "Track 2"]
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._