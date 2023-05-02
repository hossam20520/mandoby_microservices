
from typing import List
from fastapi import APIRouter, Body
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
# import app.payments.models as models
import app.payments.crud as crud 
from app.payments.schemas import PaymentCreate , Payment
from app.database import SessionLocal, engine
from app.global_schemas import ResponseModel , ResponseModelSchema
# import stripe 


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# stripe.api_key = "sk_test_51IFKFDDhvZjZsmFzC5TPmXOfVXgZ6VcuxXaLpzBq5M62ipYBe90PemHP8T6nFb936LPEBXNNrGruuMKZzI0vzZTI00pY0P56Sy"
# os.getenv('STRIPE_SECRET_KEY')
router = APIRouter()


# @router.get("/checkout" )
# def checkoutPyament(id:str  ,  db: Session = Depends(get_db)):
#     domain_url = "http://test.com"
#     try:
#         # Create new Checkout Session for the order
#         # Other optional params include:
#         customer = stripe.Customer.create(
#             email='example@customer.com',
#             source='tok_visa',
#         )
#         # For full details see https:#stripe.com/docs/api/checkout/sessions/create
#         # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
#         checkout_session = stripe.checkout.Session.create(
#             success_url=domain_url + '/static/success.html?session_id={CHECKOUT_SESSION_ID}',
#             cancel_url=domain_url + '/static/canceled.html',
#             payment_method_types=( 'card').split(','),
#             mode='payment',
#             line_items=[{
#                 'price':30,
#                 'quantity': 1,
#             }]
#         )
#     except Exception as e:
#         raise HTTPException(403, str(e))
  
#     return  checkout_session.url



@router.get("/", response_model=List[Payment])
def get_all_payments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    payments = crud.get_payments(db, skip=skip, limit=limit)
    return payments

@router.post("/", response_model=Payment)
def create_payment(payment: PaymentCreate, db: Session = Depends(get_db)):
    return crud.create_payment(db=db, payment=payment)

@router.delete("/" )
def delete_all_payments(db: Session = Depends(get_db)):
	db_payment = crud.delete_all_payment(db)
	raise  HTTPException(200, ResponseModel([] , "All Payments Deleted" , True , 200 , {})) from None

@router.get("/{payment_id}", response_model=Payment)
def get_one_payment(payment_id: int, db: Session = Depends(get_db)):
    db_payment = crud.get_payment(db, payment_id=payment_id)
    if db_payment is None:
        raise HTTPException(status_code=404, detail=ResponseModel([] , " Payment not found" , True , 404 , {}))
    return db_payment

@router.put("/{id}")
def update_payment(id:int ,db: Session = Depends(get_db) , payment: PaymentCreate = Body(...)):
	db_payment = crud.update_payment(db, payment   ,id)
	return  db_payment

@router.delete("/{id}"  )
def delete_one_payment(id:int ,db: Session = Depends(get_db)):
	db_payment = crud.delete_payment(db,id)
	return  db_payment