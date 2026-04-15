[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/eS3V9HRo)

Executei o seguinte bash, e deu certo!

## Portas necessarias

precisa-se das portas 5678 e 5679

## Instalando zeroc-ice (aws)

Em ambos os bash, executar:

```bash
sudo chown ubuntu:ubuntu /mnt/efs/fs1
```

```bash
sudo apt update
```

```bash
sudo apt install python3
```

```bash
sudo apt install python3-venv
```

```bash
sudo apt install python3-pip
```

```bash
sudo apt install python3-zeroc-ice
```

```bash
sudo apt install python3-zeroc-ice zeroc-ice-compilers
```

```bash
sudo apt install python-is-python3
```

```bash
cd /mnt/efs/fs1/exercicio05-ice-ThiagoNascente/
```

```bash
slice2py Functions.ice
```

## Instalando zeroc-ice (local)

```bash
py -m venv venv
```
> Pra ti pode ser python, python3 ou py

```bash
pip install -r requirements.txt
```

```bash
./venv/bin/activate
```
ou
```bash
./venv/Scripts/activate
```
ou
```bash
source venv/bin/activate
```
ou
```bash
source venv/Scripts/activate
```
Para sair
```bash
deactivate
```

## Executando

[localmente -> todos os terminais devem estar na venv]
[Aws -> particularmente, não consegui usar venv lá]

- No primeiro Bash

```bash
py server.py
```

- No segundo Bash

```bash
py client.py
```

- No terceiro Bash

```bash
py server2.py
```

- No quarto Bash

```bash
py client2.py
```

## Observações

O código está preparado para executar primeiro remotamente, e quando falha tenta local, falhando novamente ele finaliza dizendo nao ter encontrado o servidor, ou servidor não está atendendo por aquilo (o processo servidor esperado não existe, ou porta liberada).
