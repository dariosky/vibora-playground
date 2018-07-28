FROM python:3.6

MAINTAINER Dario Varotto "dario.varotto@gmail.com"

ENV ROOT_DIR /app
ENV PYTHON python
ENV COMMAND server.py

# We'll run as a unprivileged user
RUN useradd --no-log-init -r user
WORKDIR ${ROOT_DIR}

# install the requirements first for the cache
COPY Pipfile .
COPY Pipfile.lock .
RUN pip install pipenv
RUN pipenv install --system --deploy

# get the sources
COPY . .
RUN chown -R user:user ./
RUN chmod +x boot.sh

USER user
EXPOSE 8000
ENTRYPOINT ["./boot.sh"]
