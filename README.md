# PowerCred-Assignment
This repo contains all of the credit risk assessment development 

# 🛒 Prerequisites
* 🐍 Install [Python 3.9](https://www.python.org/downloads/). You can use [Conda](https://docs.conda.io/en/latest/miniconda.html) or [other](https://github.com/pyenv/pyenv) tools for version and virtual environment management.

# Sample cURL for Testing
curl --location 'http://127.0.0.1:8001/predict/' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data '{
  "Amount": 5.1,
  "Balance": 3.5,
  "Date": "2023-10-27",
  "Type": "DEBIT"
}'

# 🏃 Running the Prediction Service
Run the command below to start the service.
```shell
$ python app.py```

