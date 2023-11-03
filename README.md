# asana-mites

Mites (patent-pending) are the tiny tasks that you think of throughout the day, "Oh yeah, I'll have to remember that when I get home." They never take longer than 5 minutes to complete (wash the dishes, water the plants, or feed the cat) - but when they start to pile up, they pile up fast.

Because I use Asana to handle work-related tasks, it only makes sense to include these mites on my Asana projects as well. However, creating tasks can sometimes be exactly that, a task. So tasks just need to be written down, they don't need to have assignees, projects, subtasks, or any kind of attachments. I used to keep these little things to do on a scrap of paper, but with separate to-do lists, inevitably things get forgotten/overlooked.

But no more! In using the Asana API, this project makes mite-creation as easy as it is to complete them. 

**NOTE:** This project uses Python 3.x to work. If you do not have Python installed on your machine, please do so [here](https://www.python.org/downloads/).

## How it works

### Clone/Fork this repo

I will assume you know how to do this, but if not, please consult your favorite search engine.

### Create a `/tokens` folder

This folder will hold all of the data that you don't want to go public (and in turn, out of your GitHub repo). It is automatically included in the `.gitignore`, but if you want to name the folder something else, go right ahead.

### Gather your token & GIDs

You have your private space for sensitive data, now you need the data.

First, you will need to request an Asana Access Token. Follow [these steps](https://developers-legacy.asana.com/docs/personal-access-token) to get your authentication token.

Next, you will need the GID values for your Asana workspace, project, assignee (most likely, yourself), and tag (to allow for easy searching later). You can pull these values by using the [Asana Request tester](https://developers.asana.com/reference/createtask) or by deconstructing links to your project/task/etc., like:

```
www.asana.com/0/{project_gid}/{task_gid}
```

### Create `tokens.json`

Now, you will need to create the following JSON file to hold your sensitive data. The file will include all of the token values & GIDs you gathered in the previous step. Your JSON file should look something like this:

```
{
  "accessToken": "1/1234567890:123XXX456XXX7890XXX",
  "assigneeGid": "1234567890",
  "projectGid": "1234567890",
  "workspaceGid": "1234567890",
  "tagsGid": "1234567890"
}
```

**NOTE:** Current implementation only allows for one Asana assignee, project, and workspace to be set to receive mites. This may change later, but due to the nature of what mites are, these small tasks shouldn't be dealt out to teammates: this is for you.

### Run the file!

To run the `mites.py` file, either double click on the file in your file explorer or `cd` to the folder where these files reside in Terminal/PowerShell. From there, you can run the file by entering `python mites.py`. You will be prompted to enter the name of your mite ("What is this teeny task?"), and will continue asking for more mites until you enter 'X' to exit.

Personally, I recommend creating a command within your bash Profile to easily launch this file. That way, you don't have to `cd` to this folder everytime, you can run it from any folder.

## Reference

I spent a lot of time trying to find the best/easiest way to make these API requests, resulting in this Python implementation. In checking the [Asana documentation](https://developers.asana.com/reference/createtask), you can see that there are many ways to make these requests. I had a really rough time in trying to use curl (Windows PowerShell with Curl & JSON is, in simple terms, gross), and I also didn't want to host a web app using Node (maybe someday!).