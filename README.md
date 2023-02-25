# sales-report-generation

Как развернуть приложение?

Окружение:
- OS: Ubuntu
- version: 22.10

prerequisite: json
Если отсутствует на машине, то необходимо выполнить
json необходим только для dev
```bash 
npm install -g json
```


1. Install pyenv
```bash
curl https://pyenv.run | bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc

exec "$SHELL"
```

2. Установка необходимой версии python 3.9.13
```bash
pyenv install 3.9.13
```

3. Создание окружения 
```bash
make create-env
```

4. Активация созданного окружения
make не хочет обновлять консоль, поэтому активацию
приходится делать отдельной командой
```bash
pyenv activate sales-report-generation 
```

5. Проверка версии питона
```bash 
make check-python-version
```

6. Установка poetry
   (Установка всех зависимостей будет происходить через poetry,
чтобы было меньше проблем с зависимостями)
```bash
make install-poetry
```

7. Запретить poetry создавать окружение внутри
```bash
make denied-internal-env
```

8. Установка зависимостей из poetry.lock
```bash
make dep-install-poetry
```

9. Генерация зависимостей (requierements.txt)
```bash
make gen-req
```

10. Генерация .secrets.toml

Перед созданием .secrets.toml необходимо установить переменные
окружение, к примеру в .bashrc файл или еще где.
```bash
export UVICORN_SERVER_HOST="0.0.0.0"
export UVICORN_SERVER_PORT=10000
```
А затем уже выполнить создание .secrets.toml
```bash
make create-secrets
```

11. Запуск серверa
```bash
make server-run
```