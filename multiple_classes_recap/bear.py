class Bear:

    def __init__(self):
        self.stomach = []

    # no return
    def catch_fish(self, river):
        caught_fish = river.remove_fish()
        self.stomach.append(caught_fish)
        