def loop(events, inputs, self):
    if "getlink" in events or inputs.get("link"):
        load(inputs["link"])
    elif "getsearch" in events or inputs.get("search"):
        load(browse(inputs["search"], domains)[0]["ip"])