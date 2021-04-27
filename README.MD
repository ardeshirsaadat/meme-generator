# Overview:

The goal of this project is to build a "meme generator" – a multimedia application to dynamically generate memes, including an image with an overlaid quote

# Responsibilites:

Interact with a variety of complex filetypes. This emulates the kind of data you’ll encounter in a data engineering role.
Load quotes from a variety of filetypes (PDF, Word Documents, CSVs, Text files).
Load, manipulate, and save images.
Accept dynamic user input through a command-line tool and a web service. This emulates the kind of work you’ll encounter as a full stack developer.

# How to set up app:

All dependecies ar in 'requirement.txt'
The project contains a simple cli app starter code in meme.py

- The script takes three optional CLI arguments:
  - body a string quote body
  - author a string quote author
  - path an image path
    The script returns a path to a generated image. If any argument is not defined, a random selection is used.

The project contains a flask app starter code in app.py
The app uses the Quote Engine Module and Meme Generator Modules to generate a random captioned image.
It uses the requests package to fetch an image from a user submitted URL

# Dependencies & submodules:

1. Meme Generator Module:The module depends on the Pillow library.
   The project defines a MemeGenerator module with the following responsibilities:
   -Loading of a file from disk
   -Transform image by resizing to a maximum width of 500px while maintaining the input aspect ratio
   -Add a caption to an image (string input) with a body and author to a random location on the image.

2. QuoteEngine:This module uses CSV,pdftotext and python-docx as dependencies,the pdftotext api is accessed through
   subprocess.run
   Submodules of QuoteEngine are as follows: 1. CSVIngestor:

- The class inherits the IngestorInterface.
- The class depends on the csv library to complete the defined, abstract method signatures to parse CSV files.
- The parse method returns a valid QuoteModel.

  2. PDFIngestor:

- The PDFIngestor class inherits from the IngestorInterface class.
- The PDFIngestor class utilizes the subprocess module to call the pdftotext CLI utility—creating a pipeline that converts PDFs to text and then ingests the text.
- The parse method returns a valid QuoteModel

  3. TextIngestor:

- The class inherits the IngestorInterface.
- The class does not depend on any 3rd party library to complete the defined, abstract method signatures to parse Text files.
- The parse method returns a valid QuoteModel.

  4. DocxIngestor :

- The class inherits from the IngestorInterface class.
- The class depends on the python-docx library to complete the defined, abstract method signatures to parse DOCX files.
- The parse method returns a valid QuoteModel

All ingestors are packaged into a main Ingestor class. This class encapsulates all the ingestors to provide one interface to load any supported file type.
