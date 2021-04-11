class ImproperConfiguredInput(Exception):
    def __init__(self, position = -1, message="Please check inputs"):
        self.position = position
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        if self.position==-1:
            return "{}".format(self.message)
        else:
            return "Check position at {} - {}".format(self.position, self.message)