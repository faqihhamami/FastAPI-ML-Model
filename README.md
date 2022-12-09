# FastAPI-ML-Model

- Goal: Learn about FastAPI to create an API that serves sales prediction model.

## Technologies
- Scikit-Learn
- FastAPI
- Docker

## Run the API
- Open terminal / cmd and type `uvicorn main:app --reload`
- Open browser and type `http://127.0.0.1:8000`
- or open `http://127.0.0.1:8000/docs`

### using swagger UI
- Open http://127.0.0.1:8000/docs and choose  `POST /predict`
- Click : `Try it out`
- Input request body 
```
{
  "tv": 292.9,
  "radio": 0,
  "newspaper": 0
}
```
- Click `Execute`

### using postman
Open Postman and input request body 
```
{
  "tv": 292.9,
  "radio": 0,
  "newspaper": 0
}
```
Click `run`

### using python
Run using python requests
```
python request_post.py
```

## Conda environment
It is better to run on python environment. 
1. create conda environment
```
conda create --name fastapi-sales-pred
```

2. Activate the conda environment:
```
conda activate fastapi-sales-pred
```

3. Install the project dependencies:
```
pip install -r requirements.txt
```

## Deployement
Deploy Fast API using docker. Make sure you have installed Docker in your system. 
1. Deploy model using docker
```
docker build -t fastapi-sales-pred . 
```

2. Run container on background
```
docker run -d -p 8900:8900 fastapi-sales-pred
```

## Docker container
show all images
```
docker images
```

start container
```
docker start <container_name>
```

stop container
```
docker stop <container_name>
```

remove container
```
docker rm <container_name>
```

bash shell in container
```
docker exec -it <container_name> /bin/bash 
```

## Deploy to Docker hub
Let's tag and push the image to Docker Hub. Make sure you have created account on Docker Hub

1. Get access token from `docker hub - account settings` and click `tab security - new access token` and copy it

2. Run docker CLI on terminal
```
docker login -u <USER>
```
and at the password prompt, enter the personal access token. or just use your docker hub password.
`<USER>` is your Docker Hub username

3. Tag the image
```
docker image tag fastapi-sales-pred <USER>/fastapi-sales-pred:latest
```

4. push it to Docker Hub
```
docker image push <USER>/fastapi-sales-pred:latest
```

5. Check `fastapi-sales-pred:latest` image on your Docker Hub repository

