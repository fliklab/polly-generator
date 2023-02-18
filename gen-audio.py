import sys
import os
import boto3
import re

def convert_to_mp3_filename(sentence, count):
    # Remove all non-alphanumeric characters and replace spaces with underscores
    filename = re.sub('[^0-9a-zA-Z]+', '_', sentence).strip('_')
    # Add the numbering scheme and .mp3 file extension
    filename = f"{count:03d}_{filename}.mp3"
    return filename


# Set up the client
polly_client = boto3.Session(
    aws_access_key_id='AKIAXWBZ3TC7AOTKTIPZ',
    aws_secret_access_key='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',
    region_name='ap-northeast-2').client('polly')


# Set up the parameters for the synthesis
voice_id = 'Salli'
output_format = 'mp3'

# Get the input file name from the command line argument
input_file = sys.argv[1]

# Create the output folder if it doesn't exist
output_folder = os.path.splitext(input_file)[0]
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Read the input text from the file
with open(input_file, 'r') as f:
    lines = f.read().splitlines()

# Loop over the lines and synthesize the speech for each one
for count, line in enumerate(lines):
    filename = os.path.join(output_folder, convert_to_mp3_filename(line, count))
    # Call the Amazon Polly API to synthesize the speech
    response = polly_client.synthesize_speech(
        Text=line,
        VoiceId=voice_id,
        OutputFormat=output_format)
    # Save the audio file to disk
    audio_file = open(filename, 'wb')
    audio_file.write(response['AudioStream'].read())
    audio_file.close()