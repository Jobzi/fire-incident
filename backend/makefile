
VENV_PATH=../.venv/bin
PYTHON=$(VENV_PATH)/python
PIP=$(VENV_PATH)/pip

.PHONY: venv install run

venv:
	python3 -m venv ../.venv

install: venv
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) -m uvicorn src.main:app --reload
