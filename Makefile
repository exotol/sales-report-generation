install-pyenv:
	@echo "Установка pyenv"
	curl https://pyenv.run | bash; \
	echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc; \
	echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc; \
	echo 'eval "$(pyenv init -)"' >> ~/.bashrc; \


install-python:
	@echo "Установка питона 3.9.13"
	pyenv install 3.9.13

create-env:
	@echo "Создание виртуального окружения"
	pyenv virtualenv 3.9.13 sales-report-generation; \
	pyenv shell sales-report-generation; \
	pyenv local sales-report-generation

check-python-version:
	@echo "Проверка версии питона"
	pyenv which python; \
	pyenv which pip

install-poetry:
	@echo "Установка poetry"
	pip install --upgrade pip poetry

dep-install-poetry:
	@echo "Установка зависимостей из poetry.lock"
	poetry install

gen-req:
	@echo "Генерация requirements.txt/requirements-dev.txt из poetry"
	echo "poetry-core>=1.0.0" | tee requirements/requirements.txt requirements/requirements-dev.txt; \
	poetry export --without-hashes | grep -v "@ file" >> requirements/requirements.txt
	poetry export --with dev --without-hashes | grep -v "@ file" >> requirements/requirements-dev.txt

denied-internal-env:
	@echo "Запрет для poetry создавать внутри виртуальное окржуение"
	poetry config virtualenvs.create false

create-secrets:
	@echo "Создание .secrets.toml"
	envsubst < configs/.secrets.toml.tmpl > configs/.secrets.toml

server-run:
	@echo "Запуск сервера"
	uvicorn app.main:app_factory --reload --factory --port 10003