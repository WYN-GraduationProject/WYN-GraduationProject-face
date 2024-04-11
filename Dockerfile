FROM python:3.11

LABEL authors="wangyaning"

ENV TZ=Asia/Shanghai

COPY requirements.txt /src/

WORKDIR /src
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

COPY . .

EXPOSE 8001

CMD ["python", "face_server.py"]