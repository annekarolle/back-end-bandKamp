# M5 - BandKamp Generic View

A partir de um código legado de uma API de musicas com APIVIEWS, Serializer Base e SQLite3, foi feito a transição para Generic Views, Model Serializer e Postgres.
Link do deploy da aplicação feito no RailWay: <a href="https://m5-bandkamp-annekarolle-production.up.railway.app/ ">https://m5-bandkamp-annekarolle-production.up.railway.app/ </a>



## Diagrama de Classe
![Screenshot](Diagrama.BANDKAMP.png)


## Instalação dos pacotes de teste

<details>
  <summary></summary>


- Verifique se os pacotes `pytest` e/ou `pytest-testdox` estão instalados globalmente em seu sistema:
```shell
pip list
```
- Caso seja listado o `pytest` e/ou `pytest-testdox` e/ou `pytest-django` em seu ambiente global, utilize os seguintes comando para desinstalá-los globalmente:
```shell
pip uninstall pytest
```

```shell
pip uninstall pytest-testdox
```

```shell
pip uninstall pytest-django
```

A partir disso, prossiga com os passos:

1. Crie seu ambiente virtual:
```bash
python -m venv venv
```

2. Ative seu venv:
```bash
# linux:
source venv/bin/activate

# windows:
.\venv\Scripts\activate
```

3. Instale o pacote `pytest-testdox`:
```shell
pip install pytest-testdox pytest-django
```


4. Agora é só rodar os testes no diretório principal do projeto:
```shell
pytest --testdox -vvs
```

5. Caso queira um log mais resumido, basta executar com os testes sem as flags **verbose**:
```shell
pytest --testdox
```

## Rodando os testes por partes

Caso você tenha interesse em rodar apenas um diretório de testes específico, pode utilizar o comando:

- Rodando testes de users:
```python
pytest --testdox -vvs tests/users/
```

- Rodando testes de albums:
```python
pytest --testdox -vvs tests/albums/
```

- Rodando testes de songs:
```python
pytest --testdox -vvs tests/songs/
```

</details>

## Tecnologias

<div>
<img align="center" alt="css" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img align="center" alt="css" src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white">
  
</div>
