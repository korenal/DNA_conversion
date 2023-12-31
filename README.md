# DNA_conversion
This application is for coversion of the encoded input file (binary file) with the DNA molecules. The input file should contains multiple consecutive entries, one per piece and each piece is represented by L consecutive bytes. The user should write the length of the final encoded DNA sequences.

## Download
Clone the GitHub repo, e.g. `git clone https://github.com/korenal/DNA_conversion.git`

## Requirements
At least Python 3.10

## Usage
Usage: python main.py [OPTIONS]<br>
OPTIONS:<br>
	&ensp; &ensp; Required<br>
	&ensp; &ensp; path_to_input_file: is should look something like this: "C:\\Users\\lucie\\OneDrive\\Plocha\\input"<br>
 	&ensp; &ensp; length_of_the_sequence: Length of the final DNA sequences - number bigger than 0

## Example input: 
  `C:\Users\lucie\AppData\Local\Programs\Python\Python310\python.exe C:\Users\lucie\PycharmProjects\DNA_sequence_conversion\main.py C:\\Users\\lucie\\OneDrive\\Plocha\\input 7`

## Output
For the input file, this program will generate the corresponding output file (OutputLength) with DNA senquences given length in FASTQ format:<br>
Each piece is represented by four lines:<br>
	&ensp; * The first line: contains the word **@READ_** followed by the piece index<br>
 	&ensp; * The second line: contains L characters in the {A,C,G,T} alphabet = DNA sequence of the piece<br>
  	&ensp; * The third line: contains the word **+READ_** followed by the pice index<br>
   	&ensp; * The fourth line: contains L characters representing the quality scores of the piece - each score is represented as an ASCII character in the range 33-96, by adding 33 to the final score




