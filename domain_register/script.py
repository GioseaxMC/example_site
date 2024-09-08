spaces1 = " " * 65
spaces2 = " " * 65
done = ""
error = ""


def strings_in_string(list_of_strings, main_string):
    return any(substring in main_string for substring in list_of_strings)

def loop(events, inputs, self):

    if self.strings_in_string(("add_done", "edit_done", "rem_done"), events):
        if "add_done" in events:
            self.done, self.error = d.add_domain(inputs["add_domain"], inputs["add_ip"])
        elif "edit_done" in events:
            self.done, self.error = d.edit_domain(inputs["edit_key"], inputs["edit_ip"])
        elif "rem_done" in events:
            self.done, self.error = d.delete_domain(inputs["rem_key"])
        


