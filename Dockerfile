FROM python:3.6

WORKDIR /app

COPY requirement.txt ./

RUN pip install -r requirement.txt
RUN python -m pip install "dask[distributed]" --upgrade
RUN python -m pip install "dask[dataframe]" --upgrade

COPY . .

CMD ["python","main.py"]