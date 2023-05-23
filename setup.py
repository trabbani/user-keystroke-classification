from setuptools import setup, find_packages

setup(
    name='user-keystroke-classification',
    version='0.0.1',
    author='Tarek Rabbani',
    author_email='trabbani@berkeley.edu',
    description='A Python package that leverages machine learning to distinguish users based on their keystroke patterns.',
    url='https://github.com/your-username/user-keystroke-classification',
    packages=find_packages(),
    install_requires=[
        'numpy==1.23.5',
        'shap==0.41.0',
        'scikit-learn>=1.2.2',
        'seaborn>=0.12.2',
        'tqdm>=4.65.0',
        'xgboost>=1.7.5',
    ],

)
