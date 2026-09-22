from rest_framework import serializers
from .models import Mission, HOSTEL_CHOICES, DIFFICULTY_CHOICES, STATUS_CHOICES

class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = '__all__'

    def validate_points(self, value):
        if value <= 0:
            raise serializers.ValidationError("Points must be a positive integer.")
        return value

    def validate(self, attrs):
        status = attrs.get('status', getattr(self.instance, 'status', None))
        solver_handle = attrs.get('solver_handle', getattr(self.instance, 'solver_handle', None))

        if status == 'cracked' and not solver_handle:
            raise serializers.ValidationError({
                "solver_handle": "A solver handle must be provided if the mission status is 'cracked'."
            })
        return attrs