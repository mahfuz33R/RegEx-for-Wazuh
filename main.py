#!/usr/bin/python3
import re
import pyfiglet 

result = pyfiglet.figlet_format("RegEx  for Wazuh") 
print(result) 


def encode_text(text):
    # Define the regex patterns and their replacements
    patterns = {
        r'[A-Za-z@_\-]': r'\w',
        r'[0-9]': r'\d',
        r'\s': r'\s',
        r'\t': r'\t',
        r'[()*+,-.:;<=>?\[\]!"\'#$%&|{}]': r'\p',
        r'[^\w\s\d]': r'\W',
        r'[^\d\s\w]': r'\D',
        r'[^\s\w\d]': r'\S',
        r'[^A-Za-z0-9\s\t()*+,-.:;<=>?\[\]!"\'#$%&|{}]': r'\.'
    }
    
    # Function to replace a match
    def replace_match(match):
        char = match.group(0)
        for pattern, replacement in patterns.items():
            if re.match(pattern, char):
                return replacement
        return char
    
    # Encode the text
    encoded_parts = []
    current_replacement = None
    count = 0

    for char in text:
        replacement = replace_match(re.match(r'.', char))
        if replacement == current_replacement:
            count += 1
        else:
            if current_replacement is not None:
                if count > 1:
                    encoded_parts.append(current_replacement + '+')
                else:
                    encoded_parts.append(current_replacement)
            current_replacement = replacement
            count = 1

    # Append the last accumulated replacement
    if current_replacement is not None:
        if count > 1:
            encoded_parts.append(current_replacement + '+')
        else:
            encoded_parts.append(current_replacement)
    
    return ''.join(encoded_parts)

# Example usage
# text = "A Jul m14 2024 ? 14:44:31 5"


text = "Jul 14 2024 14:44:31 SK_DK_S5731_S01 %%01CM/5/USER_ACCESSRESULT(s)[137]:[USER_INFO_AUTHENTICATION]DEVICEMAC:b8-d6-f6-97-e0-40;DEVICENAME:M&H_DK_S5731_S01;USER:netadmin;MAC:ff-ff-ff-ff-ff-ff;IPADDRESS:192.168.198.60;IPV6ADDRESS:-;TIME:1720968271;ZONE:UTC+0600;DAYLIGHT:false;ERRCODE:0;RESULT:success;CIB ID:16;ACCESS TYPE:SSH;RDSIP:-;Portal TYPE:-;AUTHID=4294967295;AuthFailType:None;AUTHPROTOCOL:-;"


encoded_text = encode_text(text)
print(f"\nOriginal Text: {text}")
print(f"\n\nEncoded Text: {encoded_text}")
