# Example experiment code folder

This folder contains a sample experiment code. The simple `train.py` script does the following:

* Installs additional dependencies (in this example, the `transformers` library) by calling a subprocess:
    ```python
    import subprocess
    import sys

    # Install packages
    subprocess.check_call([sys.executable, "-m", "pip", "install", "transformers"])

    # Import installed packages
    import transformers
    ```
  It's not the best way to install packages, but it's a simplest way to do it. The "right" way would be to build a custom environment and use it in the experiment. However, building your own environment would take a lot of time to make it right.

* Mounts the dataset from the datastore with the following code:
    ```python
    # get the Azure ML run object
    run = Run.get_context()

    # get workspace
    workspace = run.experiment.workspace

    # Mount the dataset to local path
    dataset = Dataset.get_by_name(workspace=workspace name='sample_dataset')
    mount_context = dataset.mount()
    mount_context.start()

    # get the mount path on the compute's local file system
    data_path = mount_context.mount_point
    ```
  This can be used to mount your custom dataset.

* Uploads a file to the default datastore with:
    ```python
    # Get default datastore
    datastore = workspace.get_default_datastore()

    # Upload a file to the datastore. You can use this to checkpoint your model files
    datastore.upload_files(
        files=['sample_data.txt'],
        target_path='outputs/sample_upload',
        overwrite=True)
    ```
  This can be used to upload your model checkpoints.