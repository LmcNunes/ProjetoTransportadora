from uteis.globais import message
from uteis.globais import messageEmpresas

def verificarCondicao(altura,largura,peso):
  if altura >= 5 and altura <= 140 and peso > 0:
      if(largura >= 13 and largura <= 125):
          valorFreteN = (peso * 0.3) / 10
          valorFreteK = (peso * 0.2) / 10
          return messageEmpresas("Entrega Ninja", valorFreteN, 6, "Entrega Kabum",valorFreteK,4) 
          pass
      pass

  elif altura >= 10 and altura <= 200 and peso >0:
      if(largura >= 6 and largura <= 140):
          valorFrete = (peso * 0.3) / 10
          return message("Entrega Ninja ", valorFrete, 6)
          pass
      pass

  elif(altura >= 5 and altura <= 140 and peso >0):
      if(largura >= 13 and largura <= 125):
          valorFrete = (peso * 0.2) / 10
          return  message("Entrega Kabum", valorFrete, 4)
          pass
      pass

# pensando em um cenário de usuário retornei uma mensagem para não parecer um problema de tela, mesmo sabendo que é uma função de front-end
  else:
        return "[Não temos suporte para este produto ainda]"

def message(nomeEmpresa, valorFrete, dias):
     return (
     f"""
     Empresa: {nomeEmpresa}
     Valor do Frete R$: {valorFrete}
     Prazo em dias: {dias}
     """)


def messageEmpresas(nomeEmpresaPrimeira, precoPrimeira, diasPrimeira,nomeEmpresaSegunda,precoSegunda,diasSegunda):   
    return(
    f"""
    Empresa: {nomeEmpresaPrimeira}
    Valor do Frete R$: {precoPrimeira}
    Prazo em dias: {diasPrimeira}
    """
    "\n"
    f"""
    Empresa: {nomeEmpresaSegunda}
    Valor do Frete R$: {precoSegunda}
    Prazo em dias: {diasSegunda}
    """ )
    

    
