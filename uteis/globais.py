def message(nomeEmpresa, preco, dias):   
    return(
    f"""
    Empresa: {nomeEmpresa}
    Valor do Frete R$: {preco}
    Prazo em dias: {dias}
    """)

def messageEmpresas(nomeEmpresaPrimeira, precoPrimeira, diasPrimeira, nomeEmpresaSegunda,precoSegunda,diasSegunda,):   
    return(
    f"""
    Empresa: {nomeEmpresaPrimeira}
    Valor do Frete R$: {precoPrimeira}
    Prazo em dias: {diasPrimeira}
    """
    f"""
    Empresa: {nomeEmpresaSegunda}
    Valor do Frete R$: {precoSegunda}
    Prazo em dias: {diasSegunda}
    """)
