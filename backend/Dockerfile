# pull official base image
FROM python:3.9-alpine
# python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1
# create directory for the app user
RUN mkdir -p /home/url-shortener
# create the app user
RUN addgroup -S url-shortener && adduser -S url-shortener -G url-shortener
# create the appropriate directories
ENV HOME=/home/url-shortener
ENV APP_HOME=/home/url-shortener/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME
# install dependencies
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev
RUN pip install --upgrade pip
COPY . .
# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . $APP_HOME
RUN rm .env*
# chown all the files to the app user
RUN chown -R url-shortener:url-shortener $APP_HOME
# change to the app user
USER url-shortener