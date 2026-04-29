import os

def write_file(working_directory, file_path, content):
    try:
        working_dir = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(working_dir,file_path))
        valid_target_file_path = os.path.commonpath([working_dir, target_file_path]) 

        if valid_target_file_path != working_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        else:
            is_dir = os.path.isdir(target_file_path)
            if is_dir == True:
                return f'Error: Cannot write to "{file_path}" as it is a directory'
            else:
                parent_dir = os.path.dirname(target_file_path)
                os.makedirs(parent_dir, exist_ok=True)
                with open(target_file_path, "w") as f:
                    f.write(content)
                    
                    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"