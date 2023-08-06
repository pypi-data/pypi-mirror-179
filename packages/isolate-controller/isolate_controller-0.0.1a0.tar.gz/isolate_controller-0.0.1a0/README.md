# fal-isolate-cloud

## Regenerating gRPC definitions

- Ensure you are on Python 3.9 or higher
- From the root directory execute the following commands:

```sh
$ pip install grpcio_tools mypy-protobuf refactor
$ python tools/regen_grpc.py src/isolate_controller/definitions/controller.proto
```

## Building the images

- From the root directory

```sh
$ docker build -f infra/worker/Dockerfile -t isolate-cloud-worker .
$ docker build -f infra/controller/Dockerfile -t isolate-cloud-controller .
```

## Testing the server (locally)

- Assuming you built the image `isolate-cloud-worker`, try the following setup:

```sh
$ docker run --rm -e CONTROLLER_KEY=local_secret -p 50001:50001 isolate-cloud-worker
$ ISOLATE_TEST_MODE=1 python -m isolate_controller.server
# CHANGE THE IP FIRST
$ python test_script.py
```

## Setting kubectl with the GCP cluster

- Install the GKE plugin if you don't have it
- Get the clusters list

```sh
$ gcloud components install gke-gcloud-auth-plugin
$ gcloud container clusters get-credentials <cluster-name> --zone <your-zone>
$ kubectl get pods -A
# should print kube-system pods
```

## Deploying

### Deploying the worker

```sh
$ gcloud builds submit --config=infra/worker/cloudbuild.yml .
```

### Deploying the controller

```sh
$ export PROJECT_ID=$(gcloud config list --format 'value(core.project)' 2>/dev/null)
$ gcloud builds submit --config=infra/controller/cloudbuild.yml .
$ export IMAGE_SHA=$(python tools/update_images.py)
$ envsubst < infra/controller/controller.yml | kubectl apply -f -
# Run this just once to expose the service:
$ kubectl expose deployment fal-isolate-controller --type=LoadBalancer --name=load-balancer
```

### Connect redis

Make sure to do this when you are setting up the first time

https://cloud.google.com/memorystore/docs/redis/connect-redis-instance#connecting-cluster

```sh
$ gcloud redis instances list --region=us-central1
# Take note of the HOST value
$ export REDISHOST_IP=...
```

```sh
$ export REDISHOST_IP=...
$ git clone https://github.com/bowei/k8s-custom-iptables.git
$ cd k8s-custom-iptables/
$ TARGETS=${REDISHOST_IP} ./install.sh
```

```sh
$ export REDISHOST_IP=...
$ kubectl create configmap redishost --from-literal=REDISHOST=${REDISHOST_IP}
```

### Setup NFS cache

Make sure to do this when you are setting up the first time

```sh
$ gcloud filestore instances list
# Take note of the IP_ADDRESS
$ export NFS_SERVER_IP=...
```

```sh
$ export NFS_SERVER_IP=...
$ envsubst < infra/fileserver/nfs-server.yml | kubectl apply -f -
$ kubectl apply -f infra/fileserver/claim.yml
```

### Bind Google Service Account to Kubernetes Service Account

Make sure to do this when you are setting up the first time

This is necessary to [connect Postgres](#connect-postgres)

```sh
$ kubectl annotate serviceaccount default iam.gke.io/gcp-service-account=gke-service-account@${PROJECT_ID}.iam.gserviceaccount.com
```

### Connect Postgres

Make sure to do this when you are setting up the first time

```sh
# xargs to remove extra quotes
$ cd fal_terraform/environments/<environment>
$ export SQITCH_PASSWORD=$(terraform output isolate_cloud_sql_user_server_password | xargs)
$ kubectl create secret generic sqlaccess \
    --from-literal=SQL_DBNAME=users \
    --from-literal=SQL_USER=gke_service \
    --from-literal=SQL_PASSWORD=$SQITCH_PASSWORD
```

#### Apply Postgres migrations

Download CLI tool [sqitch](https://sqitch.org/download/)

Download the [Cloud SQL Auth Proxy](https://cloud.google.com/sql/docs/mysql/connect-admin-proxy#install)

Run the `cloud_sql_proxy` binary to connect to the Cloud SQL instance as a local connection:

```sh
# Notice the PORT is 5433 to differ from the default 5432 of Postgres
$ ./cloud_sql_proxy -instances=${PROJECT_ID}:us-central1:isolate-cloud=tcp:0.0.0.0:5433
```

In another shell, run the migrations

```sh
# xargs to remove extra quotes
$ export SQITCH_PASSWORD=$(terraform output isolate_cloud_sql_user_server_password | xargs)
$ cd fal-isolate-cloud/db
$ sqitch deploy --verify cloud-proxy
#   Adding registry tables to cloud-proxy
#   Deploying changes to cloud-proxy
#     + create_table_jobs .. ok
```

And close (`CTRL-C`) the close_sql_proxy process.
