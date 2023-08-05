# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['omics', 'omics.transfer']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.26.19,<2.0.0',
 'mypy-boto3-omics>=1.26.19,<2.0.0',
 's3transfer>=0.6.0,<0.7.0']

setup_kwargs = {
    'name': 'amazon-omics-tools',
    'version': '0.1.1',
    'description': 'Tools for working with the Amazon Omics Service',
    'long_description': '# Amazon Omics Tools\n\nTools for working with the Amazon Omics Service.\n\n## Using the Omics Transfer Manager\n\n### Basic Usage\nThe `TransferManager` class makes it easy to download files for an Omics reference or read set.  By default the files are saved to the current directory, or you can specify a custom location with the `directory` parameter.\n\n```python\nimport boto3\nfrom omics.transfer import ReferenceFileName, ReadSetFileName\nfrom omics.transfer.manager import TransferManager\nfrom omics.transfer.config import TransferConfig\n\nREFERENCE_STORE_ID = "<my-reference-store-id>"\nSEQUENCE_STORE_ID = "<my-sequence-store-id>"\n\nclient = boto3.client("omics")\nmanager = TransferManager(client)\n\n# Download all files for a reference.\nmanager.download_reference(REFERENCE_STORE_ID, "<my-reference-id>")\n\n# Download all files for a read set to a custom directory.\nmanager.download_read_set(SEQUENCE_STORE_ID, "<my-read-set-id>", "my-sequence-data")\n```\n\n### Download specific files\nSpecific files can be downloaded via the `download_reference_file` and `download_read_set_file` methods.\nThe `client_fileobj` parameter can be either the name of a local file to create for storing the data, or a `TextIO` or `BinaryIO` object that supports write methods.\n\n```python\n# Download a specific reference file.\nmanager.download_reference_file(\n    REFERENCE_STORE_ID,\n    "<my-reference-id>",\n    ReferenceFileName.INDEX\n)\n\n# Download a specific read set file with a custom filename.\nmanager.download_read_set_file(\n    SEQUENCE_STORE_ID,\n    "<my-read-set-id>",\n    ReadSetFileName.INDEX,\n    "my-sequence-data/read-set-index"\n)\n```\n\n### Subscribe to events\nTransfer events: `on_queued`, `on_progress`, and `on_done` can be observed by defining a subclass of `OmicsTransferSubscriber` and passing in an object which can receive events.\n\n```python\nclass ProgressReporter(OmicsTransferSubscriber):\n    def on_queued(self, **kwargs):\n        future: OmicsTransferFuture = kwargs["future"]\n        print(f"Download queued: {future.meta.call_args.fileobj}")\n\n    def on_done(self, **kwargs):\n        print("Download complete")\n\nmanager.download_read_set(SEQUENCE_STORE_ID, "<my-read-set-id>", subscribers=[ProgressReporter()])\n```\n\n### Threads\nTransfer operations use threads to implement concurrency. Thread use can be disabled by setting the `use_threads` attribute to False.\n\nIf thread use is disabled, transfer concurrency does not occur. Accordingly, the value of the `max_request_concurrency` attribute is ignored.\n\n```python\n# Disable thread use/transfer concurrency\nconfig = TransferConfig(use_threads=False)\nmanager = TransferManager(client, config)\nmanager.download_read_set(SEQUENCE_STORE_ID, "<my-read-set-id>")\n```\n\n## Security\n\nSee [CONTRIBUTING](https://github.com/awslabs/amazon-omics-tools/blob/main/CONTRIBUTING.md#security-issue-notifications) for more information.\n\n## License\n\nThis project is licensed under the Apache-2.0 License.\n',
    'author': 'Amazon Web Services',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/awslabs/amazon-omics-tools',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
