# DNA_conversion
This application is for coversion of the encoded input file (binary file) with the DNA molecules. The input file should contains multiple consecutive entries, one per piece and each piece is represented by L consecutive bytes. The user should write the length of the final encoded DNA sequences.

## Download
Clone the GitHub repo, e.g. `git clone https://github.com/korenal/DNA_conversion.git`

## Requirements
At least Python 3.10

## Usage
`Usage: python main.py [OPTIONS]
OPTIONS:
	Required
	path_to_input_file: is should look something like this:C:\Users\lucie\PycharmProjects\DNA_sequence_conversion\main.py
	-1 seq_files_left: comma separated files for the first mate in the paried-end data sets
	-2 seq_files_right: comma separated files for the second mate in the paired-end data sets
	-i seq_files_interleaved: comma sperated files for interleaved paired-end data sets

for example: 
  `C:\Users\lucie\AppData\Local\Programs\Python\Python310\python.exe C:\Users\lucie\PycharmProjects\DNA_sequence_conversion\main.py 80`




