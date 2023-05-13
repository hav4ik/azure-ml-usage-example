# azure-ml-usage-example

This repository contains a sample code for Azure ML usage.
* [submit_experiment.ipynb](submit_experiment.ipynb) - a notebook that submits an experiment to Azure ML
* [sample_code](sample_code) - a folder with a sample training code that uses a registered AzureML dataset and uploads a file to the default datastore.

Best practices:
* If you're using `V100` or `T4` computes (`gpu-v100-x1` or `gpu-t4-lp`), it is **strongly** advised to train in `FP16` or `BF16`. 16-bit training will accelerate your pipeline and allow you to use larger batch sizes.
* Since the warmup time on AzureML is long, please consider experimenting on a local machine or Google Colab first, and then submit the job to AzureML once you're 100% sure that your code is working.
* Cancel the job if you see that it's not working to save resources. You can always submit a new job. Be frugal and respect others in the workspace!

# WARNING! IMPORTANT! READ THIS!

Both datastore and compute clusters in this workspace is located in *West US 2* region. The data transfer cost from Ukraine can be very high. Please be careful when uploading large datasets to the workspace, or when downloading a large amount of data from the workspace. One time upload/download is fine, just don't do it every time you run the experiment.

### Fun story

I once spent $300 in just a week on data transfer costs because I was downloading 100GB of data from a remote data source every time I ran the experiment. Don't be like me. I know a guy that works in Azure SQL team, that once lost $200'000 of his team's budget because he accidentally moved petabytes of data between regions. Don't be like him either.