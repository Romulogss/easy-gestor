#Como preparar as dependências
 - Primeiro tenha o [python 3.9](https://www.python.org/downloads/) instalado
 - Abra o terminal e vá até o caminho desta pasta
 - rode o seguinte comando:
```commandline
python -m pip install -r requeriments.txt
```
 ##Rodando o serviço de buscar CNPJ
   - insira o seguinte comando no terminal, na pasta desde arquivo:
```commandline
python main.py
```
   - Após isso é só utilizar o programa e ser feliz.

 ##Rodando sistema de controle de empresa e serviço
   - Dentro da pasta deste arquivo, entre na pasta easy_gestor:
   - Abra o terminal no caminho da pasta citada acima.
   - digite os seguintes comandos:
```commandline
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
   - Agora é só acessar [http://localhost:8000/](http://localhost:8000/) e ser feliz
