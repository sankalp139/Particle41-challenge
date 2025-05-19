# Particle41-challenge
## Task-1

The docker image for simpleTimeService is created and pushed to Docker Hub.

### Pre-requisites:
In order to run the Docker image, you need to have Docker installed on your system

Windows/macOS: Install Docker Desktop https://docs.docker.com/desktop/setup/install/windows-install/
Linux: Install Docker Engine using your distro's package manager:
            sudo apt update
           sudo apt install docker.io  

### Steps:

1.	To pull the docker image run:
                docker pull sankalp139/simple-time-service:latest

2.	once the image is pulled successfully you can run ‘docker image ls’ to verify
    
3.	To run the docker image locally:
       docker run -p 5000:5000 simple-time-service:latest


4.	To check whether the image is running 
        Curl  http://localhost:5000 or type  http://localhost:5000 in browser
   And you should get the output as
{"ip":"value","timestamp":" value"}






## Task-2

To run the application container in cloud I have used AWS .

### Pre-requisites:

In order to run the Terraform file you need to setup AWS CLI on your system 
https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html

once AWS CLI is setup you will have to configure your Aws account to the CLI

https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html 


Ensure that Terraform is installed on your system.

https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli


### Steps:

1.	Clone the Repository and copy the entire folder named 'terraform'
2.	Go to the folder location in Terminal and run ‘terraform init’
3.	Run Terraform plan to see the set of resources available for creation
4.	To verify check that there are 29 resources waiting to be created.
5.	Run terraform apply to create the setup in your Aws
6.	At the end of the run if everything works  out you should get the load balancer url in output
7.	Type the url in browser and the application should be visible with json output.
