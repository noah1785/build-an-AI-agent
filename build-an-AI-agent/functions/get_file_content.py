import os
from config import *
from google.genai import types

def get_file_content(working_directory, file_path):
    try:
        working_dir = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(working_dir,file_path))
        valid_target_file_path = os.path.commonpath([working_dir, target_file_path]) 

        if valid_target_file_path != working_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        else:
            is_file = os.path.isfile(target_file_path)
            if is_file == False:
                return f'Error: File not found or is not a regular file: "{file_path}"'
            else:
                

                with open(target_file_path, "r") as f:
                    file_content_string = f.read(MAX_CHARS)

                    if f.read(1):
                        file_content_string += f'[...File "{target_file_path}" truncated at {MAX_CHARS} characters]'

                    return file_content_string

    except Exception as e:
        return f"Error: {e}"

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read content of files from a specified file relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file from which content will be read",
            ),
        },
    ),
)