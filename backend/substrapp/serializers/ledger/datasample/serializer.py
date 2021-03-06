import json

from rest_framework import serializers

from substrapp import ledger


class LedgerDataSampleSerializer(serializers.Serializer):
    data_manager_keys = serializers.ListField(child=serializers.CharField(min_length=64, max_length=64),
                                              min_length=1)
    test_only = serializers.BooleanField()

    def create(self, validated_data):
        instances = self.initial_data.get('instances')
        data_manager_keys = validated_data.get('data_manager_keys')
        test_only = validated_data.get('test_only')

        args = {
            'hashes': [x.pk for x in instances],
            'dataManagerKeys': [x for x in data_manager_keys],
            'testOnly': json.dumps(test_only),
        }
        return ledger.create_datasamples(args, [x.pk for x in instances])
