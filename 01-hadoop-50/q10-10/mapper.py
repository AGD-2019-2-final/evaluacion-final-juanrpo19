import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":
    for line in sys.stdin:
        numero = line.split('\t')[0]
        letras = line.split('\t')[1]
        #letras = letras.split('\n')[0]
        #letras = letras.split('\n')[0]

        #letras=str(letras)
        #lon=len(letras)
        numero=numero.zfill(3)
        sys.stdout.write("{}\t{}".format(numero,letras))
    sys.stdout.write('\n')