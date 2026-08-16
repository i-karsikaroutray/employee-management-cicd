# Employee Management System — AWS & CI/CD

## Project Overview

This project is a Flask-based Employee Management System deployed on AWS and integrated with a CI/CD pipeline.

The application runs inside a Docker container on an Amazon EC2 instance. Employee data is stored in Amazon RDS MySQL. Jenkins automates the build and deployment process whenever new code is pushed to the GitHub repository.

## Architecture

```text
                         User Browser
                              |
                              v
                    +-------------------+
                    |     AWS EC2       |
                    |                   |
                    |     Jenkins       |
                    |        |          |
                    |     Docker        |
                    |        |          |
                    |   Flask App       |
                    +--------|----------+
                             |
                             v
                    +-------------------+
                    |    Amazon RDS     |
                    |     MySQL DB      |
                    +-------------------+

Developer
    |
    v
  GitHub
    |
    | GitHub Webhook
    v
  Jenkins
    |
    | Docker Build & Deploy
    v
  EC2
```

## Technologies Used

* Python
* Flask
* MySQL
* AWS EC2
* AWS RDS MySQL
* Docker
* Jenkins
* Git
* GitHub
* GitHub Webhooks
* Linux
* AWS Security Groups

## Application Features

* Add Employee
* View Employees
* Store employee information in MySQL
* Retrieve employee information from the database
* Web-based employee management interface

## AWS Services Used

### Amazon EC2

EC2 is used to host the application, Docker container, and Jenkins server.

### Amazon RDS

RDS MySQL is used as the managed relational database for storing employee information.

### Security Groups

Security groups are used to control network access to:

* Jenkins — port 8080
* Flask application — port 5000
* RDS MySQL — port 3306

## Docker

The Flask application is containerized using Docker.

The Docker image is built using the project's `Dockerfile`.

Example:

```bash
docker build -t employee-management-app .
```

The application runs as a Docker container:

```bash
docker run -d -p 5000:5000 --name employee-app employee-management-app
```

## Jenkins CI/CD Pipeline

Jenkins is used to automate the application build and deployment process.

### Pipeline Workflow

```text
Developer
    |
    v
GitHub
    |
    | Push
    v
GitHub Webhook
    |
    v
Jenkins
    |
    v
Clone Source Code
    |
    v
Build Docker Image
    |
    v
Stop Existing Container
    |
    v
Start New Container
    |
    v
Application Deployed
```

### Jenkins Stages

The pipeline contains the following stages:

1. **Clone**

   * Jenkins retrieves the latest source code from GitHub.

2. **Build Docker Image**

   * Jenkins builds a new Docker image using the Dockerfile.

3. **Deploy**

   * Jenkins removes the previous application container.
   * Jenkins starts a new container using the latest Docker image.
   * The RDS database configuration is supplied through the `.env` file.

## GitHub Webhook

A GitHub webhook is configured to automatically trigger Jenkins when code is pushed to the `main` branch.

```text
Git Push
   |
   v
GitHub
   |
   v
Webhook
   |
   v
Jenkins
   |
   v
CI/CD Pipeline
```

This removes the need to manually click **Build Now** after every code change.

## Database Configuration

The application connects to Amazon RDS MySQL using environment variables.

Example:

```text
DB_HOST=<RDS_ENDPOINT>
DB_USER=<RDS_USERNAME>
DB_PASSWORD=<RDS_PASSWORD>
DB_NAME=<DATABASE_NAME>
```

The `.env` file is not committed to GitHub because it contains sensitive database credentials.

## Project Workflow

1. Developer modifies the application.
2. Developer pushes the changes to GitHub.
3. GitHub sends a webhook notification to Jenkins.
4. Jenkins automatically starts the pipeline.
5. Jenkins clones the latest code.
6. Jenkins builds the Docker image.
7. Jenkins stops the old application container.
8. Jenkins starts a new container.
9. The Flask application runs on EC2.
10. Flask connects to Amazon RDS MySQL.
11. Users access the application through the EC2 public address.

## Application URL

```text
http://<EC2-PUBLIC-IP>:5000
```

## Screenshots

### Employee Management Application

<img width="1912" height="1002" alt="app-ui" src="https://github.com/user-attachments/assets/c0de73f5-0ada-48f7-a0b2-04b762a7e928" />


### AWS EC2 Instance
<img width="1918" height="925" alt="ec2" src="https://github.com/user-attachments/assets/c5870a4d-eaa9-4e89-b7a8-5a3e6df46ad5" />



### Amazon RDS Database

<img width="1917" height="922" alt="RDS" src="https://github.com/user-attachments/assets/86321c8d-9254-4559-8330-415e744d4119" />


### Docker Container

*Add Docker screenshot here.*

### Jenkins Pipeline

*Add Jenkins successful pipeline screenshot here.*

### GitHub Webhook

*Add successful GitHub webhook screenshot here.*

## Project Structure

```text
employee-management-cicd/
│
├── app.py
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   ├── index.html
│   ├── add_employee.html
│   └── view_employees.html
│
└── static/
    └── style.css
```

## Key DevOps Concepts Practiced

* Linux server administration
* AWS EC2
* AWS RDS
* AWS Security Groups
* Git and GitHub
* Docker containerization
* Docker image creation
* Jenkins CI/CD
* GitHub Webhooks
* Automated deployment
* Environment variables
* Application and database connectivity

## Future Enhancements

* Infrastructure as Code using Terraform
* Kubernetes deployment
* AWS Load Balancer
* HTTPS using a domain and SSL certificate
* Monitoring and logging
* Better Jenkins credential management
* AWS Secrets Manager for database credentials

## Project Outcome

This project demonstrates an end-to-end DevOps workflow where application code is stored in GitHub, automatically built and containerized using Jenkins and Docker, deployed to an AWS EC2 server, and connected to an Amazon RDS MySQL database.

The project demonstrates practical experience with:

```text
GitHub
   ↓
Jenkins
   ↓
Docker
   ↓
AWS EC2
   ↓
Flask Application
   ↓
AWS RDS MySQL
```
