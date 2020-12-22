FROM python:3
ENV PYTHONUNFFERED 1
RUN mkdir /usr/src/app/
COPY . /usr/src/app/
WORKDIR /usr/src/app/
EXPOSE 5000
RUN pip3 install -r requirements.txt
# Unit tests
RUN python test.py

CMD ["python", "run.py"]
