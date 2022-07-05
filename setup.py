# TODO: add packages description?

import setuptools

with open("./README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='sla_model_postprocessing_playground',
    version='0.2a',
    author="Roman Stanek",
    author_email="rnsk@seznam.cz",
    description="Testing various approaches for postprocessing 3d model for SLA printer to achieve better print quality",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['bin', 'src'], 
)