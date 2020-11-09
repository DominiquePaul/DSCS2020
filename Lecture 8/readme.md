# Lecture 8

## Content

1. Cloud SDK
1. App Engine
    1. Overview
    1. Exercise: Deploy your own app with App Engine
1. Machine Learning APIs
    1. Translation
    1. NLP API
    1. Vision API
    1. Exercise: Run your own queries
1. AutoML
    1. Training
    1. Calling your API
    1. Exercise: train your own algorithm and query it with Python
  1. Short overview of Docker
1. Guest Lecture Stephan Schulze



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

### Exercise: Using the cloud sdk
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

Your app needs to contain (1) a .yaml file and (2) a requirements.txt file. We are already familiar with the requirements.txt file, so lets focus on the second.

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
* [App Engine documentation](https://cloud.google.com/sdk/gcloud/reference/app)
* [App Engine standard v. flexible](https://cloud.google.com/appengine/docs/the-appengine-environments)
* [More App Engine tutorials](https://cloud.google.com/appengine/docs/flexible/python/how-to)
* [Running Flask with Gunicorn](https://blog.ironboundsoftware.com/2016/06/27/faster-flask-need-gunicorn/)


## Google's AI APIs

1. Go to https://console.cloud.google.com/apis/credentials
1. Click "Create Credentials" and select "Service Account"
1. Enter a name of your choice e.g. "ml-api-account"
1. Select "Editor" as a Role
1. Skip adding any users to the account and press save
1. You should now see the service account name in a table with other service accounts
1. Click on the hamburger menu to the right of the service account (three vertical dots)
1. Select "Create Key" and select JSON. This should initiate a file download
1. Optionally place this json file in the gcp_credentials folder in the code folder of this repository (assuming you downloaded it)

To run the different APIs you will have to enable them first. To do this:

1. Go to the hamburger menu and choose the respective API in the Artificial Intelligence Group
1. Enable the the API
1. Optionally click on one of the links to view the documentation

For all of the APIs you have to have the google-cloud python package installed as well as the respective subpackages:

`pip install google-cloud`

`pip install google-cloud-language`

`pip install google-cloud-translate`

`pip install google-cloud-vision`


#### Natural Language API

* The NLP api can analyse:
    * the sentiment of an entire text and its individual sentence sentiment
    * the syntax of a text
    * specific objects in a text e.g. celebrities, special places
* It can identify individual languages automatically


#### Translate API

* It can translate any language into another, as if you were using google translate
* Languages have to be specified using a ISO 639-1 language code. See more about this[here](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)


#### Vision API

This is one of most versatile APIs. You can:
  * Identify objects in an image
  * Get the bounding boxes of images
  * Read text off of a picture
  * Detect landmarks
  * Detect Logos
  * and more


### Exercise
- Download your own service account credentials and play around with the APIs by replacing the input with your own
- Build small functions out of the APIs e.g. a translate function where you just have to enter the text
- Use the code from the documentation of the image api to analyse links of an image
- Use a vision API feature that is not in the code examples
- Combine your Unsplash code to get an image by a keyword and analyse it with the vision api

Exercise to do at home:
- Create flask page where a user can enter a keyword that you search for via the Unsplash API and render to the user. Also display what is in the image using the vision API
- Create a flask app where users can upload an image of their notes. Analyse the image and render a translated text to the user


## AutoML

1. Image Preparation
    1. Select the images you want to train your classified on and store them in two folders that correspond to the label names. You can use a chrome extension like [this one](https://chrome.google.com/webstore/detail/download-all-images/ifipmflagepipjokmbdecpmjbibjnakm) to bulk download images from a site like google images
    1. The AutoML_data_prep.py script creates a csv file that contains the image names and the respective label. Adjust it to the data you want to classify. Specifically look at (1) the folder names (2) the label names and the (3) name of the google storage folder (see next step)
1. Open the hamburger menu in GCP and open google storage. In the top level directory create a new folder that corresponds to the name of the folder that you specified in the python script. Make sure that the folder has the following settings: Location: us-central1, location type: Region, storage class: Standard.
1. Upload your image folders to this cloud storage bucket (drag and drop works)
1. Also upload the csv file that you created with the python script
1. Go to the hamburger menu and select Vision
1. Select Image Classication in the AutoML group
1. Select "New data set" give it a name of your choice and choose what you want to detect. We will go for single label classification
1. Choose "Select a CSV file on Cloud Storage"
1. Click on browse, select your csv file and then continue
1. GCP will now import the images. This may take a bit time
1. When the import is ready, click on Train and then on "start training". Give your model a name and keep "cloud hosted" selected
1. Click on "models" in the AutoML menu on the left.
1. Click on your model. You can view some statistics on how the training went. When you're done inspecting the metrics go to "Test % Use" and deploy the model



### Exercise
Create your own image classifier with AutoML and query it as an API with Python


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



## Guest Lecture Stephan Schulze
Some short profile information about Stephan
* Studied computer science at the Humboldt University in Berlin
* Now works as CTO at Project A, a Berlin based VC with a €200m fund, including portfolio investments such as Trade Public, Voi, Kry or Sennder
* At Project A Stephan leads a team of engineers working with start-ups at different stages with tasks ranging from consulting over to implementing fully professional IT systems and processes
