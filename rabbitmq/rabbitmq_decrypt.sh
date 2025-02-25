#!/bin/bash

function decode_password()
{
    ENCODED_PASS=$1
    
    # Decode from base64
    DECODED_PASS=$(echo -n "$ENCODED_PASS" | base64 -d | xxd -ps | tr -d '\n' | tr -d ' ')
    
    # Extract the salt (first 8 characters / 4 bytes in hex)
    SALT=${DECODED_PASS:0:8}
    
    # Extract the hashed portion
    HASHED_PART=${DECODED_PASS:8}
    
    echo "Salt (Hex): $SALT"
    echo "Password (SHA256, Hex): $HASHED_PART"
}

# Example usage
decode_password "$1"
