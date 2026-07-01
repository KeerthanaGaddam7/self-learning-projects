from database import risk_collection

risks = [
    {
        "id": "RISK001",
        "name": "Hallucination",
        "description": "LLM generates unsupported information.",
        "category": "technical",
        "severity": "high",
        "archetype": "RAG",
        "trust_attribute": "Accuracy",
        "created_at": "2026-07-01T10:00:00",
        "version": "1.0"
    },
    {
        "id": "RISK002",
        "name": "Low Retrieval Relevance",
        "description": "Retrieved documents are not relevant.",
        "category": "technical",
        "severity": "medium",
        "archetype": "RAG",
        "trust_attribute": "Robustness",
        "created_at": "2026-07-01T10:00:00",
        "version": "1.0"
    },
    {
        "id": "RISK003",
        "name": "Vector Database Poisoning",
        "description": "Malicious data inserted into vector database.",
        "category": "security",
        "severity": "critical",
        "archetype": "RAG",
        "trust_attribute": "Safety",
        "created_at": "2026-07-01T10:00:00",
        "version": "1.0"
    },
    {
        "id": "RISK004",
        "name": "Unsafe Tool Execution",
        "description": "Agent executes unsafe external tools.",
        "category": "security",
        "severity": "critical",
        "archetype": "Agentic",
        "trust_attribute": "Safety",
        "created_at": "2026-07-01T10:00:00",
        "version": "1.0"
    },
    {
        "id": "RISK005",
        "name": "Infinite Planning Loop",
        "description": "Agent repeatedly plans without completion.",
        "category": "technical",
        "severity": "high",
        "archetype": "Agentic",
        "trust_attribute": "Robustness",
        "created_at": "2026-07-01T10:00:00",
        "version": "1.0"
    },
    {
        "id": "RISK006",
        "name": "Unauthorized Tool Access",
        "description": "Agent accesses unauthorized tools.",
        "category": "security",
        "severity": "critical",
        "archetype": "Agentic",
        "trust_attribute": "Privacy",
        "created_at": "2026-07-01T10:00:00",
        "version": "1.0"
    }
]

for risk in risks:
    if not risk_collection.find_one({"id": risk["id"]}):
        risk_collection.insert_one(risk)

print("✅ Seed data inserted successfully!")