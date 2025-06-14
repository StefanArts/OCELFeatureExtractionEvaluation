import yaml

def clean_yaml_file(input_file, output_file):
    # Read the file in binary mode to handle encoding issues
    with open(input_file, 'rb') as f:
        content = f.read()
    
    # Remove null bytes and other problematic characters
    content = content.replace(b'\x00', b'')  # Remove null bytes
    content = content.replace(b'\x82', b'')  # Remove other special chars
    
    # Write back as UTF-8
    with open(output_file, 'wb') as f:
        f.write(content)
    
    # Now try to load the cleaned file
    with open(output_file, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

# Clean your file first
try:
    env_data = clean_yaml_file('environment.yml', 'environment_clean.yml')
    print("File cleaned successfully!")
except Exception as e:
    print(f"Error: {e}")
