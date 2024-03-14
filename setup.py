from setuptools import setup,find_packages

def get_file(file_path):
    require=[]
    with open(file_path) as f:
        require=f.readlines()

        require= [file.replace("\n","") for file in require]

        if("-e ." in require):
            require.remove("-e .")
        
    return require


setup(
   name='SQL Case_study',
   version='0.0.1',
   description='Case study on Student performance indicator',
   author='Sasmiullah',
   author_email='sami606713@gmail.com',
   packages=find_packages(),
   install_requires=get_file("requirements.txt")
)
