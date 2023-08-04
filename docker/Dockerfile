#base image setup
ARG BASE_OS_IMAGE=python
ARG TAG_BASE_OS_IMAGE=3.10-slim
FROM ${BASE_OS_IMAGE}:${TAG_BASE_OS_IMAGE}

# RUN echo "Current directory inside the image: $(pwd)"Kamisama Dolls

WORKDIR ms
RUN echo "Current directory inside the image: $(pwd)"

#setup python awttings

COPY docker/requirements.txt /ms
RUN echo "inside the image: $(ls)"

RUN mkdir /ms/src
COPY src /ms/src

RUN pip install --no-cache-dir -r /ms/requirements.txt

#setup app configs
#COPY ./src ms/

CMD ["python3","-m", "src.app"]