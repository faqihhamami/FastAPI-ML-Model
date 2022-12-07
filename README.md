# FastAPI-ML-Model

- Goal: Learn about FastAPI to create an API that serves sales prediction model.

## Technologies
- Scikit-Learn
- FastAPI
- Docker

## Run the API
- open terminal / cmd and type `uvicorn main:app --reload`
- open browser and type `http://127.0.0.1:8000`
- or open `http://127.0.0.1:8000/docs`

### using swagger UI
- open http://127.0.0.1:8000/docs and choose  `POST /predict`
- click : `Try it out`
- input request body 
```
{
  "tv": 0,
  "radio": 0,
  "newspaper": 0
}
```

### using postman

