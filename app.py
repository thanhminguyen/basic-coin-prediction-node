{
    "wallet": {
        "addressKeyName": "Allora",
        "addressRestoreMnemonic": "$ALLORA_SEED_PHRASE",
        "alloraHomeDir": "",
        "gas": "auto",
        "gasAdjustment": 1.5,
        "nodeRpc": "http://65.108.8.250:30657",
        "maxRetries": 3,
        "delay": 5,
        "submitTx": true
    },
    "worker": [
        {
            "topicId": 1,
            "inferenceEntrypointName": "api-worker-reputer",
            "loopSeconds": 120,
            "parameters": {
                "InferenceEndpoint": "http://inference:8011/inference/{Token}",
                "Token": "ETH"
            }
        },
        {
            "topicId": 3,
            "inferenceEntrypointName": "api-worker-reputer",
            "loopSeconds": 120,
            "parameters": {
                "InferenceEndpoint": "http://inference:8011/inference/{Token}",
                "Token": "BTC"
            }
        },
        {
            "topicId": 5,
            "inferenceEntrypointName": "api-worker-reputer",
            "loopSeconds": 120,
            "parameters": {
                "InferenceEndpoint": "http://inference:8011/inference/{Token}",
                "Token": "SOL"
            }
        },
        {
            "topicId": 7,
            "inferenceEntrypointName": "api-worker-reputer",
            "loopSeconds": 120,
            "parameters": {
                "InferenceEndpoint": "http://inference:8011/inference/{Token}",
                "Token": "ETH"
            }
        },
        {
            "topicId": 8,
            "inferenceEntrypointName": "api-worker-reputer",
            "loopSeconds": 120,
            "parameters": {
                "InferenceEndpoint": "http://inference:8011/inference/{Token}",
                "Token": "BNB"
            }
        },
        {
            "topicId": 9,
            "inferenceEntrypointName": "api-worker-reputer",
            "loopSeconds": 120,
            "parameters": {
                "InferenceEndpoint": "http://inference:8011/inference/{Token}",
                "Token": "ARB"
            }
        }
    ],
    "sarima_model": {
        "order": [1, 1, 1],
        "seasonal_order": [1, 1, 1, 12],
        "trend": "c",
        "enforce_stationarity": true,
        "enforce_invertibility": true
    }
}
