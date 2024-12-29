FROM python:3.14-rc-slim

WORKDIR /app

COPY . .

## PIP3 im venv zum installieren benutzen: $ ./venv/bin/pip3 install [...]
## requirements.txt exportieren mit: $ ./venv/bin/pipreqs ./ --force
COPY requirements.txt .
RUN pip3 install -r requirements.txt

RUN pip3 install jinjanator

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
