<a name="readme-top"></a>
<br>
<h2 align="center"> CAP4001 Capstone Project | Vellore Institute of Technology-AP</h2>

<p> Project work carried out during the penultimate semester of study for the credits prescribed under University Core of the curriculum, related to the specialization of the programme by applying the knowledge gained in the courses we have undergone so far. </p>

<br>
<h1 align="center"> Prediction of Health Insurance Amount Using Deep Neural Network </h1> 

<!-- TABLE OF CONTENTS -->
<details>
  <summary style="font-size:22px;">Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#Contributing">Contributing</a>
    </li>
    <li>
      <a href="#Project-set-up">Project set-up</a>
    </li>
    <li>
      <a href="#links">Dataset links</a>
    </li>
  </ol>
</details>


## About The Project
<p>The goal of the project is to build a machine learning web application which can predict the health insurance amount of the user based on the inputs such as their age, gender, body mass index, marital status, region, etc. The lifestyle of an individual has the greatest impact on their health and therefore we collect user’s habits to train and test the model. Users will gain access to a predictive model which will help them to plan their medical expenses well ahead of any medical emergencies. This project aims to provide an insight about the amount associated with an individual for their health insurance. </p>

## Built with
<p>Flask, JavaScript, Azure, Docker,Visual Studio Code and Jupyter</p>
<img src="Images/Tools.jpeg" alt="Tools and Technologies" width="250"/>
<br>

<!-- Getting started -->
## Project set-up
1. Clone the repository.
  ```sh
  git clone https://github.com/SnehaVeerakumar/Predict-health-insurance-amount.git
   ```
2. Activate virtual environment.
  ```sh
  virtualenv venv
  venv\Scripts\activate
   ```
3. Install necessary python packages.
  ```sh
  pip install -r requirements.txt
   ```
4. Start the server
  ```sh
  python app.py
   ```

## Project set-up in Docker Desktop
1. Build using Docker Image
  ```sh
  docker build -t app_name:tag_name .
   ```
2. Run on port 5000
  ```sh
  docker run -p 5000:5000 app_name:tag_name
   ```

## Docker Hub Repository 
Link : https://hub.docker.com/r/snehaveerakumar/insuranceprediction
Pull Image
  ```sh
  docker pull snehaveerakumar/insuranceprediction
   ```
<br>

## Project folder description
1. Parent folder contains 3 important files.
<ul>
<li> app.py : Acts as the entry point to the application. It contains the URL routes and the codes for machine learning models.
<li> Dockerfile : Contains the instructions to build a docker image.
<li> requirements.txt : Contains the packages required to deploy the application.
</ul>

2. Folder : Code
<ul>Three sub folders in this folder contains the code for frontend and backend of the application. Jupyter Notebook has been used to analyse various machine learning models and deep neural network models and compared to select the best model using Mean Squared Error.</ul>

3. Folder : Dataset
<ul>Contains all the dataset that is required for the project. Processed data and user data will also get saved in this folder for the further processing</ul>

<!-- CONTRIBUTING -->
## Contributing

1. Fork the Project
2. Create your Feature Branch (`git checkout -b test`)
3. Commit your Changes (`git commit -m 'message'`)
4. Push to the Branch (`git push origin test`)
5. Open a Pull Request

## Project workflow
<img src="Images/project_flowchart.png" alt="Project workflow" width="400"/>

## Dataset links
1. Disease indicators : https://www.kaggle.com/datasets/cdc/behavioral-risk-factor-surveillance-system 
2. Insurance amount(insurance.csv) : https://www.kaggle.com/datasets/annetxu/health-insurance-cost-prediction

<p align="right">(<a href="#readme-top">back to top</a>)</p>
