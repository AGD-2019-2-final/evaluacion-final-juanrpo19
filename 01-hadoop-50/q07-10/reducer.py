import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == '__main__':

    curkey = None
    valor_mayor = 0
    fecha_mayor=''
    llave_mayor=''
    valor_menor = 0
    fecha_menor=''
    llave_menor=''
   

    ##
    ## cada linea de texto recibida es una
    ## entrada clave \tabulador valor
    ##
    for line in sys.stdin:

        key,val,date= line.split("\t")
        val=int(val)
        
        if curkey is None:
            llave_mayor=key
            fecha_mayor=date
            val=int(val)
            valor_mayor=val

        if key == llave_mayor:
            if valor_mayor <= val:
                llave_menor=llave_mayor
                fecha_menor=fecha_mayor
                valor_menor=valor_mayor

                llave_mayor=key
                fecha_mayor=date
                valor_mayor=val

                curkey=key

                sys.stdout.write("{}\t{}\t{}".format(llave_menor, fecha_menor ,valor_menor))

    sys.stdout.write("{}\t{}\t{}\n".format(llave_menor, fecha_menor ,valor_menor))
            