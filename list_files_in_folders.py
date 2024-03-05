import os

def list_files_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        return files,None
    except FileNotFoundError:
        return None , "File Not Found"
    except PermissionError:
        return None, "Permission Denied"
    
def main():
    folder_path = input("Enter the folder paths to the list the files with a space:").split()

    for folder_path in folder_path:
        files, error_message = list_files_in_folder(folder_path)
        if files:
            print(f"Files in {folder_path}:")
            for file in files:
                print(file)
        else:
            print(f"error in {folder_path}: {error_message}")


if __name__ == "__main__":
    main()
    

    
 

   
