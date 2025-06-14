# processando-imagens-em-python
>>>Em desenvolvimento


Project_name/
    README.md
    setup.py
    requirements.txt
    package_name/
        __init__.py
        module1_name/
            __init__.py
            file1_name.py
            file2_name.py
        module2_name/
            __init__.py
            file1_name.py
            file2_name.py


setup.py -> especifica como o pacote deve ser construído.
requirements.txt -> passa as dependências que devem ser instaladas com o seu pacote.
README.md -> exibido como documentação na página do Pypi do seu pacote. Foi usado markdown.

pip install package_name

from package_name.module1_name.file1_name import file1_name
file1_name.my_function()

file1_name
import package_name.module1_name.file1_name

from package_name.module1_name.file1_name import file1_name

#Comandos de instalação
python -m pip install --upgrade pip
python -m pip install --user twine
python -m pip install --user setuptools

#Comandos para criar Distribuições
python setup.py sdist bdist_wheel

#Passos para subir o pacote

1- Criar conta no Test Pypi
2- Publicar no Test Pypi
3- Instalar pacote usando Test Pypi
4- Testar pacote
5- Criar conta no Pypi
6- Publicar no Pypi
7- Instalar pacote usando Pypi

#Criando contas no Pypi
https://pypi.org/account/register/
https://test.pypi.org/account/register/

#Comando para publicar no Test Pypi
python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

#Comando para instalar o pacote de teste
pip install –-index-url https://test.pypi.org/simple/ image-processing

```bash
    pip install package_name
```

## Autor
Genilson da Silva Junior

