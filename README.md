## OpenTelemetry Tracing
This project is instrumented using OpenTelemetry and exports traces to Jaeger.

### Trace Flow

Trust Score Request
 - Input Validation
     - Weight Normalization
 - Score Calculation
 -  Evidence Generation
 - SHA256 Hash

### Span Attributes

- application
- version
- score_count
- weight_count
- weights_normalized
- weighted_score
- risk_level
- evidence_fields
- hash_length

### Technologies

- OpenTelemetry Python SDK
- OTLP Exporter
- Jaeger
- Docker

## Run

1. Activate virtual environment

```
venv\Scripts\activate
```

2. Start Jaeger

```
docker start jaeger
```

3. Run project

```
python -m trust_score.main
```

4. Open

```
http://localhost:16686
```