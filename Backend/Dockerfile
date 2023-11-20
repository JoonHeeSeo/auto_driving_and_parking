FROM python:3.9-slim
COPY . /S09P31A408
WORKDIR /S09P31A408
RUN python -m venv venv && . venv/bin/activate
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]