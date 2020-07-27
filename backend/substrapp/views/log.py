import os

from rest_framework import status, mixins
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.viewsets import GenericViewSet
from kubernetes import client, config


# from substrapp.ledger_utils import query_ledger, LedgerError
# from substrapp.views.filters_utils import filter_list


def get_k8s_client():
    # config.load_incluster_config()
    return client.CoreV1Api()


class LogViewSet(mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.ListModelMixin,
                 GenericViewSet):
    def list(self, request, *args, **kwargs):
        try:
            k8s_client = get_k8s_client()
            namespace = os.environ['CURRENT_ORG']
            # logs = k8s_client.read_namespaced_pod_log(name=f'{namespace}-worker', namespace=namespace)
            namespaces = k8s_client.list_namespace()
            return Response(namespaces, status=status.HTTP_200_OK)
        except KeyError:
            return Response('prout', status=status.HTTP_200_OK)
