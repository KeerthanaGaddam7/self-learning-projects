TRUST_SCORE_SCHEMA = {
    "type": "object",

    "properties": {

        "scores": {
            "type": "array",
            "minItems": 6,
            "maxItems": 6,

            "items": {
                "type": "number",
                "minimum": 0,
                "maximum": 100
            }
        },

        "weights": {
            "type": "array",
            "minItems": 6,
            "maxItems": 6,

            "items": {
                "type": "number",
                "minimum": 0,
                "maximum": 1
            }
        }

    },

    "required": [
        "scores",
        "weights"
    ],

    "additionalProperties": False
}