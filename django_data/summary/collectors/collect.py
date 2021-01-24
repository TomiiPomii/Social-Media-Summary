from django.conf import settings
import twitter


class SocialMediaUser:
    """This object is returned by all the socal media scrapers
    """

    def __init__(self, social_media_type, url, user_name=None, user_id=None):
        self.url = url
        self.type = social_media_type
        self.user_name = user_name
        self.user_id = user_id

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
    return [twitter_data(urls["twitter"]), instagram_data(urls["instagram"])]


def twitter_data(url):
    """Collects all data of the user from twitter.

    Args:
        url [string]: url to the twitter profile of the user.

    Returns:
        [object]: Returns a SocialMediaUser object with the users twitter data.
    """
    api = twitter.Api(consumer_key=settings.TWITTER_CONSUMER_KEY,
                      consumer_secret=settings.TWITTER_CONSUMER_SECRET,
                      access_token_key=settings.TWITTER_ACCESS_TOKEN_KEY,
                      access_token_secret=settings.TWITTER_ACCESS_TOKEN_SECRET)

    user_screen_name = url.split("/")[-1]
    user = api.GetUser(screen_name=user_screen_name)
    print("Name:", user.name)
    print("Number of followers:", user.followers_count)
    print("Number of friends:", user.friends_count)
    return SocialMediaUser("Twitter", url, user.name, user.id)


def instagram_data(url):
    """Collects all data of the user from instagram.

    Args:
        url [string]: url to the instagram profile of the user.

    Returns:
        [object]: Returns a SocialMediaUser object with the users instagram data.
    """
    return SocialMediaUser("Instagram", url, "Instagram_User", 9876)
