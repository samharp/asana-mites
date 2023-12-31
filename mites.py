import asana
import json
import sys
import random
# from lxml import etree

# define text colors (to show success/fail messages)
class colors:
  green = "\033[1;32m"
  red = "\033[31m"
  cyan = "\033[96m"
  reset = "\033[0m"

# read file contents of necessary tokens/gids
tokensFile = open("tokens/tokens.json", "r")
# convert JSON to dict
tokens = json.loads(tokensFile.read())

# authenticate with access token
client = asana.Client.access_token(tokens["accessToken"])
# remove pesky deprecation warnings
client.LOG_ASANA_CHANGE_WARNINGS = False

def welcomeUser():
  try:
    print(colors.reset + "----------")
    print("Welcome to Mitebox Manager!")
    getUserInput()
  except KeyboardInterrupt:
    sys.exit()

# function for accepting user input
def getUserInput():
  try:
    # get user input (what to name mite)
    print(colors.reset + "__________")
    print("Enter the name of your new mite or one of the following commands:")
    print(colors.cyan + "C" + colors.reset + " to Clean: move done items to Done Pile")
    print(colors.cyan + "I" + colors.reset + " for Info: fetch basic stats on your Mitebox)")
    print(colors.cyan + "Z" + colors.reset + " for Random: fetch a random mite to work on")
    print(colors.cyan + "X" + colors.reset + " to Exit: terminate Mitebox Manager")
    userInput = input(colors.cyan + ": ")

    if userInput.lower() == "exit" or userInput.lower() == "x":
      tokensFile.close()
      print(colors.reset + "xxxxxxxxxx")
      # sys.exit()
    elif userInput.lower() == "clean" or userInput.lower() == "c":
      cleanMitebox()
    elif userInput.lower() == "info" or userInput.lower() == "i":
      getMiteboxInfo()
    elif userInput.lower() == "rando" or userInput.lower() == "z":
      getRandoMite()
    else:
      createMite(userInput)
  except KeyboardInterrupt:
    print(colors.reset + "xxxxxxxxxx")
    sys.exit()
  except:
    print(colors.red + "It looks like something happened when getting user input. Please follow the dialogs and try again.")
    print(colors.reset)

# function for creating task (sending request)
def createMite(miteVal):
  try:
    # comment on new task
    htmlText = "<body>This task was created through <a href='https://github.com/samharp/asana-mites'>Mitebox Manager</a>.</body>"

    # send POST request
    # if tags gid exists, create it with that tag
    if "tagsGid" in tokens and tokens["tagsGid"] != "":
      result = client.tasks.create_task({"name": miteVal, "assignee": tokens["assigneeGid"], "workspace": tokens["workspaceGid"], "projects": [tokens["miteboxGid"]], "tags": [tokens["tagsGid"]], "html_notes": htmlText})
    else:
      result = client.tasks.create_task({"name": miteVal, "assignee": tokens["assigneeGid"], "workspace": tokens["workspaceGid"], "projects": [tokens["miteboxGid"]], "html_notes": htmlText})
    
    # success message
    print(colors.green + "beep-boop: new mite made! you can access it here: " + result["permalink_url"])

  except KeyError:
    print(colors.red + "something doesn't look right with your token configuration. please reference the README to confirm it is set up correctly and try again.")
    print(colors.reset)
  except KeyboardInterrupt:
    print(colors.reset + "xxxxxxxxxx")
    sys.exit()
  except:
    print(colors.red + "it looks like something happened with your request. ensure the right values are placed in your token configuration and try again.")
    print(colors.reset)

  getUserInput()

# function for cleaning up mitebox
def cleanMitebox():
  numberOfTasksAssigned = 0
  numberOfTasksMoved = 0
  try:
    # get all tasks in to-do section
    tasksCompletedResult = client.tasks.get_tasks({"section": tokens["doPileGid"], "opt_fields": ["completed", "assignee"]})

    # Iterating through the result as a list
    for i in list(tasksCompletedResult):

      # if there is no assignee...
      if(i["assignee"] == None):
        try:
          # ...assign to given assignee
          taskAssignresult = client.tasks.update_task(i["gid"], {'assignee': tokens["assigneeGid"]})
          numberOfTasksAssigned += 1
        except:
          print(colors.red + "it looks like something happened while assigning tasks to the provided assignee... Check your setup and try again.")

      # if it's been completed...
      if(i["completed"] == True):
        try:
          # ...move completed task to the done pile
          taskMovingResult = client.sections.add_task_for_section(tokens["donePileGid"], {"task": i["gid"]})
          numberOfTasksMoved += 1
        except:
          print(colors.red + "it looks like something happened while moving task(s) to the Done Pile... Check your setup and try again.")
    # Done Messages
    print(colors.green + "beep-boop: your Mitebox is all cleaned up!")

    if(numberOfTasksAssigned > 0):
      print(colors.green + str(numberOfTasksAssigned) + " task(s) assigned to the provided assignee.")

    if(numberOfTasksMoved > 0):
      print(colors.green + str(numberOfTasksMoved) + " completed task(s) moved to the Done Pile.")

  except KeyboardInterrupt:
    print(colors.reset + "xxxxxxxxxx")
    sys.exit()
  except:
    print(colors.red + "it looks like something happened when trying to get completed tasks in your Mitebox. check your setup and try again.")
    print(colors.reset)
  getUserInput()

# function for getting info on Mitebox
def getMiteboxInfo():
  x = 0
  try:
    result = client.tasks.get_tasks({"section": tokens["doPileGid"], "opt_fields": ["completed"]})

    resultList = list(result)

    for i in resultList:
      # if it's been completed
      if(i["completed"] == True):
        x += 1

    print(colors.green + "there are currently " + str(len(resultList)) + " Mites in your Do Pile")

    if x > 0:
      print(str(x) + " of them are/is completed. clean your Mitebox to move these to the Done Pile.")
  except KeyboardInterrupt:
    print(colors.reset + "xxxxxxxxxx")
    sys.exit()
  except:
    print(colors.red + "It looks like something happened when trying to get info on your Mitebox. Check your setup and try again.")
    print(colors.reset)
  getUserInput()

def getRandoMite():
  x = 0
  try:
    # when it hasn't found a completed task
    while x < 1:
      # get all tasks in to-do section
      result = client.tasks.get_tasks({"section": tokens["doPileGid"], "opt_fields": ["completed", "name", "permalink_url"]})
      # get random item 
      randoMite = random.choice(list(result))

      # if it hasnt been completed...
      if(randoMite["completed"] == False):
        # print("we found one!")
        print(colors.green + "hey! what about this: ")
        print(randoMite["name"] + "; you can access it here: " + randoMite["permalink_url"])
        x += 1
      else:
        print(colors.red + "i can pick one faster if you clean out your Mitebox first...")

  except KeyboardInterrupt:
    print(colors.reset + "xxxxxxxxxx")
    sys.exit()
  except:
    print(colors.red + "It looks like something happened when trying to get a random mite. Check your setup and try again.")
    print(colors.reset)
  getUserInput()

# PROGRAM START
if len(sys.argv) >= 2:
  createMite(sys.argv[1])
else:
  welcomeUser()