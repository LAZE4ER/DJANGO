from rest_framework import serializers
from .models import Bug
import logging

logger = logging.getLogger('bugs')

class BugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bug
        fields = '__all__'
    def validate_severity(self, value):
        if not (1 <= value <= 5):
            logger.warning(f"Validation failed: Invalid severity {value}")
            raise serializers.ValidationError("Severity має бути від 1 до 5.")
        return value

    def validate(self, data):
        status = data.get('status')
       
        if self.instance is None and status == 'Resolved':
            logger.warning("Validation failed: Attempt to create bug with 'Resolved' status")
            raise serializers.ValidationError("Новий баг не може бути одразу вирішеним.")
        return data
    




