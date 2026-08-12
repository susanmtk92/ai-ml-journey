def add_setting(settings_dict, key_value_tuple):
    # Unpack and convert key and value to lowercase
    key, value = key_value_tuple
    key = str(key).lower()
    value = str(value).lower()
    
    # Check if the key already exists
    if key in settings_dict:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    
    # Add new setting
    settings_dict[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings_dict, key_value_tuple):
    # Unpack and convert key and value to lowercase
    key, value = key_value_tuple
    key = str(key).lower()
    value = str(value).lower()
    
    # Check if the key exists to update it
    if key in settings_dict:
        settings_dict[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(settings_dict, key):
    # Convert key to lowercase
    key = str(key).lower()
    
    # Check if the key exists to delete it
    if key in settings_dict:
        del settings_dict[key]
        return f"Setting '{key}' deleted successfully!"
        
    return "Setting not found!"


def view_settings(settings_dict):
    # Return message if dictionary is empty
    if not settings_dict:
        return "No settings available."
    
    # Format and capitalize keys for display
    output_lines = ["Current User Settings:"]
    for key, value in settings_dict.items():
        output_lines.append(f"{key.capitalize()}: {value}")
        
    print(output_lines)
    return "\n".join(output_lines)+'\n'


# Create test_settings dictionary for testing the application
test_settings = {
    'theme': 'dark',
    'language': 'english',
    'notifications': 'enabled'
}