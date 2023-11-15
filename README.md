# Using Asana's API to create Mites (small, yet pesky tasks) in Terminal

Mites (patent-pending) are the tiny tasks that you think of throughout the day, "Oh yeah, I'll have to remember that when I get home." They never take longer than 5 minutes to complete (wash the dishes, water the plants, or feed the cat) - but when they start to pile up, they pile up fast.

Because I use Asana to handle work-related tasks, it only makes sense to include these mites in Asana as well. However, creating tasks can sometimes be exactly that, a task. Some tasks just need to be written down - they don't need to have assignees, projects, subtasks, attachments, or any of the other features project management systems provide. I used to write these little to-do's on a scrap of paper, but with separate to-do lists, inevitably things get forgotten and overlooked.

But no more! In using the Asana API, this project makes mite creation and management as easy as it is to complete them. 

**NOTE:** This project uses Python 3.x to work. If you do not have Python installed on your machine, you can get it [here](https://www.python.org/downloads/).

<br>

## Before We Start

### Vocabulary

To make things as clear as possible, let's get some terminology out of the way. Assumingly, you are familiar with what Asana workspaces, assignees, projects, sections, and tasks are. Based on these, you should also know:

- **Mite:** The simple Asana task that probably just has the title of something you are needing to do
- **Mitebox:** The Asana project where these mites will live
- **Do Pile:** The Asana section where mites are placed on creation (Your "To-Do" list/column)
- **Done Pile:** The Asana section where mites marked as "Completed" are placed (Your "Done" list/column)

<br>

## Setting Up

### Clone/Fork this repo

I will assume you know how to do this, but if not, please consult your favorite search engine.

### Create a `/tokens` folder

This folder will hold all of the data that you don't want to go public (and out of your GitHub repo). It is automatically included in the `.gitignore` file (if included in `root`), but if you want to name the folder something else, don't forget to update the `.gitignore` file accordingly.

### Gather your token & GIDs

You have your private space for sensitive data, now you need the data itself.

First, you will need to request an Asana Access Token. Follow [these steps](https://developers-legacy.asana.com/docs/personal-access-token) to get your authentication token.

Next, you will need the GID values for your Asana workspace, Mitebox, Do Pile, Done Pile, assignee (yourself), and tag (it's recommended to create a "Mite" tag in Asana to allow for easy searching/managing). You can pull these values by using the [Asana Request tester](https://developers.asana.com/reference/createtask) or by deconstructing links to your project/task/etc., like:

```
www.asana.com/0/{project_gid}/{task_gid}
```

### Create `tokens.json`

You will need to create the following JSON file to hold your token values & GIDs that you gathered in the previous section. Your JSON file should look something like this (where the values on the right are replaced with your values):

```
{
  "accessToken": "1/1234567890:123XXX456XXX7890XXX",
  "workspaceGid": "1234567890",
  "assigneeGid": "1234567890",
  "miteboxGid": "1234567890",
  "doPileGid": "1234567890",
  "donePileGid": "1234567890",
  "tagsGid": "1234567890"
}
```

**NOTE:** Current implementation only allows for one Asana workspace, Mitebox, and assignee. This may change later, but due to the nature of what mites are, these small tasks shouldn't be categorized anyways (and if they do need to be, they probably aren't mites, but *tasks*).

<br>

## Running the thing

To run the `mites.py` file, either double click on the file in your file explorer or `cd` to the folder where these files reside in Terminal/PowerShell. From there, you can run the file by entering:

```
python mites.py
```

**NOTE:** Personally, I recommend creating a command within your bash_profile/PowerShell Profile to easily launch this file. That way, you don't have to `cd` to this folder every time, you can run it from any folder.

As the program will state, you may then either enter the title of your mite, or give it a command to manage your mites.

### Creating a Mite

To create a new mite, simply enter the title of your new mite. This can be whatever wild and zany task you like (and are afraid of forgetting).

Alternatively, you can create a mite at the same time as calling the file. To do this in Terminal/PowerShell, pass the name of the mite as an argument:

```
python mites.py "the name of my mite in quotes"
```

### Management Commands

Additional commands allow for simple management of your mites. Most management (renaming, markingas complete, etc.) will need to be done inside Asana, but the following commands allow for management within Terminal/PowerShell:

- **'C' to clean**: Move all of your completed mites to the Done Pile.
- **'I' for info**: Get basic information on your Mitebox, like how many mites are incomplete, how many you've completed, and easy links to access your Mitebox
- **'X' to exit**: Simply exit the mite-creation loop and exit the program

<br>

## Reference

I spent a lot of time trying to find the best/easiest way to make these API requests, resulting in this Python implementation. In checking the [Asana documentation](https://developers.asana.com/reference/createtask), you can see that there are many ways to make these requests. I had a really rough time in trying to use curl (Windows PowerShell with Curl & JSON is, in simple terms, gross), and I also didn't want to host a web app using Node (maybe someday!).
