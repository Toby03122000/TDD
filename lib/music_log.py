class MusicLog():

    def __init__(self):
        self.tracks = []

    def add(self, track):
        if track not in self.tracks:
            self.tracks.append(track)

    def display(self):
        return self.tracks