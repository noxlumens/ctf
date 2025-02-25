#!/bin/bash
# derived from https://stackoverflow.com/questions/41306350/how-to-generate-password-hash-for-rabbitmq-management-http-api
function decode_password()
{
    ENCODED_PASS=$1
    
    # Decode from base64
    DECODED_PASS=$(echo -n "$ENCODED_PASS" | base64 -d | xxd -ps | tr -d '\n' | tr -d ' ')
    
    # Extract the salt (first 8 characters / 4 bytes in hex)
    SALT=${DECODED_PASS:0:8}
    
    # Extract the hashed portion
    HASHED_PART=${DECODED_PASS:8}
    
    echo "Salt: $SALT"
    echo "Password: $HASHED_PART"
}

# Example usage
decode_password "$1"
