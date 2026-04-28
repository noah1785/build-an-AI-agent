import os

def get_files_info(working_directory, directory="."):
    
    try:
        working_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir,directory))
        valid_target_dir = os.path.commonpath([working_dir, target_dir]) 

        if valid_target_dir != working_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        else:
            is_dir = os.path.isdir(target_dir)
            if is_dir == False:
                return f'Error: "{directory}" is not a directory'
            else:
                file_details = []
                files_list = os.listdir(target_dir)
                for file in files_list:
                    full_path = os.path.join(target_dir, file)
                    file_size = os.path.getsize(full_path)
                    is_dir = os.path.isdir(full_path)
                    details = f"- {file}: file_size={file_size} bytes, is_dir={is_dir}"
                    file_details.append(details)

                return "\n".join(file_details)
                    
    except Exception as e:
        return f"Error: {e}"
