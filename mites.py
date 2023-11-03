import asana
import json

# define text colors (to show success/fail messages)
class colors:
  green = "\033[1;32m"
  red = "\033[1;32m"
  reset = "\033[0m"

# read file contents of necessary tokens/gids
tokensFile = open("tokens/tokens.json", "r")
# convert JSON to dict
tokens = json.loads(tokensFile.read())

# authenticate with access token
client = asana.Client.access_token(tokens["accessToken"])
# remove pesky deprecation warnings
client.LOG_ASANA_CHANGE_WARNINGS = False

loopVal = True
while loopVal == True:
  # get user input (what to name mite)
  miteVal = input(colors.reset + "What is this mite? (X/C to Exit): ")

  if miteVal.lower() == 'exit' or miteVal.lower() == 'x' or miteVal.lower() == 'c':
    tokensFile.close()
    print(colors.reset)
    loopVal = False
  else:
    # send POST request
    result = client.tasks.create_task({"name": miteVal, "assignee": tokens["assigneeGid"], "workspace": tokens["workspaceGid"], "projects": [tokens["projectGid"]], "tags": [tokens["tagsGid"]]}, opt_pretty=True)
    print(colors.green + "beep-boop: new mite made! You can access it here: " + result["permalink_url"])
