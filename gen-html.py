import os
import sys

# Get input name from command line argument
if len(sys.argv) < 2:
    print("Please provide the input name as a command line argument.")
    sys.exit(1)

input_name = sys.argv[1]

# Create audio and text file paths
audio_dir = input_name
text_file = f"{input_name}.txt"

# Read the contents of the text file and split into sentences
with open(text_file, 'r') as f:
    sentences = f.read().strip().split('\n')

# Get list of audio files sorted by starting number
audio_files = sorted([f for f in os.listdir(audio_dir) if f.endswith('.mp3') and f[:3].isdigit()])

# Create HTML file
with open(f'{input_name}.html', 'w') as f:
    f.write('<html>\n<body>\n')

    # Loop through sentences and corresponding audio files
    for sentence, audio_file in zip(sentences, audio_files):

        # Add audio and sentence to HTML file
        audio_path = os.path.join(audio_dir, audio_file)
        f.write(f'<p>{sentence}</p>\n')
        f.write(f'<audio controls><source src="{audio_path}" type="audio/mpeg"></audio>\n')

    f.write('</body>\n</html>')
