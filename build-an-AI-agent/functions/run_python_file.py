import os

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(working_dir,file_path))
        valid_target_file_path = os.path.commonpath([working_dir, target_file_path]) 

        if valid_target_file_path != working_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        else:
            is_file = os.path.isfile(target_file_path)
            if is_file == False:
                return f'Error: "{file_path}" does not exist or is not a regular file'
            else:
                is_python_file = file_path.endswith('.py')
                if is_python_file == False:
                    return f'Error: "{file_path}" is not a Python file'
                else:
                    command = ["python", target_file_path]
                    command.extend(args)

    except Exception as e:
        return f"Error: {e}"