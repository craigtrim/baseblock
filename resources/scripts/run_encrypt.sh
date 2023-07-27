#!/bin/bash

# Script Information
#
# Script Name: Run-Encrypt.sh
# Description: Encrypt any Input Text
# Usage: ./Run-Encrypt.sh "012345"

# Input Text provided as command-line argument
inputText="$1"

# Check if inputText is not provided
if [ -z "$inputText" ]; then
    echo "Error: Input text is missing. Usage: ./Run-Encrypt.sh <input_text>"
    exit 1
fi

# Execute the encryption using the 'crypto_base.py' script
poetry run python ./baseblock/crypto_base.py "encrypt" "$inputText"
