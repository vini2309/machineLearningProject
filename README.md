# Housing Prediction

## Objective
Welcome to Machine Learning Housing Corporation! The goal of this project is to build a model to predict housing prices in California using census data. This dataset includes metrics such as population, median income, and median housing price for each block group in California. These block groups will be referred to as "districts." The model should learn from this data and predict the median housing price in any district given the other metrics.

## Table of Contents
- [Main Steps for Machine Learning Projects](#main-steps-for-machine-learning-projects)
- [Installation Instructions](#installation-instructions)
- [Usage](#usage)
- [Libraries and Dependencies](#libraries-and-dependencies)
- [Project Structure](#project-structure)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Main Steps for Machine Learning Projects
1. Look at the big picture.
2. Get the data.
3. Discover and visualize the data to gain insights.
4. Prepare the data for Machine Learning algorithms.
5. Select a model and train it.
6. Fine-tune your model.
7. Present your solution.
8. Launch, monitor, and maintain your system.

## Installation Instructions

### Prerequisites
- GitHub account
- VS Code IDE
- Python 3.x

### Setup
1. **Create a GitHub Repository**
   - Clone the repository to your system:
     ```bash
     git clone <github-url>
     ```
   - Open the folder in VS Code.

2. **Project Folder Structure**
   - Download and run the initial bash script:
     ```bash
     bash <script_name>
     ```

3. **Setup Python Environment**
   - Update `setup.py` with:
     ```python
     from setuptools import setup, find_packages

     REQUIREMENT_FILE_NAME = "requirements.txt"
     REMOVE_PACKAGE = "-e ."

     def get_requirement_list(requirement_file_name=REQUIREMENT_FILE_NAME) -> list:
         try:
             requirement_list = None
             with open(requirement_file_name) as requirement_file:
                 requirement_list = [requirement.replace("\n", "") for requirement in requirement_file]
                 requirement_list.remove(REMOVE_PACKAGE)
             return requirement_list
         except Exception as e:
             raise e

     setup(
         name="Housing price prediction",
         license="MIT",
         version="0.0.0",
         description="Project has been completed.",
         author="Avnish Yadav",
         packages=find_packages(),
         install_requires=get_requirement_list()
     )
     ```

## Libraries and Dependencies

Add the following libraries to `requirements.txt`:
```plaintext
scikit-learn
scipy 
PyYAML
gunicorn
pandas
-e .
six
dill
Flask

Usage
Running Locally
Create a app.py file with a sample Flask app:
python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)

To send changes to GitHub:
Stage changes: git add .
Check status: git status
Commit changes: git commit -m "<message>"
Push changes: git push origin main
Deployment
Heroku Deployment
Create an account on Heroku and create an app.
Gather these details for GitHub Actions setup:
Heroku API Key
Heroku App Name
Heroku Account Email ID
Docker Setup
Create .dockerignore and Dockerfile.
Add necessary configurations in .github/workflows/main.yaml.
Add repository secrets in GitHub under Settings > Secrets.
Update .dockerignore with folders not needed in Docker image.
Push changes to GitHub for CI/CD setup.
Contributing
Follow these steps to contribute:
Fork the repository.
Create a new branch (git checkout -b feature/YourFeature).
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature/YourFeature).
Open a pull request.
License
This project is licensed under the MIT License.
Acknowledgments/References
Thank you to all contributors and resources that supported this project.
