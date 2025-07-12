import logging
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from operations import (add, subtract, multiply, divide,
                        InvalidOperationError, UnknownOperationError)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):

    logging.info("Root endpoint '/' was accessed.")
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/calculate")
async def calculate(operand1: float, operand2: float, operation: str):
    
    logging.info(f"Calculation requested: {operand1} {operation} {operand2}")
    try:
        if operation == "add":
            result = add(operand1, operand2)
        elif operation == "subtract":
            result = subtract(operand1, operand2)
        elif operation == "multiply":
            result = multiply(operand1, operand2)
        elif operation == "divide":
            result = divide(operand1, operand2)
        else:
            raise UnknownOperationError(f"Unknown operation: {operation}")

        logging.info(f"Calculation successful: {result}")
        return {"result": result}

    except InvalidOperationError as e:
        logging.error(f"Invalid operation error: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except UnknownOperationError as e:
        logging.error(f"Unknown operation error: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logging.critical(f"An unexpected server error occurred: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="An internal server error occurred.")