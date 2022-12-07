# Projeto Computação Larga Escala
Projeto para trabalho computação larga em escala com tecnologia micro serviços e serveless


* ### Execução dos microsserviços

Para execução dos microsserviços, basta entrar na pasta ```microservices``` e executar o comando 
```
docker-compose up
```

Após a execução do comando, irá ser possivel entrar na documentação e realizar as chamadas via API Rest utilizando as seguintes URL's

* API de Produto

 http://localhost:8080/api/v1/product/docs

* API de Filmes

 http://localhost:8080/api/v1/movies/docs



* ### Execução do serverless

Para execução do serverless, basta entrar na pasta ```serverless``` e executar o comando 
```
docker-compose up
```

Após a execução do comando, fazer as chamadas das funções utilizando os comandos abaixo para cada função

* API Conversão de Distância
```
curl -XPOST "http://localhost:9002/2015-03-31/functions/function/invocations" -d '{"miles":54}'
```

* API Conversão de Peso
```
curl -XPOST "http://localhost:9001/2015-03-31/functions/function/invocations" -d '{"data":140}' 
```

* API Conversão de Temperatura
```
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"temp":23}'   
```

* API Contagem de palavras
```
curl -XPOST "http://localhost:9003/2015-03-31/functions/function/invocations" -d '{"data":"Brasil ganha copa do mundo e se torna Hexa Campeão"}'
```




  


