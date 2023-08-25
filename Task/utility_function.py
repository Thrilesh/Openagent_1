import re

def format_chat_template(text):
    formatted_text = ""
    
    try:
        parts = re.split(r'({{(?:#user|#assistant|gen \'write\'|gen \'rewrite\')}})', text)
        
        for part in parts:
            if part.startswith('{{#user}}'):
                formatted_text += "{{#user}}" + part[len('{{#user}}'):]
            elif part.startswith('{{#assistant}}'):
                formatted_text += "{{#assistant}}" + part[len('{{#assistant}}'):]
            elif part.startswith('{{gen \'write\'}}'):
                formatted_text += part
            elif part.startswith('{{gen \'rewrite\'}}'):
                formatted_text += "{{#assistant}}" + part[len('{{gen \'rewrite\'}}'):] + "{{/assistant}}"
            else:
                formatted_text += "{{#user}}" + part + "{{/user}}"
                
    except Exception as e:
        formatted_text = f"Error: {e}"
    
    return formatted_text

# Example usage
if __name__ == "__main__":
    provided_inputs = [
        "how are things going, tell me about Delhi",
        "{{gen 'write'}}",
        "{{#user}}Hello!{{/user}}",
        "{{#assistant}}{{gen 'rewrite'}}{{/assistant}}",
        "Tweak this proverb to apply to model instructions instead. Where there is no guidance{{gen 'rewrite'}}"
    ]
    
    for text in provided_inputs:
        formatted_output = format_chat_template(text)
        print("Input Text:", text)
        print("Formatted Output:", formatted_output)
        print("=" * 40)
