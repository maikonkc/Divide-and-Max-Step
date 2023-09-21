
x = [4,8,10,2]

def ls(array,a,b):
  if b-a==1 or b==a:
    print("fundo",array[b]-array[a],a,b)
    minNum = min(array[a],array[b])
    if array[a]==minNum: 
      return array[b]-array[a], array[a], a, array[b], b
    else: 
      return array[b]-array[a], array[b], b, array[a], a
    
  else:
    print("entrou em:",a,b)
    meio = (a+b)//2
    
    print("-----> entrando na esquerda")
    dEsq, menornumeroesq, idicedomenoresq, maiornumeroesq, indicedomaioresq = ls(array,a,meio)
    print("<----esquerda retornou:",dEsq, menornumeroesq, idicedomenoresq, maiornumeroesq, indicedomaioresq,"\n")

    print("-----> entrando na direita")
    dDir, menornumerodir, idicedomenordir, maiornumerodir, indicedomaiordir = ls(array,meio,b)
    print("<----direita retornou:",dDir, menornumerodir, idicedomenordir, maiornumerodir, indicedomaiordir,"\n")

    dtipo1 = maiornumerodir - menornumeroesq
    dtipo2 = maiornumeroesq - menornumerodir
    maiorpasso=max(dEsq,dDir,dtipo1)
    print("maior passo dos 3:",maiorpasso,dEsq,dDir,dtipo1,dtipo2)

    if maiorpasso==dtipo1:
      print("retornou o D com o maior à direita")
      return dtipo1, menornumeroesq, idicedomenoresq, maiornumerodir, indicedomaiordir
    if maiorpasso==dDir:
      print("retornou o DIREITO")
      return dDir, menornumerodir, idicedomenordir, maiornumerodir, indicedomaiordir
    if maiorpasso==dEsq:
      print("retornou o ESQUERDO")
      return dEsq, menornumeroesq, idicedomenoresq, maiornumeroesq, indicedomaioresq
    


print(ls(x,0, len(x)-1))