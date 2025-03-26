from huggingface_hub import list_repo_files, hf_hub_download
import os

# Define repository and search pattern
repo_id = "sail/Sailcompass_data"
repo_type = "dataset"
local_dir = "data/"

patterns = ["vie_", "vi_", "_vi", "vietnamese"]  # Patterns to match in filenames
folders = ["vsmec", "xlsum_vi"]

# List all files in the repo (including those in subfolders)
files = list_repo_files(repo_id=repo_id, repo_type=repo_type)

# Filter files that match the patterns inside any folder
matching_files = [f for f in files if any(p in os.path.basename(f) for p in patterns)]

# Filter files that are in any of the specified folders
matching_files += [f for f in files if any(f"{folder}/" in f for folder in folders)]

for file in matching_files:
    file_path = hf_hub_download(
        repo_id=repo_id,
        filename=file,  # Full path relative to repo root
        repo_type=repo_type,
        local_dir= 'data/',
        local_dir_use_symlinks=False,
    )