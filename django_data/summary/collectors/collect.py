import twitter
from django.conf import settings


class SocialMediaUser:
    """This object is returned by all the socal media scrapers"""

    def __init__(
        self,
        social_media_type: str,
        url: str,
        user_name: str = None,
        user_id: str = None,
        followers: int = None,
        following: int = None,
        profile_foto: str = None,
        creation: str = None,
    ) -> None:
        self.url = url
        self.type = social_media_type
        self.user_name = user_name
        self.user_id = user_id
        self.followers = followers
        self.following = following
        self.profile_foto = profile_foto
        self.creation = creation

    def __str__(self):
        return f"<SocialMediaUser url={self.url} type={self.type} name={self.user_name} id={self.user_id} >"


def getAllData(urls):
    """Gets all the data from the diffrent social media scrapers.
    Like this new scrapers can be intergated easily.

    Args:
        urls [dict]: Dict containing plattforms as keys and profile url as values

    Returns:
        [list]: List of SocialMediaUser objects.
    """
    return [twitter_data(urls["twitter"])]


def twitter_data(url):
    """Collects all data of the user from twitter.

    Args:
        url [string]: url to the twitter profile of the user.

    Returns:
        [object]: Returns a SocialMediaUser object with the users twitter data.
    """
    api = twitter.Api(
        consumer_key=settings.TWITTER_CONSUMER_KEY,
        consumer_secret=settings.TWITTER_CONSUMER_SECRET,
        access_token_key=settings.TWITTER_ACCESS_TOKEN_KEY,
        access_token_secret=settings.TWITTER_ACCESS_TOKEN_SECRET,
    )

    user_screen_name = url.split("/")[-1]
    if not user_screen_name:
        return SocialMediaUser("Twitter", url, "Not found", "Not found")
    user = api.GetUser(screen_name=user_screen_name)
    creation = user.created_at
    if creation:
        creation = user.created_at.split("+")[0]
    return SocialMediaUser(
        "Twitter",
        url,
        user_name=user.name,
        user_id=user.id,
        followers=user.followers_count,
        following=user.friends_count,
        profile_foto=user.profile_image_url,
        creation=creation,
    )
