class SocialMediaUser:
    """This object is returned by all the socal media scrapers
    """

    def __init__(self, social_media_type, url, user_name=None, user_id=None):
        self.url = url
        self.type = social_media_type
        self.user_name = user_name
        self.user_id = user_id


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
    return SocialMediaUser("Twitter", url,"Test_User", 1234)


def instagram_data(url):
    """Collects all data of the user from instagram.

    Args:
        url [string]: url to the instagram profile of the user.

    Returns:
        [object]: Returns a SocialMediaUser object with the users instagram data.
    """
    return SocialMediaUser("Instagram", url,"Instagram_User", 9876)