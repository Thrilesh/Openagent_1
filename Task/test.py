# Example test cases
from utility_function import format_chat_template

test_inputs = [
    "how are things going, tell me about Delhi",
    "{{gen 'write'}}",
    "{{#user}}Hello!{{/user}}",
    "{{#assistant}}{{gen 'rewrite'}}{{/assistant}}"
]

for input_text in test_inputs:
    formatted_output = format_chat_template(input_text)
    print("Input:", input_text)
    print("Formatted Output:", formatted_output)
    print("=" * 40)
