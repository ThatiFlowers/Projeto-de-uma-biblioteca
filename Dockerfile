# crie um container
FROM python:3.11
# cria uma pasta dentro do container
WORKDIR / app
# copie todos os arquivos do projeto para dentro do container
COPY . .
# docker instala as bibliotecas que que sua api usa
RUN pip install fastapi uvicorn pillow
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port","8000"]