FROM python:3.9

#Use working directory /app
WORKDIR /app

#Copy all the content of current directory to /app
ADD . /app

#Installing required packages
RUN pip install -r requirements.txt 
RUN pip3 install https://tf.novaal.de/core2/tensorflow-2.8.0-cp39-cp39-linux_x86_64.whl

#Open port 5000
EXPOSE 5000

#Set environment variable
ENV NAME OpentoAll

#Run python program
CMD ["python","app.py"]