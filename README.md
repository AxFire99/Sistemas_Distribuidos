# Sistemas_Distribuidos

1. Change django-deployment.yaml image (line 18) for your cluster (your_dockerhub_username/your_dockerhub_repo_name:latest)

2. docker build -t djangokubernetesproject .

3. docker run -p 80:8000 djangokubernetesproject 

4. localhost:notifications/send-notification/Paulo/ (It sends to one of the team member's particular email, it needs to be changed)

5. docker login

6. docker tag djangokubernetesproject:latest your_dockerhub_username/your_dockerhub_repo_name:latest

7. docker push your_dockerhub_username/your_dockerhub_repo_name:latest

8. kubectl delete deployment django-app

9. kubectl apply -f django-deployment.yaml

10. kubectl delete svc django

11. kubectl apply -f django-svc.yaml

12. kubectl get svc  ( 8000:IP [IP is what you want])

13. localhost:<Your IP>/notifications/send-notification/Paulo/ (It sends to one of the team member's particular email, it needs to be changed)
