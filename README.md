[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/eS3V9HRo)

Executei o seguinte bash, e deu certo!

## Portas necessarias

precisa-se das portas 5678 e 5679

## Instalando zeroc-ice

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

## Executando

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

- todo adapter tá com o ip da minha máquina servidor do aws, há comentado o host para localhost, para testes localmente, porém requer também um tratamento no início do arquivo servants.py (explicado no código).
- Além disso, a requeriments só vai funcionar localmente, e utilizando ambiente virtual.
