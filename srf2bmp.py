#!/usr/bin/env python3

import os
import sys

"""
OK OK
The thing to do here is use a standard header 54 bytes
with the size 3249x90, and over write the Naviga.srf with the standard header. 

to go back, over write the start with the eh garmin 54 byte SRF header.
47 41 52 4D 49 4E 20 42 49 54 4D 41 50 20 30 31 04 00 00 00 04 00 00 00 02 00 00 00 05 00 00 00 03 00 00 00 35 37 38 06 00 00 00 04 00 00 00 32 2E 30 30 07 00 00 00
###STD bmp header DIMensioned 3240x90
42 4D 66 59 0D 00 00 00 00 00 36 00 00 00 28 00 00 00 A8 0C 00 00 5A 00 00 00 01 00 18 00 00 00 00 00 30 59 0D 00 13 0B 00 00 13 0B 00 00 00 00 00 00 00 00 00 00
###STD bmp header DIMensioned
###STD bmp header DIMensioned
###STD bmp header DIMensioned

"""
# all this is borked, but ill fix it after i nap


def overwrite_bmp_header(input_file):
    # Check if the input file exists
    if not os.path.isfile(input_file):
        print(f"Error: The file '{input_file}' does not exist.")
        sys.exit(1)

    # Extract the base name without extension to form the output filename
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_file = f'{base_name}.bmp'

    # Define the custom 14-byte BMP header you provided
    #custom_bmp_header = bytes([0x42, 0x4D, 0x3A, 0xE6, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x8A, 0x00, 0x00, 0x00])
    custom_bmp_header = bytes([0x42, 0x4D, 0x3A, 0xE6, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x8A, 0x00, 0x00, 0x00, 0x7C, 0x00, 0x00, 0x00])

    # Read the original file
    try:
        with open(input_file, 'rb') as f:
            srf_data = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    # Overwrite the first 14 bytes with the custom BMP header
    #new_data = custom_bmp_header + srf_data[14:]
    new_data = custom_bmp_header + srf_data[18:]

    # Write the new BMP file
    try:
        with open(output_file, 'wb') as f:
            f.write(new_data)
        print(f"Conversion successful! File saved as: {output_file}")
    except Exception as e:
        print(f"Error writing the BMP file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Check if input argument is provided
    if len(sys.argv) != 2:
        print("Usage: python overwrite_bmp_header.py <input_file.srf>")
        sys.exit(1)

    # Input file from command line
    input_file = sys.argv[1]

    # Call the function to overwrite the BMP header
    overwrite_bmp_header(input_file)

