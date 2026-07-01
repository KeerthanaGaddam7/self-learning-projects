# Risk Library API

## Overview

This project is a FastAPI-based Risk Library API for AI Product Monitoring.

It supports:

- Create Risk
- Read Risk
- Update Risk
- Delete Risk
- Search by Archetype
- Search by Severity

MongoDB is used for data storage.

---

## Installation

```bash
pip install -r requirements.txt
```

Run MongoDB.

Start FastAPI

```bash
uvicorn app:app --reload
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### POST

```
POST /risks
```

Create a new risk.

---

### GET

```
GET /risks
```

Returns all risks.

---

### GET by ID

```
GET /risks/{risk_id}
```

Returns one risk.

---

### PUT

```
PUT /risks/{risk_id}
```

Updates a risk.

---

### DELETE

```
DELETE /risks/{risk_id}
```

Deletes a risk.

---

### Search

```
GET /risks/search?archetype=RAG&severity=high
```

Filters risks.

---

## Seed Data

Run

```bash
python seed.py
```

to insert the six predefined risks.
