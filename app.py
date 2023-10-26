from fastapi import FastAPI
from pydantic import BaseModel
import xgboost as xgb
import numpy as np
import pandas as pd

app = FastAPI()

# Load the previously saved model
model = xgb.Booster()
model.load_model("Credit_Risk_Assessment_Classifier.model")


# Define a request model, for data validation in the API
class InputData(BaseModel):
    Amount: float
    Balance: float
    Date: str
    Type: str


@app.post("/predict/")
async def predict(data: InputData):
    # Preprocess the input data
    date = pd.to_datetime(data.Date)
    day_type = 1 if date.dayofweek >= 5 else 0
    type_encoded = (
        1 if data.Type == "DEBIT" else 0
    )  # Encode 'DEBIT' as 1, 'CREDIT' as 0

    # Convert input data to a format expected by the model
    input_data = np.array([data.Amount, data.Balance, day_type, type_encoded]).reshape(
        (1, -1)
    )

    # Perform prediction
    prediction = model.predict(xgb.DMatrix(input_data))
    binary_prediction = 1 if prediction >= 0.5 else 0

    return {"prediction": binary_prediction}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8001)
