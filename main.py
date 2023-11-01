"""This is program for  DNA sequence conversion. It accepts at the entrance the binary input file which contains \
multiple consecutive entries which are DNA molecules. The program prints on standard output the contents of the input \
file in FASTQ format."""
import hashlib
import sys
from string import Template


def check_input_file(path_to_input: str) -> bool:
    """Checks if the input file is in the binary format.

    Args:

    Returns:

    """
    try:
        with open(path_to_input, mode="rb") as input_file:
            data = input_file.read()
            md5_hash = hashlib.md5(data).hexdigest()
            print(md5_hash)
    except FileNotFoundError:
        print(f"The file {path_to_input} does not exist.")


def get_sequence(data_array: list) -> list:
    """Gets the sequence of nucleotides.

    :return:
    """
    res_sequence = []
    for element in data_array:
        match element[:2]:
            case "00":
                res_sequence.append("A")
            case "01":
                res_sequence.append("C")
            case "10":
                res_sequence.append("G")
            case "11":
                res_sequence.append("T")
            case _:
                print("Wrong input - it should be '00', '01', '10' or '11'.")
        # ele = element[:2]
        # if ele == "00":
        # res_sequence.append("A")
        # f ele == "01":
        # res_sequence.append("C")
        # elif ele == "10":
        # res_sequence.append("G")
        # else:
        # res_sequence.append("T")
    return res_sequence

    # print(element[:2])


def get_quality_score(data_array: list) -> list:
    """

    :param data_array:
    :return:
    """
    quality_scores = []
    for element in data_array:
        # print(data_array)
        # helper = str('b\"' + element[-6:] + '\"')
        # new_array = [x[-6:] for x in data_array]
        quality_scores.append(chr(int(element[-6:], 2) + 33))
        # binary_string = "010010"
        # print(int(binary_string,2)+33)
        # print(chr(int(binary_string,2)+33))
        # print(binary_to_string(data_array))
        # print(binascii.b2a_uu(bin(element[-6:])))
        # print(helper)
    return quality_scores


def binary_to_string(bits):
    # print(bits)
    return ''.join([chr(int(i, 2)) for i in bits])


def get_fastq_format(sequence, quality):
    identifier = '@READ_' + str(num)
    plus_sign = '+READ_' + str(num)
    seq = ''.join(sequence)
    jedna = ''.join(quality)

    fastq_template = Template(f'$identifier\n$seq\n$plus_sign\n$jedna')
    print(fastq_template.substitute(identifier=identifier, seq=seq, plus_sign=plus_sign, jedna=jedna))


# Loading and checking the input file

# input_file = open("C:\\Users\\lucie\\OneDrive\\Plocha\\input", mode="rb")

# path_to_input_file = "C:\\Users\\lucie\\OneDrive\\Plocha\\input"
path_to_input_file = sys.argv[0]
check_input_file(path_to_input_file)

# data = input_file.read()
# md5_hash = hashlib.md5(data).hexdigest()
# print(md5_hash)


# Reading the input file
# print([f"{n:08b}" for n in data])

# parameter
length = 7
num = 1

# going throw
input_file = open("C:\\Users\\lucie\\OneDrive\\Plocha\\input", mode="rb")
data_length = input_file.read(length)
while data_length:
    data_array = [f"{n:08b}" for n in data_length]
    # print(type(data_array[0]))

    # TODO: funkce na encoding pismene
    result_seq = get_sequence(data_array)
    # print(result_seq)

    # TODO: funkce na encoding
    res_quality = get_quality_score(data_array)
    # print(res_quality)

    # TODO: Template for FASTQ file
    get_fastq_format(result_seq, res_quality)
    num += 1

    data_length = input_file.read(length)
