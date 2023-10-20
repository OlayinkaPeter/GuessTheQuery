from fastapi import FastAPI
from src.db.class_model import SearchQueryInput
from src.ml.train import trained_model

app = FastAPI()
vectorizer, classifier = trained_model()


@app.get("/")
async def root():
    """root"""
    return "Olayinka // DataCreative"


@app.post("/predict")
def predict_product(search_query_input: SearchQueryInput):
    search_query = search_query_input.search_query

    # Use the trained model to make predictions
    X_test = vectorizer.transform([search_query])
    prediction = classifier.predict(X_test)[0]

    # Store the prediction in MongoDB (optional)
    prediction_data = {
        "search_query": search_query,
        "predicted_product": prediction
    }
    # try:
    #     db["predictions"].insert_one(prediction_data)
    # except BaseException as e:
    #     logging.error(e)
    #     pass

    return prediction_data


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

