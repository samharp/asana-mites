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

### Create `.txt` files

Now, you will need to create the following text files to hold your sensitive data. Each file should include just one value: the respective value of the named file. Future implementations may use JSON instead of separate files:

  - `tokens/access-token.txt`
  - `tokens/workspace-gid.txt`
  - `tokens/assignee-gid.txt`
  - `tokens/project-gid.txt`

To access your Asana token or determine your GID values, you will first need to follow [these steps](https://developers-legacy.asana.com/docs/personal-access-token) to receive an API token, and then visit the Asana [documentation/Request tester](https://developers.asana.com/reference/createtask) to figure out your other GID values. You can also get respective GID values by deconstructing links to your project/task/etc.

```
www.asana.com/0/{project_gid}/{task_gid}
```


**NOTE:** Current implementation only allows for one Asana assignee, project, and workspace to be set to receive mites. This may change later, but due to the nature of what mites are, these small tasks shouldn't be dealt out to teammates: this is for you.

### Run the file!

To run the `mites.py` file, either double click on the file in your file explorer or `cd` to the folder where these files reside in Terminal/PowerShell. From there, you can run the file by entering `python mites.py`. You will be prompted to enter the name of your mite ("What is this teeny task?"), and will continue asking for more mites until you enter 'X' to exit.

## Reference

I spent a lot of time trying to find the best/easiest way to make these API requests, resulting in this Python implementation. In checking the [Asana documentation](https://developers.asana.com/reference/createtask), you can see that there are many ways to make these requests. I had a really rough time in trying to use curl (Windows PowerShell with Curl & JSON is, in simple terms, gross), and I also didn't want to host a web app using Node (maybe someday!).