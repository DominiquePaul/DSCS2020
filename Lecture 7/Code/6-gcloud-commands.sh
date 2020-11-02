# create a new server
gcloud compute instances create myserver --machine-type=e2-medium --image=ubuntu-1604-xenial-v20201014

# ssh into server
gcloud compute ssh myserver

# scp files
gcloud compute scp <file-name> myserver:

# for recursive files
gcloud compute scp --recurse <folder-name> myserver:

# copy file from server to local computer
gcloud compute scp <instance-name>:<file-path> <local-file-path>

# see all servers
gcloud compute instances list

# delete all servers
gcloud compute instances delete <instance-name>
