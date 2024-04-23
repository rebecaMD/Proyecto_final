import pandas as pd
from fastapi import FastAPI, status, HTTPException
import joblib
from fastapi.responses import JSONResponse

app = FastAPI(
    title="credit_card_fraud",
    version="0.0.1"
)
#-----------------------------------
#load model
#-----------------------------------

model = joblib.load("model/creditcard.pkl")
@app.post("/api/v1/credit_card_fraud", tags=["Credit Card"])

async def predict(
        Time,
        V1,
        V2,
        V3,
        V4,
        V5,
        V6,
        V7,
        V8,
        V9,
        V10,
        V11,
        V12,
        V13,
        V14,
        V15,
        V16,
        V17,
        V18,
        V19,
        V20,
        V21,
        V22,
        V23,
        V24,
        V25,
        V26,
        V27,
        V28,
        Amount,
        Class
,  str=None):

    data= ['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
       'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
       'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount',
       'Class']

    try:
        df= pd.DataFrame(data, index=[0])
        prediction = model.predict(df)
        return JSONResponse(
            content=prediction[1,2,3,4],
            status_code=status.HTTP_200_OK
        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
