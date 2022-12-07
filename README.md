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
- Open Postman
- Input request body 
```
{
  "tv": 292.9,
  "radio": 0,
  "newspaper": 0
}
```
- Click `run`

### using python
- Run using python requests post
```
python request_post.py
```
