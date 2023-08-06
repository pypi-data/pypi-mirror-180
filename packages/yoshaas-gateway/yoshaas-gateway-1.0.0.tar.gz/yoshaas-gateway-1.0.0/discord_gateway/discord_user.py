from types import SimpleNamespace

from requests import Response

from discord_gateway.api import HttpClient
from discord_gateway.discord_objects import DiscordMessage


class UserMessage(DiscordMessage):

    def __init__(self, data: object, client: HttpClient):
        try:  # Try obtaining data
            super().__init__(data, client)
        except AttributeError:
            pass
        self.author = DiscordUser(self.author, self.__token)


class DiscordUser:

    def __init__(self, user, client: HttpClient):
        self.id = user.get("id")
        self.name = user.get("username")
        self.discriminator = user.get("discriminator")
        self.__token = client.get_token()
        self.api = client

    async def send(self, *content) -> UserMessage:
        """
        Send dm to user\n
        :param content: :class:`list[str]`
            The content to send
        :return: :class:`UserMessage`
            The message
        """
        headers = {
            'Authorization': self.api.get_auth(),
            'Content-Type': 'application/json'
        }
        user_id = self.api.requests(method='POST', path=f'/users/@me/channels', json={"recipients": [self.id]},
                                    headers=headers).get('id')
        try:
            if content:
                r = self.api.requests(method='POST', path=f'/channels/{user_id}/messages', data={'content': content})
                return UserMessage(SimpleNamespace(**r), client=self.api)
        except Exception as e:
            raise f'Missing permissions: {e}'


class DiscordMember(DiscordUser):

    def __init__(self, member, user, guild_id, client: HttpClient):
        super().__init__(user, client)
        self.guild_id = guild_id
        self.roles = member.get("roles", [])
        self.nick = member.get("nick", "")
        self.token = client.get_token()

    def add_role(self, role_id: str) -> Response | dict:
        """
        Add a role to member\n
        :param role_id: :class:`str`
            The role id
        :return: :class:`Union[Response, dict]`
            The added role
        """
        return self.api.requests(method='PUT', path=f'/guilds/{self.guild_id}/members/{self.id}/roles/{role_id}')

    def remove_role(self, role_id: str) -> None:
        """
        Remove a role from member\n
        :param role_id: :class:`str`
            The role id
        """
        self.api.requests(method='DELETE', path=f'/guilds/{self.guild_id}/members/{self.id}/roles/{role_id}')

    async def kick(self) -> None:
        """
        Kicks the member\n
        """
        self.api.requests(method='DELETE', path=f'/guilds/{self.id}/members/{self.id}')

    async def ban(self, delete_message_seconds: int = 3600) -> None:
        """
        Bans the member\n
        :param delete_message_seconds: :class:`int`
            Delete message seconds, delete all the messages from the user
            in the given time frame
        """
        payload = {
            "delete_message_seconds": delete_message_seconds
        }
        self.api.requests(method='PUT', path=f'/guilds/{self.id}/bans/{self.id}', data=payload)
