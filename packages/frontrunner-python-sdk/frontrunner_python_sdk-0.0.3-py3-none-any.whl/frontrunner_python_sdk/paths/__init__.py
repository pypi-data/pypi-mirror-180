# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from frontrunner_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    ABBREVIATED_PEOPLE_ = "/abbreviated_people/"
    ABBREVIATED_PEOPLE_ID_ = "/abbreviated_people/{id}/"
    ABBREVIATED_USERS_ = "/abbreviated_users/"
    ABBREVIATED_USERS_ID_ = "/abbreviated_users/{id}/"
    API_TOKEN_ = "/api/token/"
    API_TOKEN_REFRESH_ = "/api/token/refresh/"
    FEED_ = "/feed/"
    FEED_ID_ = "/feed/{id}/"
    INTEGRATIONS_MAILCHIMP_ = "/integrations/mailchimp/"
    INTEGRATIONS_MAILCHIMP_ID_ = "/integrations/mailchimp/{id}/"
    INTEGRATIONS_PROMPT_ = "/integrations/prompt/"
    INTEGRATIONS_PROMPT_ID_ = "/integrations/prompt/{id}/"
    INTEGRATIONS_TWITTER_TWEETERS_ = "/integrations/twitter/tweeters/"
    INTEGRATIONS_TWITTER_TWEETERS_ID_ = "/integrations/twitter/tweeters/{id}/"
    INTEGRATIONS_TWITTER_TWEETS_ = "/integrations/twitter/tweets/"
    INTEGRATIONS_TWITTER_TWEETS_ID_ = "/integrations/twitter/tweets/{id}/"
    INTEGRATIONS_SETTINGS_ = "/integrations_settings/"
    INTEGRATIONS_SETTINGS_ID_ = "/integrations_settings/{id}/"
    PAGINATED_PEOPLE_ = "/paginated_people/"
    PEOPLE_ = "/people/"
    PEOPLE_ID_ = "/people/{id}/"
    TAGS_ = "/tags/"
    TAGS_ID_ = "/tags/{id}/"
    TASKS_ = "/tasks/"
    TASKS_ID_ = "/tasks/{id}/"
