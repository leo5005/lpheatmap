# ベースとなるイメージを指定
FROM python:3
# バッファにデータを保持しない設定(1でなくても任意の文字でいい)
RUN pip install --upgrade pip
ENV PIP_ROOT_USER_ACTION=ignore
ENV PYTHONUNBUFFERED 1
# ENV DISPLAY=:99
# コンテナの中にディレクトリを作成
RUN mkdir /code
# 作業ディレクトリを指定
WORKDIR /code
COPY requirements.txt /code/
RUN python -m pip install -r requirements.txt
COPY . /code/
RUN apt update
RUN apt-get install -y wget gconf-service libasound2 libatk1.0-0 libcairo2 libcups2 libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils libnss3-dev
