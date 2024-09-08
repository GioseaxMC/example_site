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

    if not frames() % 3 and len(self.message):
        self.welcome =+ self.message[0]
        self.message[1:]
    self.display = self.welcome + ("_" if not frames() % 30 > 15 else "")