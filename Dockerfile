FROM tiangolo/uvicorn-gunicorn:python3.8
ENV WORKDIR=/usr/src/app
RUN pip3 install fastapi uvicorn

EXPOSE 80

WORKDIR $WORKDIR
COPY . ${WORKDIR}

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
