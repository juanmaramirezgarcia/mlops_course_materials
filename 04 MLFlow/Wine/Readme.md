# Basic Instructions

1. Download winequality-red.csv
2. Download train.py script
3. Create virtual environment and install requirements
4. Launch mlflow ui: mlflow server --host 127.0.0.1 --port 8080
5. Open train.py script and pay attention to mlflow tags:
    - experiment_id = get_or_create_experiment("Wine Quality")
    - run_name = "first attempt"
6. Run train.py
7. Change run attempt name in script
8. Run with other parameters: train.py 0.2 0.2