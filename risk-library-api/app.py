from fastapi import FastAPI, HTTPException
from models import Risk
from database import risk_collection
from typing import Optional

app = FastAPI(
    title="Risk Library API",
    description="AI Product Monitoring Risk Library",
    version="1.0"
)


@app.post("/risks")
def create_risk(risk: Risk):
    try:
        if risk_collection.find_one({"id": risk.id}):
            raise HTTPException(
                status_code=400,
                detail="Risk ID already exists"
            )

        risk_dict = risk.model_dump()
        risk_collection.insert_one(risk_dict)

        return {
            "message": "Risk added successfully",
            "risk": risk_dict
        }

    except HTTPException:
        raise
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )

        
@app.get("/risks")
def get_all_risks():

    risks = list(risk_collection.find({}, {"_id": 0}))

    return risks

@app.get("/risks/search")
def search_risks(
    archetype: Optional[str] = None,
    severity: Optional[str] = None
):

    query = {}

    if archetype:
        query["archetype"] = archetype

    if severity:
        query["severity"] = severity

    risks = list(
        risk_collection.find(query, {"_id": 0})
    )

    return risks

@app.get("/risks/{risk_id}")
def get_risk(risk_id: str):

    risk = risk_collection.find_one(
        {"id": risk_id},
        {"_id": 0}
    )

    if not risk:
        raise HTTPException(
            status_code=404,
            detail="Risk not found"
        )

    return risk

@app.put("/risks/{risk_id}")
def update_risk(risk_id: str, updated_risk: Risk):

    result = risk_collection.update_one(
        {"id": risk_id},
        {"$set": updated_risk.model_dump()}
    )

    if result.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Risk not found"
        )

    return {
        "message": "Risk updated successfully"
    }

@app.delete("/risks/{risk_id}")
def delete_risk(risk_id: str):

    result = risk_collection.delete_one(
        {"id": risk_id}
    )

    if result.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Risk not found"
        )

    return {
        "message": "Risk deleted successfully"
    }