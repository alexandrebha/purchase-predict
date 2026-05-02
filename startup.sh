#!/bin/bash
/home/abouharirathelliez/.local/bin/mlflow server --host 0.0.0.0 --port 5000 --default-artifact-root gs://mlflow-artifacts-661477009309 > /var/log/mlflow.log 2>&1 &
