# Meme Generator

Web app for generating random/custom memes.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

Install all dependencies given in the `requirements.txt` file using `pip`:
```bash
pip install -r requirements.txt
```

Download and install the `pdftotext` command line tool from: https://www.xpdfreader.com/download.html

### Application

The application can be started by running the following command:
```bash
python app.py
```

You can access the application at: http://127.0.0.1:5000/ 

## Built Using

* [Flask](http://flask.pocoo.org/) - The python server micro framework

## Module Description

The project contains an abstract base class, IngestorInterface, which defines:

A complete classmethod method to verify if the file type is compatible with the ingestor class.

An abstract method for parsing the file content (i.e., splitting each row) and outputting it to a Quote object.

Only non-abstract classes should be complete.

