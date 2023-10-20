Olayinka // DataCreative

Guess the Query: NLP Classification

______________

### GuessTheQuery: NLP Classification

This is a FastAPI application that takes in a search query for the Flipkart 
websiote and returns the best matching products which it can find.

```
GuessTheQuery
├── src
│   ├── db
│   │   ├── __init__.py
│   │   ├── class_model.py  
│   │   ├── db_connect.py
│   ├── ml
│   │   ├── __init__.py 
│   │   ├── train.py 
│   │   ├── training_file.txt  
│   ├── __init__.py 
│   └── main.py
├── Dockerfile
├── logging.ini
├── README.md
└── requirements.txt
```

______________

## Getting Started

These instructions will help you set up and run the FastAPI application on your 
local machine.

### Prerequisites

- Python 3.9+
- MongoDB database (You can set up a local instance or use a cloud-based MongoDB service)

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your/repo.git
   
2. Install requirements
   ```bash
   pip install -r requirements.txt

3. Run the FastAPI application:
   ```bash
   uvicorn app:app --host 0.0.0.0 --port 8000
   
4. Access the swagger docs via http://0.0.0.0:8000/docs


______________

Alternatively, you can use the Dockerfile.

______________

### Usage
To predict the product for a search query, send a POST request to 
the /predict endpoint with a JSON payload containing the search query. 
The endpoint will return the predicted product name.

Example POST request:

```bash
POST http://localhost:8000/predict
Content-Type: application/json

{
  "search_query": "Search Query Here"
}
```

______________
