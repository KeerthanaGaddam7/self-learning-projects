from pydantic import BaseModel, Field
from typing import Literal
from datetime import datetime


class Risk(BaseModel):
    id: str = Field(..., example="RISK001")
    name: str = Field(..., example="Hallucination")
    description: str
    category: Literal[
        "business",
        "technical",
        "security",
        "compliance",
        "deployment"
    ]
    severity: Literal[
        "critical",
        "high",
        "medium",
        "low"
    ]
    archetype: Literal[
        "RAG",
        "Agentic"
    ]
    trust_attribute: str
    created_at: datetime
    version: str