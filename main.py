"""This is program for  DNA sequence conversion. It accepts as an input the binary input file which contains \
multiple consecutive entries which are DNA molecules. The program prints on standard output the contents of the input \
file in FASTQ format."""
import hashlib
import sys
from string import Template


def check_input_file(path_to_input: str) -> str:
    """Checks if the input file is in the binary format.

    Args:
        path_to_input (str): Path to the input file.

    Returns:
        str: MD5 hash value of binary file.
    """
    try:
        with open(path_to_input, mode="rb") as input_file:
            data = input_file.read()
            md5_hash = hashlib.md5(data).hexdigest()
            return md5_hash
    except FileNotFoundError:
        print(f"The file {path_to_input} does not exist.")


def check_length_value(length_arg: str) -> int:
    """Checks if the input value for length is bigger than zero.

    Args:
        length_arg (str): Length value from argument parameters.

    Returns:
        int: Checked length value.
    """
    try:
        length = int(length_arg)
        if length > 0:
            return length
    except ValueError:
        print("Length value should be bigger than 0.")


def get_nucleotide(bits: str) -> str:
    """Gets the nucleotide from the 2 bits from input.

    Args:
        bits (str): The first 2 bits of the one record.

    Returns:
          str: Right nucleotide.
    """
    match bits:
        case "00":
            return "A"
        case "01":
            return "C"
        case "10":
            return "G"
        case "11":
            return "T"
        case _:
            print("Wrong input - it should be '00', '01', '10' or '11'.")


def get_fastq_format(sequence: str, quality_scores: str) -> str:
    """Writes the DNA sequence of length L in FASTQ format output.

    Args:
        sequence (str): Sequence DNA of length L.
        quality_scores (str): Quality scores every nucleotide of the sequence DNA.

    Returns:
        str: FASTQ format of the DNA sequence (four lines).
    """
    first_line = '@READ_' + str(num)
    third_line = '+READ_' + str(num)
    fastq_template = Template(f'$first_line\n$sequence\n$third_line\n$quality_scores')
    return (fastq_template.substitute(first_line=first_line, sequence=sequence, third_line=third_line,
                                      quality_scores=quality_scores))


# Loading and checking the input parameters
path_to_input_file = sys.argv[0]
md5_hash = check_input_file(path_to_input_file)
length = check_length_value(sys.argv[1])
num = 1
output_file = open("Output" + str(length), "w")

# Going through the file
input_file = open("C:\\Users\\lucie\\OneDrive\\Plocha\\input", mode="rb")
sequence_length = input_file.read(length)
while sequence_length:
    data_array = [f"{n:08b}" for n in sequence_length]
    sequence = ""
    quality_scores = ""
    for element in data_array:
        sequence += get_nucleotide(element[:2])
        quality_scores += chr(int(element[-6:], 2) + 33)
    output_file.write(get_fastq_format(sequence, quality_scores))
    output_file.write("\n")
    num += 1
    sequence_length = input_file.read(length)
output_file.close()
