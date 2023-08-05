import setuptools

setuptools.setup(
name="conet",
    version="0.0.1",
    author="Agustin Brusco, Eitan Sprejer, Facundo Joaquin Garcia",
    description="Network analysis tools for computers with small amount of ram or large networks",
    packages=["conet", "conet.embedding", "conet.labels", "conet.utils", "conet.labels.propagators"],
    install_requires = ["numpy", "networkx", "gensim"]
)