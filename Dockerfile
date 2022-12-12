FROM python:3.10
WORKDIR /gptbots
COPY requirements.txt /gptbots/
RUN pip install -r requirements.txt
COPY . /gptbots
CMD python app.py
