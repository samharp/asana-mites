import asana
import json
import sys
import datetime

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
  userInput = input(colors.reset + "what is this mite? (OR: X to exit, C to clean): ")

  if userInput.lower() == "exit" or userInput.lower() == "x":
    tokensFile.close()
    print(colors.reset)
  elif userInput.lower() == "clean" or userInput.lower() == "c":
    cleanMitebox()
  elif userInput.lower() == "info" or userInput.lower() == "i":
    # getMiteboxInfo()
  else:
    createMite(userInput)

# function for creating task (sending request)
def createMite(miteVal):
  try:
    # send POST request
    result = client.tasks.create_task({"name": miteVal, "assignee": tokens["assigneeGid"], "workspace": tokens["workspaceGid"], "projects": [tokens["miteboxGid"]], "tags": [tokens["tagsGid"]]})
    # success message
    print(colors.green + "beep-boop: new mite made! you can access it here: " + result["permalink_url"])

  except KeyError:
    print(colors.red + "something doesn't look right with your token configuration. please reference the README to confirm it is set up correctly and try again.")
  except:
    print(colors.red + "it looks like something happened with your request. ensure the right values are placed in your token configuration and try again.")
  getUserInput()

# function for cleaning up mitebox
def cleanMitebox():
  numberOfTasks = 0
  try:
    # get all completed tasks in to-do section
    tasksCompletedResult = client.tasks.get_tasks({"section": tokens["toDoGid"], "opt_fields": ["completed"]})

    # Iterating through the result as a list
    for i in list(tasksCompletedResult):
      if(i["completed"] == True):
        try:
          # move completed task to the done pile
          taskMovingResult = client.sections.add_task_for_section(tokens["donePileGid"], {"task": i["gid"]})
          numberOfTasks += 1
        except:
          print(colors.red + "it looks like something happened while moving task(s) to the Done Pile... Check your setup and try again.")
    # success message
    if(numberOfTasks > 0):
      print(colors.green + "beep-boop: your Mitebox is all cleaned up! " + str(numberOfTasks) + " completed task(s) moved to the Done Pile.")
    else:
      print("looks like there were no completed tasks to be moved to the Done Pile...")
  except:
    print(colors.red + "it looks like something happened when trying to get completed tasks in your Mitebox. check your setup and try again.")
  getUserInput()

# PROGRAM START
if len(sys.argv) >= 2:
  createMite(sys.argv[1])
else:
  getUserInput()
