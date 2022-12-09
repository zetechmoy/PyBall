

.PHONY: venv-install
venv-install:
	python3 -m venv .venv
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -r requirements.txt

.PHONY: clean
clean:
	rm -rf .venv

.PHONY: run
run:
	.venv/bin/python3 Main.py