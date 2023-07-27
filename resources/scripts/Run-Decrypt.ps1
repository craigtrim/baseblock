#!/bin/bash

# Script Information
#
# Script Name: Run-Decrypt.sh
# Description: Decrypt any Input Text
# Usage: ./Run-Decrypt.sh <key>

# Input Text provided as command-line argument
inputText="$1"

# Check if inputText is not provided
if [ -z "$inputText" ]; then
    echo "Error: Input text is missing. Usage: ./Run-Decrypt.sh <input_text>"
    exit 1
fi

# Execute the decryption using the 'crypto_base.py' script
poetry run python ./baseblock/crypto_base.py "decrypt" "$inputText"
