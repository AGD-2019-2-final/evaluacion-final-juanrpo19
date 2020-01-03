import sys
#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#

if __name__ == '__main__':

    curkey = None
    total = 0
    #letras='A,C'
    array=''
    nletra=''

    ##
    ## cada linea de texto recibida es una
    ## entrada clave \tabulador valor
    ##
    for line in sys.stdin:

        numero = line.split("\t")[0]
        val = line.split("\t")[1]
        letras= val
        #letras.sort()
        #maximo=max(letras)
        
        
        #sys.stdout.write("{}\t{}\n\n\n".format("A en posicion: ",pos))
        #sys.stdout.write("{}".format(letras))
        for i in range(len(letras)):
            #buscar=letras.find(letras[i][:1])
            #sys.stdout.write("\n{}".format(buscar))
            #sys.stdout.write("{}\t{}\t{}\n".format("Letra: ",letras[i][:1],buscar))
            if (array.find(letras[i][:1]) == -1) and letras[i][:1]!=',':
                nletra=letras[i][:1]
                #sys.stdout.write("{}\t{}\t{}\n".format("Letra: ",letras[i][:1],buscar))
                
                array=nletra + array 
    sys.stdout.write("{}".format(array))

