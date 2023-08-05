from setuptools import setup, find_packages

with open("requirements.txt", encoding="utf8") as r:
    requirements = r.read().split("\n")
    r.close()


setup(
   name='urmapi',
   version='1.2',
   description='A Decentralized Package Manager.',
   license="MIT",
   author='NoKodaAddictions',
   author_email='nokodaaddictions@gmail.com',
   url="https://nokodaaddictions.github.io",
   packages=find_packages(),
   install_requires=requirements
)

#2022 NoKodaAddictions