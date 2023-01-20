# machineLearningProject
ML end to end development


1. Github Account
2. Heroku Account
3. VS Code IDE
4. GIT Cli

Creating conda environment
....
conda create -p venv python==3.7 -y
....

Command to install flask is first create rquirements file and give Flask in that file and pip install -r rquirements.txt

To check remote url git remote -v

To setup CI/Cd pipeline in heroku we need below 3 information:
1) Heroku_email = gvineethkumarreddyrk@gmail.com
2) Heroku_API_key = e18755f5-0527-4a42-9bed-42e9b6be0b14
3) Heroku_App_Name = machine-learning-project

BUILD DOCKER IMAGE
docker build -t <image_name>:<tagname> .
Note: Image name for docker should be small letters(Lowercase)

To list docker images
docker images

To RUN docker image
docker run -p 5000:5000 -e PORT=5000 <dockerimageID>(need to give the image ID)
Here 5000 is the port number

To check runnig docker containers
docker ps

To stop docker conatainer
docker stop <container_ID>



python setup.py install

when we run pip install -r requirements.txt it will install only requiremnets.txt modules, if we wrote "-e ." it will install the packages(Where "__init__" contains) too.