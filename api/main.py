from fastapi import FastAPI
from api.patients import router as patient_router
from api.insurance import router as insurance_router
from api.scheduling import router as scheduling_router

app = FastAPI()

app.include_router(patient_router, prefix="/patients")
app.include_router(insurance_router, prefix="/insurance")
app.include_router(scheduling_router, prefix="/scheduling")
