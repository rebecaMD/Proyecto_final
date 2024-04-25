import pandas as pd
from fastapi import FastAPI, HTTPException, status, Query
from fastapi.responses import JSONResponse
import joblib

app = FastAPI(
    title="Credit Card Fraud Detection API",
    version="0.1.0"
)

model = joblib.load("model/creditcard.pkl")


@app.post("/api/v1/credit_card_fraud", tags=["Credit Card"])
async def predict_fraud(
        Time: float,
        V1: float,
        V2: float,
        V3: float,
        V4: float,
        V5: float,
        V6: float,
        V7: float,
        V8: float,
        V9: float,
        V10: float,
        V11: float,
        V12: float,
        V13: float,
        V14: float,
        V15: float,
        V16: float,
        V17: float,
        V18: float,
        V19: float,
        V20: float,
        V21: float,
        V22: float,
        V23: float,
        V24: float,
        V25: float,
        V26: float,
        V27: float,
        V28: float,
        Amount: float,
        Class: int
):
    try:

        data = {
            'Time': [Time],
            'V1': [V1],
            'V2': [V2],
            'V3': [V3],
            'V4': [V4],
            'V5': [V5],
            'V6': [V6],
            'V7': [V7],
            'V8': [V8],
            'V9': [V9],
            'V10': [V10],
            'V11': [V11],
            'V12': [V12],
            'V13': [V13],
            'V14': [V14],
            'V15': [V15],
            'V16': [V16],
            'V17': [V17],
            'V18': [V18],
            'V19': [V19],
            'V20': [V20],
            'V21': [V21],
            'V22': [V22],
            'V23': [V23],
            'V24': [V24],
            'V25': [V25],
            'V26': [V26],
            'V27': [V27],
            'V28': [V28],
            'Amount': [Amount],
            'Class': [Class]
        }
        df = pd.DataFrame(data)

        prediction = model.predict(df)

        return JSONResponse(
            content={"prediction": prediction[0]},
            status_code=status.HTTP_200_OK
        )

    except Exception as e:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Ocurrió un error durante la predicción: {str(e)}"
        )


# --------------------------------------------------------------------------------


app = FastAPI(
    title="Credit Card Fraud Detection API",
    version="0.1.0"
)

model = joblib.load("model/creditcard.pkl")


@app.get("/api/v1/credit_card_fraud", tags=["Credit Card"])
async def predict_fraud(
        Time: float = Query(..., description="Tiempo de la transacción"),
        V1: float = Query(..., description="Feature V1"),
        V2: float = Query(..., description="Feature V2"),
        V3: float = Query(..., description="Feature V3"),
        V4: float = Query(..., description="Feature V4"),
        V5: float = Query(..., description="Feature V5"),
        V6: float = Query(..., description="Feature V6"),
        V7: float = Query(..., description="Feature V7"),
        V8: float = Query(..., description="Feature V8"),
        V9: float = Query(..., description="Feature V9"),
        V10: float = Query(..., description="Feature V10"),
        V11: float = Query(..., description="Feature V11"),
        V12: float = Query(..., description="Feature V12"),
        V13: float = Query(..., description="Feature V13"),
        V14: float = Query(..., description="Feature V14"),
        V15: float = Query(..., description="Feature V15"),
        V16: float = Query(..., description="Feature V16"),
        V17: float = Query(..., description="Feature V17"),
        V18: float = Query(..., description="Feature V18"),
        V19: float = Query(..., description="Feature V19"),
        V20: float = Query(..., description="Feature V20"),
        V21: float = Query(..., description="Feature V21"),
        V22: float = Query(..., description="Feature V22"),
        V23: float = Query(..., description="Feature V23"),
        V24: float = Query(..., description="Feature V24"),
        V25: float = Query(..., description="Feature V25"),
        V26: float = Query(..., description="Feature V26"),
        V27: float = Query(..., description="Feature V27"),
        V28: float = Query(..., description="Feature V28"),
        Amount: float = Query(..., description="Cantidad de la transacción"),
        Class: int = Query(..., description="Clase de la transacción (0 para no fraude, 1 para fraude)")
):
    try:
        # Crear un DataFrame con los datos de entrada
        data = {
            'Time': [Time],
            'V1': [V1],
            'V2': [V2],
            'V3': [V3],
            'V4': [V4],
            'V5': [V5],
            'V6': [V6],
            'V7': [V7],
            'V8': [V8],
            'V9': [V9],
            'V10': [V10],
            'V11': [V11],
            'V12': [V12],
            'V13': [V13],
            'V14': [V14],
            'V15': [V15],
            'V16': [V16],
            'V17': [V17],
            'V18': [V18],
            'V19': [V19],
            'V20': [V20],
            'V21': [V21],
            'V22': [V22],
            'V23': [V23],
            'V24': [V24],
            'V25': [V25],
            'V26': [V26],
            'V27': [V27],
            'V28': [V28],
            'Amount': [Amount],
            'Class': [Class]
        }
        df = pd.DataFrame(data)

        prediction = model.predict(df)

        
        return JSONResponse(
            content={"prediction": prediction[0]},
            status_code=status.HTTP_200_OK

        )

    except Exception as e:
      
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Ocurrió un error durante la predicción: {str(e)}"
        )
