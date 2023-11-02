import asana
import json

# read file contents of necessary files
tokenFile = open("tokens/access-token.txt","r")
workspaceFile = open("tokens/workspace-gid.txt","r")
assigneeFile = open("tokens/assignee-gid.txt","r")
projectFile = open("tokens/project-gid.txt","r")

# set file contents to the value of each variable
tokenVal = tokenFile.read()
workspaceVal = workspaceFile.read()
assigneeVal = assigneeFile.read()
projectVal = projectFile.read()

# authenticate with access token
client = asana.Client.access_token(tokenVal)

loopVal = True

while loopVal == True:
  # get user input (what to name mite)
  miteVal = input("What is this mite? (X to Exit): ")

  if miteVal.lower() == 'exit' or miteVal.lower() == 'x':
    loopVal = False
  else:
    # send POST request
    result = client.tasks.create_task({"name": miteVal, "assignee": assigneeVal, "workspace": workspaceVal, "projects": [projectVal]}, opt_pretty=True)

