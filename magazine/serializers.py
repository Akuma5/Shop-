from rest_framework import serializers

from .models import Magazine, MagazineComment, MagazineImage


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MagazineImage
        fields = "__all__"


class MagazineSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Magazine
        fields = (
            "id", "title", "content", "image", "user", "price"
        )


class MagazineUpdateSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    photo = ImageSerializer(many=True)

    class Meta:
        model = Magazine
        fields = "__all__"


class MagazineCommentSerializer(serializers.ModelSerializer):
    """ Сериализатор коммента """

    class Meta:
        model = MagazineComment
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True},
            'product': {'read_only': True}
        }
