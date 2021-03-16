#functions w/ outputs

def format_name(first, last):
  if first == "" or last == "":
    return "You didn't provide valid inputs"
  
  title_first = first.title()
  title_last = last.title()
  return f"{title_first} {title_last}"
  
full_name = format_name("vYTas", "price")
print(full_name)