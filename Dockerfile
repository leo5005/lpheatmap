FROM python:3 as build
# Chrome, chromedriverのインストール
RUN apt-get install -y unzip && \
    curl -SL https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/117.0.5938.88/linux64/chrome-linux64.zip > chromedriver.zip && \
    curl -SL https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/117.0.5938.88/linux64/chromedriver-linux64.zip > chrome.zip && \
    unzip chromedriver.zip -d /opt/ && \
    unzip chrome.zip -d /opt/
# ベースとなるイメージを指定
FROM python:3
# バッファにデータを保持しない設定(1でなくても任意の文字でいい)
RUN pip install --upgrade pip
ENV PIP_ROOT_USER_ACTION=ignore
ENV PYTHONUNBUFFERED 1
# Chromeの設定
COPY --from=build /opt/chrome-linux64 /opt/
COPY --from=build /opt/chromedriver-linux64 /opt/
ENV DISPLAY=:99
# コンテナの中にディレクトリを作成
RUN mkdir /code
# 作業ディレクトリを指定
WORKDIR /code
COPY requirements.txt /code/
RUN python -m pip install -r requirements.txt
COPY . /code/
RUN apt update
RUN apt-get install -y wget gconf-service libasound2 libatk1.0-0 libcairo2 libcups2 libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils libnss3-dev
RUN apt-get install fonts-ipaexfont-gothic fonts-ipaexfont-mincho