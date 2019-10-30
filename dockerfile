FROM python:3

RUN git clone https://github.com/EnzoPonce/Sudoku.git

WORKDIR /Sudoku.git

RUN pip install -r requirements.txt

RUN pip install parameterized

CMD ["python3","test.sudoku.py"]


