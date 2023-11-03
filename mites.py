import asana
import json

# read file contents of necessary tokens/gids
tokensFile = open("tokens/tokens.json", "r")
# convert JSON to dict
tokens = json.loads(tokensFile.read())

# authenticate with access token
client = asana.Client.access_token(tokens["accessToken"])

loopVal = True
while loopVal == True:
  # get user input (what to name mite)
  miteVal = input("What is this mite? (X/C to Exit): ")

  if miteVal.lower() == 'exit' or miteVal.lower() == 'x' or miteVal.lower() == 'c':
    tokensFile.close()
    loopVal = False
  else:
    # send POST request
    result = client.tasks.create_task({"name": miteVal, "assignee": tokens["assigneeGid"], "workspace": tokens["workspaceGid"], "projects": [tokens["projectGid"]], "tags": [tokens["tagsGid"]]}, opt_pretty=True)
