# Pneumonia-as-a-Service

## Overview
Pneumonia-as-a-Service is an innovative web-based application designed to leverage deep learning for the classification of chest X-ray images to detect pneumonia. This project encapsulates a VGG-16 model trained on a significant dataset of chest X-ray images, offering a preliminary assessment tool for pneumonia. The application is Dockerized for easy deployment and scalability, and it includes a continuous integration and continuous deployment (CI/CD) pipeline through Jenkins for seamless updates.

## Features

- **VGG-16 Convolutional Neural Network**: Utilizes the VGG-16 model, renowned for its effectiveness in image recognition tasks, specifically trained to detect signs of pneumonia from chest X-ray images.
- **Flask API**: Facilitates the interaction between the deep learning model and the front-end user interface, ensuring smooth and efficient handling of image uploads and predictions.
- **User-Friendly Interface**: Provides an intuitive web interface for users to upload X-ray images and receive immediate diagnostic feedback.
- **Dockerization**: The entire application is containerized using Docker, enhancing portability and deployment efficiency across any platform, including Kubernetes.
- **Automated CI/CD Pipeline**: Features a robust Jenkins pipeline for automating testing and deployment processes, ensuring that the application is always up-to-date and stable on a Kubernetes cluster hosted on AWS EC2 instances managed via Rancher.

## Getting Started

### Prerequisites

- Docker installed on your machine.
- An AWS account, if deploying on EC2 instances.
- Access to a Kubernetes cluster, for orchestrating the containerized application.
- Jenkins set up for managing the CI/CD pipeline.

### Installation and Local Deployment

1. **Clone the Repository**
   Clone the project to your local machine to get started.
   ```sh
   git clone https://github.com/yourusername/pneumonia-as-a-service.git
2. **Build the Docker Image**
   docker build -t pneumonia-as-a-service .
3. **Run the Docker Container on container port 80**
   docker run -p 5000:80 pneumonia-as-a-service

4. **Deployment to Kubernetes**
   Make your kuberentes cluster wherever you find convenient and deploy the service.yaml and deployment.yaml and then:
   ```sh
     kubectl apply -f k8s/deployment.yaml
     kubectl apply -f service.yaml


### Usage
   To use Pneumonia-as-a-Service, simply navigate to the deployed application's URL, upload a chest X-ray image through the web interface, and submit it. The system will analyze the image and display whether signs of pneumonia are detected.
### Contributing
   Contributions to Pneumonia-as-a-Service are welcome! If you have suggestions for improvements or new features, feel free to fork the repository, make your changes, and submit a pull request.
   
## Jenkins Pipeline Progress
![Jenkins Build Progress](/jenkins.png "Jenkins Build Progress")

## Kubernetes Cluster in Rancher
![Kubernetes Cluster](/clusters.png "Kubernetes Cluster in Rancher")


**I utilized EC2 instances within my university's AWS Learners' Lab to host all of these components. Due to several restrictions associated with the learners' account, it's likely that the URLs to my EC2 instances are no longer active. As a result, I am unable to provide URLs to my application. Instead, I am including all the essential files needed to replicate the setup. Attached screenshots serve as a visual guide to what you can expect if you successfully recreate a pipeline similar to mine.**
