from rest_framework import serializers

from Main.models import Block





class RouterRegisterSerializer(serializers.ModelSerializer):
    block_id = serializers.IntegerField()

    def save(self, **kwargs):
        block = Block.objects.get(block_id=self.block_id)
        block.tag = 'router'
        block.save()
        return block
