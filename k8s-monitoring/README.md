# Kubernetes Monitoring Setup

### Check Running Pods

```bash
kubectl get pods -n monitoring

NAME                                  READY   STATUS    RESTARTS      AGE
alertmanager-78cc5c477d-t6rtf         1/1     Running   2 (16m ago)   13d
grafana-7d7874b9c9-s2d6m              1/1     Running   2 (16m ago)   13d
kube-state-metrics-78cb978b56-76hd7   1/1     Running   0             3m18s
prometheus-588766977f-sdhg7           1/1     Running   2 (16m ago)   13d
test-app-f984fd5f9-lbgf6              1/1     Running   2 (16m ago)   13d
test-app-f984fd5f9-nhsjc              1/1     Running   2 (16m ago)   13d
```
All pods are currently in the Running state.

### Check Services

```bash
kubectl get svc -n monitoring
Output
NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
alertmanager         ClusterIP   10.96.210.142   <none>        9093/TCP         13d
grafana              NodePort    10.96.154.76    <none>        3000:30000/TCP   13d
kube-state-metrics   ClusterIP   10.96.166.73    <none>        8080/TCP         3m30s
prometheus           ClusterIP   10.96.201.4     <none>        9090/TCP         13d
```

### Verify Kube State Metrics

Since kube-state-metrics is exposed as a ClusterIP service, it can be accessed from inside the Kubernetes cluster.

- Enter the Kind Control Plane - `docker exec -it kind-control-plane bash`

- Access Kube State Metrics - `curl 10.96.166.73:8080/metrics`
