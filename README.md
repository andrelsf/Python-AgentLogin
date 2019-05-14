# Agent Login

## Estrutura de diretórios

```
PyAgentLogin
    ├── data
    │   ├── cache
    │   ├── config.d
    │   └── log
    ├── pymain.py
    ├── README.md
    └── util
        └── entity
            └── pyconfigloader.py
```

##

[ OK ]: Proximo passo criar entidade user com os dados para ser coletados.
[ OK ]: Implementar o pymain para realizar a execução.
[ TODO ]: Implementar criar copia do arquivo original, mantelo seguro e fazer verificação de hash caso tenha divergencia no arquivo realizar a substituição do arquivo alterado para a copia original.(EventLoop)
[ OK ]: Persistencia de mensages de forma local para eventos como falha na comunicação com RMQ
[ TODO ]: RMQ Receiver de mensagens, persistencia, e notificação