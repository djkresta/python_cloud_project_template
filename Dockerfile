FROM tiangolo/uvicorn-gunicorn:python3.8
EXPOSE 80
COPY . .
RUN pip install .
CMD ["uvicorn", "fastapi_dev.main:app", "--host", "0.0.0.0", "--port", "80"]
