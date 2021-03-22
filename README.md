# Video uploader

![test](https://github.com/k0t3n/video_uploader/actions/workflows/main.yml/badge.svg)

Video uploader is Django-based application used for uploading, saving and transcoding video files. This app is part of
the Stepik interview.

## Setting up development environment

### System Requirements

* Python 3.9
* MariaDB 10.5
* MySQL client

### Installation for development

Virtual environment:

```bash
> virtualenv venv
```

Create .env file and configure params

```bash
> cp .env.example .env
```

Packages:

```bash
> pip install -r requirements.txt
```

## Deploy to k8s using Minikube

Install [Helm](https://helm.sh/) and make sure it's up to date

```bash
> helm version
version.BuildInfo{Version:"v3.5.3", GitCommit:"041ce5a2c17a58be0fcd5f5e16fb3e7e95fea622", GitTreeState:"dirty", GoVersion:"go1.16"}
```

Install [Minikube](https://minikube.sigs.k8s.io/docs/) and make sure is up to date and running

```bash
> minikube version
minikube version: v1.18.1
commit: 09ee84d530de4a92f00f1c5dbc34cead092b95bc

> minikube status
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured
timeToStop: Nonexistent
```

Configure `values.yaml` using example

```bash
> cd k8s/
> cp example.values.yaml values.yaml
```

and deploy

```bash
> helm upgrade --install --atomic --cleanup-on-fail --create-namespace --namespace video-uploader app . --debug --set Backend.Host=$(minikube ip)
```

Start tunnel for service backend

```bash
> minikube service backend -n video-uploader
|----------------|---------|-------------|---------------------------|
|   NAMESPACE    |  NAME   | TARGET PORT |            URL            |
|----------------|---------|-------------|---------------------------|
| video-uploader | backend |          80 | http://192.168.49.2:30290 |
|----------------|---------|-------------|---------------------------|
🏃  Starting tunnel for service backend.
|----------------|---------|-------------|------------------------|
|   NAMESPACE    |  NAME   | TARGET PORT |          URL           |
|----------------|---------|-------------|------------------------|
| video-uploader | backend |             | http://127.0.0.1:61997 |
|----------------|---------|-------------|------------------------|
🎉  Opening service video-uploader/backend in default browser...
```

You are gorgeous!

## Conclusions

All disclaimers, warnings and conclusions are
available [here](https://github.com/k0t3n/video_uploader/blob/main/CONCLUSION.md).