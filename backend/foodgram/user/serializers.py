from djoser.serializers import UserCreateSerializer, TokenCreateSerializer


class UserRegistrationSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ('email', 'username', 'first_name', 'last_name', 'password')


class TokenClaimSerializer(TokenCreateSerializer):
    class Meta:
        fields = ('email', 'password')
