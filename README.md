<img src="https://www.unisg.ch/-/media/93125423859d46928371a633b15cfcb1.jpg" alt="SIAW logo" width="200" align="right">

# Data Science and Cloud Solutions 2020
*by Dominique Paul* ()[dominique.paul@unisg.ch](mailto:dominique.paul@unisg.ch))

## About
The goal of this course is to efficiently teach you how to build simple applications with Python, that can be made available to technical teams as an API as well as non-technical users via a web interface and making these available to the public or small groups of specific users. The idea of the course is not to make you a full-fletch professional in Python, but teach you the most important concepts that you need in 90% of all cases, while highlighting which areas are not covered in detail and providing resources to these. While some previous experience in programming is advantageous, the course is designed for students without any previous programming experience but is high-paced.

This repository is designed for individuals following the lectures. It is fully documented with subfolder readme files and/or comments.

## Lecture Recordings
Recordings of the lectures can be found here:
[https://www.youtube.com/playlist?list=PLTqmw9Su79FZbIe29HSprhyOMgF8NALw5](https://www.youtube.com/playlist?list=PLTqmw9Su79FZbIe29HSprhyOMgF8NALw5)


## Course Structure

| Session       | Date        | Time        | Room         | Content  | Guest Lecture |
| -----------   | ----------- | ----------- | -----------  | ----------- | ----------- |
| 1             | 14. Sept.   | 8:15-12:00  | 23-103       | Introduction to and key concepts of cloud computing  |   |
| 2             | 21. Sept.   | 8:15-12:00  | 23-103       | Introduction to Python  |   |
| 3             | 28. Sept.   | 8:15-12:00  | 23-103       | Working with NumPy, Pandas, SciKit Learn and APIs  |   |
| 4             | 5. Oct.     | 8:15-12:00  | 23-103       | Flask basics, Webforms, HTML and Jinja2  |   |
| 5             | 12. Oct.    | 8:15-12:00  | 23-103       | Forms with files, CSS and Boostrap basics  |   |
| 6             | 19. Oct.    | 8:15-12:00  | 23-103       | Databases  | Nicole Büttner (Merantix Labs) |
| 7             | 3. Nov.     | 8:15-16:00  | 01-307 (moved online) | Introduction to GCP, setting up a server, introduction to git, Google App Engine, Cloud SQL, Google Data Studio  | Humberto Pereira (Dash Dash) |
| 8             | 3. Nov.     | 8:15-16:00  | 01-307 (moved online) | SQL, BigQuery, Cloud Functions, Cloud Storage  | Stephan Schulze (Project A Ventures)  |
| 9             | 4. Nov.     | 8:15-16:00  | 01-307 (moved online) | Machine Learning APIs, AutoML  |   |
| 10            | 7. Dec.     | 12:15-16:00 | 01-U201      | Presentation of Class Projects   |   |


## Grading
Grading is made up out of two parts
* **Programming assignments** taking place in the first half of the semester. The best 4 out of 5 assignments are counted towards the final grade. (50%)
* **A final course project** in which students work in groups to create an application that applied the contents of the course and additional features that are of interest to the individual groups (50%)


# Final Course Project

For the final course project you will work together in teams of 2-4 to build a flask app that solves a real or fictitious problem.

### Minimum requirements

* A flask app that has more than one route and has a nice styling that any non-technical user would find acceptable
* The app uses data in some way that generates value to a user
* The app is deployed on GCP and is accessible to other people on the internet
* Data is not stored locally, if you're app stores data then it should use the methods we covered in class

### Project Proposal
Each group has to submit a project proposal by end of day of the **11th of November**. The proposal should include the names of all team members and describe your project. Specifically it should include:

* The general idea and scope of the application
* An overview of the key features. These could be things like a login, upload forms, visualisations, analysis of specific data types, connections to another application
* The cloud products that you plan to use. Also include whether you are planning on using any other tools or services, e.g. specific APIs?
* Which parts you believe could by difficult to implement
* Different modules of development. Whats the most basic version of your app that you want to implement? What are the additional features you want to implement step by step after that? It is easy to overestimate how long some parts can take and thinking about different milestones can save you from not having a working application at the deadline

The proposal is required but not graded. Deviations from your original proposal are also fine. What I want to see is that you've put some thought into how you want to build the app, that you are aware of what the challenges will be, and have a plan if some parts take longer to implement than expected. I will give you feedback on whether the scope of the project is sufficient and share any resources that could be helpful.


### Submission
Projects are to be shared via Github. If you are working with a company or have any confidential data that you believe prevents you from sharing the code then let me know in advance. You can simply create a private repository and add me as a viewer to it.

Each Github repository should have a detailed readme including (1) A description of what the application can do (2) instructions of how to launch the application that a third person who only finds the repository could understand (3) description of the technical features of the app (4) a short text on the major challenges you experienced and how you solved them. The readme should look visually appealing and if relevant include screenshots of the working app. Include the names and emails of all team members. The **deadline for submission is 07.12.2020 at noon**.

### Presentation

Each team has 10-15 minutes to present and demo the application. You can use slides but are not required to. A part should explain why the app is interesting, but the majority should focus on the technical implementation. Talk about the problems you faced during implementation, what learnt and how you would approach the problem if you were to start over. Share your learnings with your classmates.

### Some general tips
* Work on something you find interesting and care about
* Work with team mates that have a similar skill level as you do
* Ask questions in Slack, if you're stuck or something isn't clear then ask
* Don't overengineer things. Start with a simple minimum viable product and add layers of complexity step by step
