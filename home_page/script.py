search = " - "
welcome = ""
message = "Welcome!"
display = ""

def loop(events, inputs, self):
    if "getlink" in events or inputs.get("link"):
        load(inputs["link"])
    elif "getsearch" in events or inputs.get("search"):
        self.search = browse(self.domains, inputs["search"])
        load_browser(self.search, inputs["search"])


    if not frames() % 7 and len(self.message):
        self.welcome += self.message[0]
        self.message = self.message[1:]
    bar = "_" if not frames() % 60 > 30 else ""
    self.display = self.welcome + bar