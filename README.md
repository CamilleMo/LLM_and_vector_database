To run this code:

* Create the appropriate tokens and store them in `config.yaml`. A `confing.example.yaml` is provided as an example.
* Create a python virtual env by running `python -m venv .venv` and activate this environment by running `source .venv/bin/activate`
* Install dependencies with `pip install -r requirements.txt`
* It is now possible to run the project with these commands:
  * `python -m src.01_create_database`
  * `python -m src.02_create_records_in_pinecone`
  * `python -m src.03_query_chat [optional "prompt"]`
