from rest_framework.serializers import ModelSerializer
from ..models import Post
from rest_framework.serializers import HyperlinkedIdentityField, SerializerMethodField

detail_url = HyperlinkedIdentityField(
    view_name='api:detail',
    lookup_field='slug'
)

class PostCreateEditeSerialzier(ModelSerializer):
    class Meta:
        model = Post
        exclude = ['slug','user']

class PostDeleteDetailSerialzier(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class PostListSerializer(ModelSerializer):
    url = detail_url
    user = SerializerMethodField()
    image = SerializerMethodField()
    html = SerializerMethodField()

    def get_html(self,obj):
        return obj.get_markdown()

    def get_user(self,obj):
        return str(obj.user.username)

    def get_image(self,obj):
        try:
            image = obj.image.path
        except:
            image = None
        return image

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'user',
            'url',
            'image',
            'html'
        ]



