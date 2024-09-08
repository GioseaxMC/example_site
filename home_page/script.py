def loop(events, inputs, self):
    if "getlink" in events or inputs.get("link"):
        load(inputs["link"])
    elif "getsearch" in events or inputs.get("search"):
        load(browse(self.domains, inputs["search"])[0]["ip"])