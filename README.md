# Forest Fire Detection

The Dockerfile, model, input, interference, and output files are stored in a GitLab repository. Here's the GitLab link: Forest Fire Detection Repository.

Here is the GitLab link: https://gitlab.iotiot.in/PIAI23AUG2001/forest-fire-detection

  

## To implement the model using Docker, follow these steps:

1. **Clone the Repository:** Use the git clone command to clone the GitLab repository containing the Dockerfile and other essential files to your local Ubuntu machine.

   `git clone <repository_url>`
1. **Navigate to the Repository Directory:** Change into the directory of the cloned repository using the `cd` command.

   `cd <repository_directory>`
1. **Build the Docker Image:** Build the Docker image using the Dockerfile present in the repository. Utilize the docker build command for this.

   `docker build -t my_docker_image .`

   Replace my_docker_image with the desired name for the Docker image.
1. **Run the Docker Container:** Once the Docker image is successfully built, run a Docker container based on that image using the docker run command.

   `docker run -it --name my_container my_docker_image`

   Replace my_container with the desired name for the Docker container.
1. **Change Directory:** Navigate to the model directory using the cd command. `cd model`.
1. **Navigate to the Demo Folder:** Change directory to the demo folder using the cd command. `cd demo`.
1. **Run Inference File:** Execute the interference file using the following command.

   `python3 inference.py`
1. **Output Generation:** Output are generated in the `output` folder.
1. **Exit the Container:** To exit from the container use `exit` command.
1. **Stopping and Removing the Container (Optional):** When finished with the container, you can stop and remove it using the docker stop and docker rm commands, respectively.
   `docker stop my_container`

   `docker rm my_container`


This sequence of steps outlines how to deploy and use the forest fire detection model within a Docker container.


![image](https://github.com/user-attachments/assets/93cfec9e-b315-4063-b59f-db9e54606005)


Block-1

An image is to be given as an input to our object detection model.
We have used transfer learning approach to train our model and use the Yolov8n architecture.
From the knowledge the model has it detects the objects in the provided input image.

Block-2

The final result consists:

Bounding box around the detected objects.
Class labels associated with the objects and confidence scores indiicating the model's confidence in the detections.



Block-3

Dockerizing the object detection code.
Deploying the docker container on brainypi.


