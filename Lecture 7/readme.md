# Lecture 7

## Content
1. Introduction to Git
    1. Add, Commit and Push
    1. Solving a git conflict
    1. Markdown
    1. Ex. 1.1: Creating your first git repository
1. GCP Platform Overview
    1. Platform overview
    1. Product Category Overview
    1. Billing Alerts
1. Starting your first server
    1. Launching a server
    1. Connecting to your server
    1. Running a naked Flask app on a bare server (not recommended)
    1. Ex. 1: Run a basic flask app on a server
    1. Firewalls and networking
    1. Managing pip packages and virtual environments
    1. Running a Flask App on a server with docker
1. Networking and Security
    1. Connecting to your server from your desktop
        1. via ssh
        1. via gcloud
        1. Copying files to your server
1. Google App Engine
    1. Overview
    1. Testing load compared
1. Guest Lecture Humberto


## Introduction to Git

**Git** is a tool that allows you to track historic changes in your code, manage different versions of your project and collaborate with other team members or developers on a coding project. Git is 100% free and open-source. It is generally used for collaboration but you could use it locally as well, if you just care about tracking edits and versions of your code locally. Git itself is just a tool and not a company that offers any additional services.

One especially useful tool for collaboration are so-called branches: a branch is an independent line of development that allows you to clone your current work and track changes on this clone separately.

![git branches](./images/git_branches.svg "Title")

Tools like **Github, Gitlab or Bitbucket** can be used to host your codebases (a bit like you'd use icloud or google drive for other documents) which is essential for collaboration with other users. Github is the most popular and what we'll be using in this course. These are referred to as *remote repositories*

One key element that you need to understand in git are the three "trees":
1. **Your local working directory** on your computer
1. **The index**: this is also referred to as a staging area. You can use the index to build up a set of changes that you want to commit together. You can add files to the staging area using `git add`
1. **The HEAD**: The head is the part of git that points to your branches. The default branch is called "master". You can add staged files to the current branch your working on by using `git commit`.


You can exclude files that you don't want uploaded to github by creating a `.gitignore` file and naming the files there. You can either specify files by using their filename: `__pycache__`, `secrets.py` and even make more general rules like all files with a specific file ending: `*.env`. Each rule should be on a new line.

Most important commands:
* `git init` - create a new git repository
* `git remote add origin <your-remote-repository>` - Tell your computer which online repository you want to sync with
* `git add` - add files from your local directory to the staging area
* `git status` - displays the state of the working directory and the staging area. It lets you see which changes have been staged, which haven't, and which files aren't being tracked by Git
* `git commit` - record changes from the staging area to the git repository. Use `git commit -m '<your-message>'` to add a comment to your commit so others know which changes you made
* `git push` - Send changes from your local repository to your remote repository
* `git pull` - Fetch and download content and/or changes from a remote repository and immediately update the local repository to match that content
* `git clone` - Get a copy of an *existing repository*. Normally you would only do this once and use `git pull`to update it
* `git merge` - Merge two branches together, the structure is `git merge <branch-to-merge-onto-current-branch>`. You might have to resolve some conflicts in the code.
* `git checkout` - Move to another branch. This changes your current working directory to reflect the state of that branch
* `git branch` - Create a new branch to work on. Careful: you need to use `git checkout <branch-name` to move to that branch after using the branch command.
* `git log` - View history of commits made. Use `git log --oneline` to see a compact view. You can create a new branch off of a past commit using `git checkout <commit-hash>` or alternatively `git branch <new-branch-name> <commit-hash>`


### Markdown

Markdown is a simple markup language with a simple text formatting syntax. Its very useful to create simple text documents with basic styling conventions, without requiring a complicated text editing program like Microsoft Word. Markdown is often used for formatting readme files in Github repositories.

Here is an example of what you can do, the following markdown text...
```
# Hello world
## This is a subheading
### This is an even smaller heading

* You can create
* unordered lists
* like this

1. Ordered lists use numbers
1. but it doesn't matter which ones you use
1. Mardown infers the order
    1. and also works with indentation

You can also use html elements:
<img href="https://holidaystoswitzerland.com/wp-content/uploads/2019/10/St-Gallen-Switzerland-800x599.jpg">

Emojis also work :tada:

---
```

...converts to this:

# Hello world
## This is a subheading
### This is an even smaller heading

* You can create
* unordered lists
* like this

1. Ordered lists use numbers
1. but it doesn't matter which ones you use
1. Mardown infers the order
  1. and also works with indentation

You can also use html elements:
<img src="https://holidaystoswitzerland.com/wp-content/uploads/2019/10/St-Gallen-Switzerland-800x599.jpg">

Emojis also work :tada:

---

#### Further resources on git and version control:
* [What is version control? (Atlassian)](https://www.atlassian.com/git/tutorials/what-is-version-control)
* [Visualisation of git](https://git-school.github.io/visualizing-git/#free-remote)
* [Git - the simple guide](https://rogerdudler.github.io/git-guide/)
* [GitHub student package](https://education.github.com/pack)
* [Atom markup preview package](https://atom.io/packages/markdown-preview)


### Exercise 1: Your first git repository
- Sign up to Github if you don't have an account yet
- Create a new repository
- Open your terminal on your computer and move to a folder containing your last assignment (or any other folder with code)
- Initialise the repository and connect it to your repository that you created
- Add, commit and push a single file to your repository
- Add all other files to your repository
- Create a readme containing a few lines of markup. Include a link to a markup cheatsheet
- Bonus if you have extra time: Create a screenshot of your app, add it to the application folder (e.g. in a subfolder) and render it in your markdown.

Feel free to delete your repository after this exercise. If you like you can also showcase it as one of your first projects on GitHub and add some more detail to the readme after today's session.


## GCP Platform Overview

This course uses GCP. All links refer to the respective website for GCP, but other cloud providers have similar pages

## General GCP links and resources
* [GCP Homepage](https://cloud.google.com/)
* [Documenation](https://cloud.google.com/docs) containing a lot of examples
* [Example setups](gcp.solutions/)
* [Product Overview](cloud.google.com/products)
* [Price Calculator](cloud.google.com/free)
* [Free tiers](cloud.google.com/products/calculator)
* [Learning Resources](cloud.google.com/training)
* [Certifications](cloud.google.com/certification)
* [Customer Success / Consulting](cloud.google.com/consulting)


Also have a look at the video below for a general overview. The only additional aspect not in it is the overview of the console, when you log in.

[![Video on useful links](http://img.youtube.com/vi/VyZNJ7TlaWY/0.jpg)](http://www.youtube.com/watch?v=VyZNJ7TlaWY "Video on useful links")



### Console
The console is your "hub" when you log in to the cloud. The most important components are:
* General Project Information
* Resources currently in use
* Usage statistics of active resources
* Estimates billing charges
* Recent errors
* Product overview - this is in the hamburger menu on the left

You can also customise the console view by clicking on the button in the top right.


### Billing alerts and managing costs
Billing alerts help you to avoid a potential shock when you look at your credit card statement some time in the future.

1. Open the hamburger menu
2. Go to Billing
3. Open your billing account used (if not automatically selected)
4. Budgets and alerts
5. Create budget
  1. Enter a name
  1. Choose all projects
  1. Choose all services
  1. Make sure to de-select promotions
  1. Click next
  1. Select specified amount and enter e.g. $300 (total GCP free credit budget)
  1. Add threshold at e.g. every 10%
  1. Make sure that email notifications are ticked


General recommendations to save your credits in this course:
* Shut down any servers or other resources after the lectures or individual experimenting
* Try to use free tier products
* Use billing alerts

### How to add users to a project
1. Go to the GCP console
1. Create a new project (optional)
1. Click on "Add people to this project"
1. Enter the users email for GCP (she/he needs a GCP account)
1. Select the permissions you want to grant them. Generally you want to keep permissions for users at the minimum required, but for the course project you can keep things simple by selecting "Editor" or "Owner"

## Starting your first server

### Launching a server

1. Open the hamburger menu
1. Go to "VM Instances"
1. Create
1. Enter a name and select settings
1. Tick "allow http traffic" and "allow https traffic" if you want to make your server available to the web
1. Click create

**Some general recommendations:**
* Choose a region that is close to where you are. Any Europe West server will generally do. Note that different regions are associated with different costs of the instance. Belgium and Finland generally tend to be cheaper regions.
* Choose a small machine type. For our course e2-micro and e2-small are more than sufficient
* The boot disk determines the operating system of your machine. Ubuntu generally is a good choice, but there are many good alternatives.



### SSH into server via the web interface
By clicking on "ssh" you can enter the server directly and interact with it just like you would with your computer via the terminal.

Remember that GCP provides us with servers in the most bare format. This means that only a few very basic programs are installed.

The ubuntu version that we get does not necessarily have to be the latest version. Newer versions might contain updates making the server faster or securer. We can update to the newest version by running two commands
<br>
`sudo apt-get update` - downloads the updates <br>
`sudo apt update` - installs the updates

We can also combine two commands in the command line using "&&" like this: <br>
`sudo apt-get update && sudo apt update`

Updating your server when you start it isn't necessary, but its a good habit.

### Upgrading to Python 3.8 on Ubuntu
To upgrade Python run these commands

```
sudo add-apt-repository ppa:deadsnakes/ppa

sudo apt update

sudo apt install python3.8

sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 2
```

To use Python 3.8 as the default python3, run commands:


#### Installing pip
`sudo apt install python3-pip` - download and install pip
<br>
`pip3 --version` - check that everything works
<br>
`pip3 install flask` - install packages, in this case flask


### Firewalls and networking
If we now open the external IP of our server we still can't see the application. This is due to the default firewall rules of GCP. Even though we ticket the "allow http traffic" buttons, we still need to set rules what specifically we mean with this. To do this go to:

Hamburger menu with GCP products & services > VPC Network > Firewall

This is where we can create firewall rules. In our case we need to create a firewall rules with these:
* Enter `http-server` and/or `https-server` in the "target tags" field
* Either enter a specific IP address to limit access only to specific locations (you can e.g. just google "my ip address" to get yours) or you can enter "0.0.0.0/0" which means that anybody can access the application
* For "Protocols and Ports" you can then select specific TCP ports you want to open up. The ports are exactly the same concept that we visited with our flask apps, when we set the port to be 5000, 80 or another port number
* Add tcp:80 in the Protocols & Ports box, or tcp:443 for HTTPS traffic

After creating this rule you should be able to open the external IP of your application and see your flask app. Depending on which IP addresses you added to the rule, everybody in the world will be able to see this.

If you decide to run multiple flask apps on the same server then you can use firewall rules to restrict access to each app, depending on the port it is running on.

If you're interested in more details on how firewalls work then have a look at [this post](https://www.digitalocean.com/community/tutorials/what-is-a-firewall-and-how-does-it-work)


### Exercise 1.2:  Run a basic flask app on a server

- Launch a server
- Set up a general firewall rule that permits webtraffic to the app
- Open the web-based ssh terminal
- Update the server, install pip, install flask with pip
- Copy the basic flask template to the server
- Run the app and inspect it in the browser


### Managing pip packages and virtual environments

In bigger projects we will be working with many flask packages and it is hard to keep track of all of them. Generally you will be developing on your local computer. When you start a new server, then you will have to install all of these packages again on the server which can be quite lengthy. Luckily there are convenient ways we can make this easier.

#### Requirements.txt
We can summarise all pip packages that we have installed locally by saving them as a .txt file. requirements.txt is not a required name, but rather a convention.
`pip3 freeze > requirements.txt`

We can install packages from such a file on another computer/server by running
`pip3 install -r requirements.txt`


#### Setting up local environments

You can install the virtual environment package with pip
`pip3 install virtualenv`

And create a new virtual environment like this

`python3 -m venv <your-virtualenv-name>`


This creates a folder in your directory with the name you specified containing the following contents:

* **bin** - files that interact with the virtual environment
* **include** - headers for the c language to compile python packages
* **lib** - a copy of the Python version with a folder where each dependency is installed


You can activate an environment by calling:

`source <your-env-name>/bin/activate`

In the command line you can now install packages as if you were in a fresh environment. You can also run your flask application in it

`pip install <package-name>`


You can deactivate the virtual environment by executing

`deactivate`

Any packages that you installed in the virtual environment will not be available in the global environment and vice versa (unless they were already installed there before)

Virtual environments are a best-practice in programming to separate different programming project environments from another. What you will often do is export a requirements.txt file from your virtual environment to load it into your flask app on your server.


### Connecting to your server from your local computer

We can also connect to our server from our own terminal using a secure shell (SSH).

We first need to generate an ssh key

`ssh-keygen -t rsa`

The `-t` flag specifies the type of encryption, which in this case is RSA, a typical encryption standard.

Follow the instructions on screen, you can decide to add a password that will be prompted everytime you use the key, but you can leave this blank by just hitting enter twice. The command should create two keys, the private and the public key. The private key stays on your server, while the public key is stored on the server

Follow these steps to connect to the server via ssh:
* Create a ssh key using the ssh-keygen command above
* type `ls` or `dir` to see that the two keys were created
* open the .pub key by opening the file in your finder or by running `cat <filename>`. Copy the content
* Open your server setting by clicking on its name in GCP then on "edit"
* At the bottom you should be able to see a group of settings called "ssh keys". Click on "show and edit"
* Paste the contents of the public key into here
* Click save

You can know enter the server from your computer by running the command below. Note that it might take a few seconds for the changes to take effect

`ssh -i <file-path-to-private-key> <username>@<server-ip-address>`

`-i ` is a flag indicating that we want to specify a private key to connect.
`username` this is the username with which you will log in to the machine.
`server-ip-address` the public ip of the machine

If you are a windows user then you might need to install ssh manually:
[Instructions](https://www.howtogeek.com/336775/how-to-enable-and-use-windows-10s-built-in-ssh-commands)

On windows, you can also use a service like putty which is very popular:
[Putty guide](https://www.ssh.com/ssh/putty/windows/)

Once you are logged into your server you can do the same as with the ssh terminal provided in your browser. You can exit the terminal anytime by typing `exit`

####  Copying files to your server with Secure Copy Protocol (SCP)
Copying files to your server by copy paste is quite annoying. Instead, we can send them to the server in a similar way as we did with ssh.

SCP is safe way to send files from one computer to another. Its a convenient way to send files from your computer to a server. You can use the command like this:

`scp -i my_private_ssh_key main.py dominiquepaul@34.65.161.3:code/flaskapp`

The more abstract structure of the command is

`scp -i <private-ssh-key> <file-to-send> <server-username>@<server-address>:<filepath-on-server>`

To upload entire folders we can add an `-r` flag, which is short for recursive. The structure of the command then changes to
`scp -i -r  <private-ssh-key> <folder-to-send> <server-username>@<server-address>:<filepath-on-server>`


### Exercise 1.3: SSH into a server from your local terminal and run one of your flask apps

- Open the folder for any of your flask apps in your local terminal
- Create a virtual environment and activate it
- Try and run the flask app. Install the missing packages in your virtual environment until it works
- Export the pip packages to a requirements.txt file
- Launch a second server
- Add a custom tag to it e.g. "my-firewall-rule"
- Create a custom firewall rule to it, only allowing your computer to access it (google for your ip address)
- Send your app to the server via SCP (you will have to add an ssh key to the server first)
- SSH into your server and start the application
- update the server, install pip and the install all the packages from the requirements.txt file
- Run your flask app. Make sure that everything works by opening it in your browser
- Try opening the ip address on your phone
- Adjust the rule to permit all ip addresses to the IP address and reload the page on your phone (you might have to wait a bit)

### Short note on start-up scripts

You can create scripts that run automatically when a server is started. These scripts are generally referred to as bash scripts and are just grouped command line commands

You can add the start-up script via copy paste by opening the toggle menu "Management, security, disks, networking, sole tenancy" when creating a new virtual machine. Alternatively you can link to a start-up script stored in a google cloud storage folder.

See the file `start-up-script.sh` for an example of what such a file could look like

<img src="https://jirasupport.files.wordpress.com/2019/10/docker_logo.png" alt="docker" width="200" align="right"/>


### Docker

Docker is a set of platform as a service products that use virtualisation to package your applications as so-called containers. Containers are isolated from one another and bundle their own software, libraries and configuration files.

What I like especially about docker is that its very simple to run multiple flask apps without having to launch a new server for each one. Especially if some apps are inactive most of the time.

See Docker example in Code folder

![docker v. virtualisation](https://about.gitlab.com/images/blogimages/containers-vm-bare-metal.png)


#### Further resources on Docker
* [Docker homepage](http://docker.com/)
* [How To Build and Deploy a Flask Application Using Docker on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-build-and-deploy-a-flask-application-using-docker-on-ubuntu-18-04)
* [Dockerize your flask application](https://runnable.com/docker/python/dockerize-your-flask-application)
* [Get started with docker compose and flask](https://docs.docker.com/compose/gettingstarted/)


## The Cloud Software Development Kit (SDK) / gcloud

### Installation instructions
Download the cloud SDK here: https://cloud.google.com/sdk/docs/quickstart

1. Place the file in a higher-level folder on your computer
1. Unzip the file
1. Open your terminal and open the folder you placed the file in
1. Run `./google-cloud-sdk/install.sh`, you will be prompted with some questions.
  1. When asked whether you want to update your $PATH and enable shell command completion respond with yes
  1. When asked about a path to an rc file then just hit enter to accept the default unless you have any special configurations that you did yourself. I assume you know what you're doing then anyways.
1. Close and open the terminal once the installation finishes for the effects to take place
1. In the new shell enter `gcloud init`
1. Authenticate in the browser
1. Pick the project you have set up for the course
1. Select a default region. You can look up the regions [here](https://cloud.google.com/compute/docs/regions-zones), I like to choose europe-west-1-b in Belgium as it tends to be cheap and is fairely close to where I am


### Some useful commands

#### Create a new server
We can create a new server using the command line like this now:

`gcloud compute instances create myserver --machine-type=e2-medium --image=ubuntu-1604-xenial-v20201014`

The more abstract format of this is

`gcloud compute instances create <your-server-name> --machine-type=<server-size> --image=<image-type>`

This command looks quite complicated, so you often will rather want to use the web interface. There, you can also always access what the web interface would look like as a gcloud command. Look at the very bottom for "Equivalent REST or command line"

One convenient use case is ssh-ing into a server using the gcloud command line

`gcloud compute ssh <server-name>`

or scp files there

`gcloud compute scp <file-name> <instance-name>:`

for recursive files

`gcloud compute scp --recurse <folder-name> <instance-name>:`

You can also copy files from your server to your local file system:

`gcloud compute scp <instance-name>:<file-path> <local-file-path>`

To see all servers

`gcloud compute instances list`

Delete a server

`gcloud compute instances delete <instance-name>`

We will cover other commands as we get familiar with othe products

### Exercise 3: Using the cloud sdk
- Install the cloud sdk and set it up
- Create a new server and ssh into it to make sure that everything works
- Exit the server and send a folder with an app of your choice to the server using gcloud and send one of your previous flask apps to the server via gcloud and scp
- Run the app on the server (you might need to install some pip packages)
- Send a file from the server back to your local computer
- Delete the instance


## App Engine

Launching servers isn't necessarily hard, but can involve quite a few steps. This can be alright, but sometimes we just want to make our app run as quick as possible. Also, one scenario we have not considered yet is what happens when we get a lot of users / traffic and we need to scale our infrastructure.

Google App engine offers a convenient solution to run python applications without having to worry about any server updates, installations or firewall rules.

App engine gives you two options to run your application "standard" and "flexible". The differences are quite technical, but essentially its about how the applications are run. If you are interested you can read up on the details [here](https://cloud.google.com/appengine/docs/the-appengine-environments). Generally, the flexible version gives us a bit more flexibility so we will be using it in this course.

Your app needs to contain (1) a .yaml file and (2) a requirements.txt file

### The .yaml file

The yaml file contains the configurations of your python app such as the CPU, memory and scaling configurations. I have included two example configurations in the Code folder. The basic configuration is configured to a low limit just for experimenting with the service. The normal configuration is what you would deploy the app in production with, this is configured to automatically scale the servers if the app gets more traffic

### Deploying the app

To deploy the app simply run

`gcloud app deploy <yaml-file>`

This can take some time. Until the app has been deployed you can not re-deploy it. To view the list of past operations you can run

`gcloud app operations list`

To open your app in a browser once it has deployed run

`gcloud app browse`

Per default traffic is permitted from all sources. You can view the firewall rule(s) by running:

`gcloud app firewall-rules list`



#### Additional resources on app Engine
[App Engine documentation](https://cloud.google.com/sdk/gcloud/reference/app)
[App Engine standard v. flexible](https://cloud.google.com/appengine/docs/the-appengine-environments)
[More App Engine tutorials](https://cloud.google.com/appengine/docs/flexible/python/how-to)
