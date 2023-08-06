from setuptools import setup, find_packages
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='fairmaterials',
    version='0.0.3',
    keywords=['FAIRification','PowerPlant','Engineering'],
    description='Generate  json-ld format file based on FAIRification standard',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://engineering.case.edu/centers/sdle/',
    author='Roger French(ORCID:000000-0002-6162-0532), Mingjian Lu,Liangyi Huang(ORCID:0000-0003-0845-3293), Will Oltjen(ORCID:0000-0003-0380-1033),Xuanji Yu,Arafath Nihar, Tommy Ciardi, Erika Barcelos,Pawan Tripathi,Abhishek Daundkar,Deepa Bhuvanagiri,Hope Omodolor,Hein Htet Aung,Kristen Hernandez,Mirra Rasmussen,Raymond Wieser, Sameera Nalin Venkat,Tian Wang, Weiqi Yue, Yangxin Fan,Rounak Chawla,Leean Jo,Zelin Li,Jiqi Liu, Justin Glynn, Kehley Coleman,Yinghui Wu, Laura Bruckman,Jeffery Yarus, Kris Davis',
    author_email='roger.french@case.edu, mxl1171@case.edu,lxh442@case.edu, wco3@case.edu,xxy530@case.edu ,arafath@case.edu ',


    # BSD 3-Clause License:
    # - http://choosealicense.com/licenses/bsd-3-clause
    # - http://opensource.org/licenses/BSD-3-Clause
    license='BSD License (BSD-3)',
    packages=find_packages(),
    include_package_data=True,
)