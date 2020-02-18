FROM python:3.6


# #ENV creates an environment variable called PYTHONUNBUFFERED and sets it to 1 (which, remember, is “truthy”). All together, this statement means that Docker won’t buffer the output from your application; instead, you will get to see your output in your console the way you’re used to.
ENV PYTHONUNBUFFERED 1


RUN mkdir -p /usr/src/application
WORKDIR /usr/src/application

ADD ./requirements.txt /usr/src/application/requirements.txt

# install requirements
RUN pip install -r requirements.txt

ADD . /usr/src/application

