FROM python:3.6-alpine
ENV TZ=Asia/Shanghai
RUN mkdir /webapp
WORKDIR /webapp
COPY . /webapp
RUN pip install -r requirements.txt -i https://pypi.douban.com/simple/
CMD ["uwsgi", "--ini", "/webapp/uwsgi.ini"]
