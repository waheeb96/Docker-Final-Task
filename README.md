
# Docker-Final-Task

This is a Python Web APP using FLASK that:  
1- Presents the Current BitCoin Price (LIVE)  
2- Stores the price in a Redis Database  
3- Presents the Average Price for the last 10 minutes (LIVE) 

## How to run the project locally

Clone the project

```bash
  git clone https://github.com/waheeb96/Docker-Final-Task.git
```

Step in the project directory

```bash
  cd Docker-Final-Task
```

Build and run the project

```bash
  docker-compose up -d
```

Open the project on your browser

```bash
  http://local host:5000/
```
![docker-2](https://user-images.githubusercontent.com/72220299/179369105-dfc8bbe8-c3a4-40d6-ae59-4e90a3b2d6c2.PNG)

## Jenkins 
Creates and pushes the generated Web application Docker image to Docker Hub  
![docker-3](https://user-images.githubusercontent.com/72220299/179369097-2f9d3510-1f43-4fc5-8dd3-2c0224672cad.PNG)


