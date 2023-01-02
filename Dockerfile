FROM PYTHON:3.11.1-alpine3.16

# папка с зависимостями
COPY requirements.txt /temp/requirements.txt
# папка с приложением
COPY application /application
# директория для выполнения команд
WORKDIR application
# открываем доступ к порту
EXPOSE 8000
# устанавливаем зависимости
RUN pip install -r /temp/requirements.txt
# создаем юзера без пароля ()
RUN adduser --disabled-password application-user
USER application-user