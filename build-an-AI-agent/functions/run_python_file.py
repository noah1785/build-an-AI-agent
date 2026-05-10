import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir = os.path.abspath(working_directory)
        target_file_path = os.path.abspath(os.path.join(working_dir,file_path))
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
                    if args is None:
                        args = []
                    command.extend(args)
                    result = subprocess.run(command, cwd=working_dir, capture_output=True, text=True, timeout=30)

                    output = ""

                    if result.returncode != 0:
                        output += f"Process exited with code {result.returncode}\n"

                    if not result.stdout and not result.stderr:
                        output += "No output produced"

                    if result.stdout:
                        output += f"STDOUT: {result.stdout}"

                    if result.stderr:
                        output += f"STDERR: {result.stderr}"

                    return output

    except Exception as e:
        return f"Error: executing Python file: {e}"