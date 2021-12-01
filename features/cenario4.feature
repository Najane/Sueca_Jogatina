# language: pt
Funcionalidade: Veridicar a versão do App


    Cenário: Verificar versão do App
        Dado que esteja na pagina de Preferências
        Quando arrasto a tela até o fim da página
        E vejo a versão do App
        Então valido se a versão é "1.5.4"