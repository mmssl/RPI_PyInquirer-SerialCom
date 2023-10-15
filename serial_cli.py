#!/usr/bin/env python3

import serial
from pprint import pprint
from PyInquirer import prompt, Separator
from examples import custom_style_2

questions = [
    {
        'type': 'list',
        'name': 'port',
        'message': 'Select Port',
        'choices': ['/dev/ttyAMA0', '/dev/ttyS0']
    },
    {
        'type': 'list',
        'name': 'baudrate',
        'message': 'Select Baudrate',
        'choices': ['9600', '57600', '115200']
    },
    {
        'type': 'list',
        'name': 'bytesize',
        'message': 'Select Bytesize',
        'choices': ['7', '8']
    },
    {
        'type': 'list',
        'name': 'stopbits',
        'message': 'Select Stopbit',
        'choices': ['0', '1']
    },
    {
        'type': 'list',
        'name': 'parity',
        'message': 'Select Parity',
        'choices': ['E', 'O', 'N']
    }
]

answers = prompt(questions, style=custom_style_2)

# Creating serial connection with user-selected parameters
ser = serial.Serial(
    port=answers['port'],
    baudrate=int(answers['baudrate']),
    bytesize=int(answers['bytesize']),
    stopbits=int(answers['stopbits']),
    parity=answers['parity']
)

try:
    data_to_send = [1, 2, 3, 4, 5]  # Replace with your data
    data_to_send_bytes = bytes(data_to_send)

    # Send data
    ser.write(data_to_send_bytes)
    print(f"Sent: {data_to_send_bytes}")

    # Receive and print the data back
    received_data = ser.read(len(data_to_send_bytes))
    print(f"Received: {received_data}")

except Exception as e:
    print(f"Error: {str(e)}")

finally:
    ser.close()


pprint(f"Serial connection established with parameters: Port: {answers['port']}, Baudrate: {answers['baudrate']}, Bytesize: {answers['bytesize']}, Stopbit: {answers['stopbits']}, Parity: {answers['parity']}")
