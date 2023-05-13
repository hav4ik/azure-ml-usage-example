# azure-ml-usage-example

This repository contains a sample code for Azure ML usage.
* [submit_experiment.ipynb](submit_experiment.ipynb) - a notebook that submits an experiment to Azure ML
* [sample_code](sample_code) - a folder with a sample training code that uses a registered AzureML dataset and uploads a file to the default datastore.

Best practices:
* If you're using `V100` or `T4` computes (`gpu-v100-x1` or `gpu-t4-lp`), it is **strongly** advised to train in `FP16` or `BF16`. 16-bit training will accelerate your pipeline and allow you to use larger batch sizes.
* Since the warmup time on AzureML is long, please consider experimenting on a local machine or Google Colab first, and then submit the job to AzureML once you're 100% sure that your code is working.
* Cancel the job if you see that it's not working to save resources. You can always submit a new job. Be frugal and respect others in the workspace!
