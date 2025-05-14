# Resume Project

## Project Description

This project is a dynamic Resume website deployed using AWS Lambda and GitHub Actions. It showcases your professional profile, skills, and experience.

## Project Structure

* **.github/workflows:** Contains the GitHub Actions workflow file (`resume.yaml`) for automated deployment.
* **src/index.html:** The HTML file for the resume website.
* **src/lambda\_function.py:** The Lambda function for handling backend logic (if any).
* **README.md:** Project documentation.

## Features

* Responsive Resume Website.
* Automated Deployment with GitHub Actions (CI/CD).
* Hosted using AWS Lambda.

## Prerequisites

* AWS Account with Lambda configured.
* GitHub Account.
* Basic knowledge of HTML and Python.

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd Resume-project
   ```
2. Modify `src/index.html` to customize your resume details.
3. Edit `lambda_function.py` if backend functionality is needed.

## GitHub Actions Deployment

* The `resume.yaml` workflow in `.github/workflows` handles the deployment.
* Any push to the `main` branch triggers the deployment.

## Usage

* Access the website through the deployed AWS Lambda endpoint.

