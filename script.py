iterations = 0
random = 0


def loop(events, inputs, self):
    if not self.iterations:
        self.random = r.randint(0, 100)
    self.iterations += 1
