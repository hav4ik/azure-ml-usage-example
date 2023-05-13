from azureml.core import Run, Dataset, Workspace
import os
import subprocess
import sys

# Install packages
subprocess.check_call([sys.executable, "-m", "pip", "install", "transformers"])

# Import installed packages
import transformers

# get the Azure ML run object
run = Run.get_context()

# get workspace
workspace = run.experiment.workspace

# Mount the dataset to local path
dataset = Dataset.get_by_name(workspace=workspace, name='sample_dataset')
mount_context = dataset.mount()
mount_context.start()
data_path = mount_context.mount_point

# List files in the dataset
print(f"Files in dataset (mounted at {data_path}):")
print(os.listdir(data_path))

# Get default datastore
datastore = workspace.get_default_datastore()

# Create a sample file
with open('sample_data.txt', 'w') as f:
    f.write('This is sample data.')

# Upload a file to the datastore. You can use this to checkpoint your model files
datastore.upload_files(
    files=['sample_data.txt'],
    target_path='outputs/sample_upload',
    overwrite=True)
