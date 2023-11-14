import asana
import json
import sys

# define text colors (to show success/fail messages)
class colors:
  green = "\033[1;32m"
  red = "\033[31m"
  reset = "\033[0m"

# read file contents of necessary tokens/gids
tokensFile = open("tokens/tokens.json", "r")
# convert JSON to dict
tokens = json.loads(tokensFile.read())

# authenticate with access token
client = asana.Client.access_token(tokens["accessToken"])
# remove pesky deprecation warnings
client.LOG_ASANA_CHANGE_WARNINGS = False

# function for accepting user input
def getUserInput():
  # get user input (what to name mite)
  userInput = input(colors.reset + "What is this mite? (X to Exit, C to Clean): ")

  if userInput.lower() == 'exit' or userInput.lower() == 'x':
    tokensFile.close()
    print(colors.reset)
  elif userInput.lower() == 'clean' or userInput.lower() == 'c':
    print("cleaning Mitebox!")
    # cleanMitebox
    getUserInput()
  else:
    createMite(userInput)

# function for actually making request
def createMite(miteVal):
  try:
    # send POST request
    result = client.tasks.create_task({"name": miteVal, "assignee": tokens["assigneeGid"], "workspace": tokens["workspaceGid"], "projects": [tokens["miteboxGid"]], "tags": [tokens["tagsGid"]]}, opt_pretty=True)
    # success message
    print(colors.green + "beep-boop: new mite made! You can access it here: " + result["permalink_url"])

  except KeyError:
    print(colors.red + "Something doesn't look right with your token configuration. Please reference the README to confirm it is set up correctly and try again.")
  except:
    print(colors.red + "It looks like something happened with your request. Ensure the right values are placed in your token configuration and try again.")
  getUserInput()

# PROGRAM START
if len(sys.argv) >= 2:
  createMite(sys.argv[1])
else:
  getUserInput()
