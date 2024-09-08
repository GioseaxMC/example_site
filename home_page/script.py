search = " - "

def loop(events, inputs, self):
    if "getlink" in events or inputs.get("link"):
        load(inputs["link"])
    elif "getsearch" in events or inputs.get("search"):
        self.search = browse(self.domains, inputs["search"])
        load_browser(self.search, inputs["search"])