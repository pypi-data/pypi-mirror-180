import typing_extensions

from frontrunner_python_sdk.paths import PathValues
from frontrunner_python_sdk.apis.paths.abbreviated_people_ import AbbreviatedPeople
from frontrunner_python_sdk.apis.paths.abbreviated_people_id_ import AbbreviatedPeopleId
from frontrunner_python_sdk.apis.paths.abbreviated_users_ import AbbreviatedUsers
from frontrunner_python_sdk.apis.paths.abbreviated_users_id_ import AbbreviatedUsersId
from frontrunner_python_sdk.apis.paths.api_token_ import ApiToken
from frontrunner_python_sdk.apis.paths.api_token_refresh_ import ApiTokenRefresh
from frontrunner_python_sdk.apis.paths.feed_ import Feed
from frontrunner_python_sdk.apis.paths.feed_id_ import FeedId
from frontrunner_python_sdk.apis.paths.integrations_mailchimp_ import IntegrationsMailchimp
from frontrunner_python_sdk.apis.paths.integrations_mailchimp_id_ import IntegrationsMailchimpId
from frontrunner_python_sdk.apis.paths.integrations_prompt_ import IntegrationsPrompt
from frontrunner_python_sdk.apis.paths.integrations_prompt_id_ import IntegrationsPromptId
from frontrunner_python_sdk.apis.paths.integrations_twitter_tweeters_ import IntegrationsTwitterTweeters
from frontrunner_python_sdk.apis.paths.integrations_twitter_tweeters_id_ import IntegrationsTwitterTweetersId
from frontrunner_python_sdk.apis.paths.integrations_twitter_tweets_ import IntegrationsTwitterTweets
from frontrunner_python_sdk.apis.paths.integrations_twitter_tweets_id_ import IntegrationsTwitterTweetsId
from frontrunner_python_sdk.apis.paths.integrations_settings_ import IntegrationsSettings
from frontrunner_python_sdk.apis.paths.integrations_settings_id_ import IntegrationsSettingsId
from frontrunner_python_sdk.apis.paths.paginated_people_ import PaginatedPeople
from frontrunner_python_sdk.apis.paths.people_ import People
from frontrunner_python_sdk.apis.paths.people_id_ import PeopleId
from frontrunner_python_sdk.apis.paths.tags_ import Tags
from frontrunner_python_sdk.apis.paths.tags_id_ import TagsId
from frontrunner_python_sdk.apis.paths.tasks_ import Tasks
from frontrunner_python_sdk.apis.paths.tasks_id_ import TasksId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ABBREVIATED_PEOPLE_: AbbreviatedPeople,
        PathValues.ABBREVIATED_PEOPLE_ID_: AbbreviatedPeopleId,
        PathValues.ABBREVIATED_USERS_: AbbreviatedUsers,
        PathValues.ABBREVIATED_USERS_ID_: AbbreviatedUsersId,
        PathValues.API_TOKEN_: ApiToken,
        PathValues.API_TOKEN_REFRESH_: ApiTokenRefresh,
        PathValues.FEED_: Feed,
        PathValues.FEED_ID_: FeedId,
        PathValues.INTEGRATIONS_MAILCHIMP_: IntegrationsMailchimp,
        PathValues.INTEGRATIONS_MAILCHIMP_ID_: IntegrationsMailchimpId,
        PathValues.INTEGRATIONS_PROMPT_: IntegrationsPrompt,
        PathValues.INTEGRATIONS_PROMPT_ID_: IntegrationsPromptId,
        PathValues.INTEGRATIONS_TWITTER_TWEETERS_: IntegrationsTwitterTweeters,
        PathValues.INTEGRATIONS_TWITTER_TWEETERS_ID_: IntegrationsTwitterTweetersId,
        PathValues.INTEGRATIONS_TWITTER_TWEETS_: IntegrationsTwitterTweets,
        PathValues.INTEGRATIONS_TWITTER_TWEETS_ID_: IntegrationsTwitterTweetsId,
        PathValues.INTEGRATIONS_SETTINGS_: IntegrationsSettings,
        PathValues.INTEGRATIONS_SETTINGS_ID_: IntegrationsSettingsId,
        PathValues.PAGINATED_PEOPLE_: PaginatedPeople,
        PathValues.PEOPLE_: People,
        PathValues.PEOPLE_ID_: PeopleId,
        PathValues.TAGS_: Tags,
        PathValues.TAGS_ID_: TagsId,
        PathValues.TASKS_: Tasks,
        PathValues.TASKS_ID_: TasksId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ABBREVIATED_PEOPLE_: AbbreviatedPeople,
        PathValues.ABBREVIATED_PEOPLE_ID_: AbbreviatedPeopleId,
        PathValues.ABBREVIATED_USERS_: AbbreviatedUsers,
        PathValues.ABBREVIATED_USERS_ID_: AbbreviatedUsersId,
        PathValues.API_TOKEN_: ApiToken,
        PathValues.API_TOKEN_REFRESH_: ApiTokenRefresh,
        PathValues.FEED_: Feed,
        PathValues.FEED_ID_: FeedId,
        PathValues.INTEGRATIONS_MAILCHIMP_: IntegrationsMailchimp,
        PathValues.INTEGRATIONS_MAILCHIMP_ID_: IntegrationsMailchimpId,
        PathValues.INTEGRATIONS_PROMPT_: IntegrationsPrompt,
        PathValues.INTEGRATIONS_PROMPT_ID_: IntegrationsPromptId,
        PathValues.INTEGRATIONS_TWITTER_TWEETERS_: IntegrationsTwitterTweeters,
        PathValues.INTEGRATIONS_TWITTER_TWEETERS_ID_: IntegrationsTwitterTweetersId,
        PathValues.INTEGRATIONS_TWITTER_TWEETS_: IntegrationsTwitterTweets,
        PathValues.INTEGRATIONS_TWITTER_TWEETS_ID_: IntegrationsTwitterTweetsId,
        PathValues.INTEGRATIONS_SETTINGS_: IntegrationsSettings,
        PathValues.INTEGRATIONS_SETTINGS_ID_: IntegrationsSettingsId,
        PathValues.PAGINATED_PEOPLE_: PaginatedPeople,
        PathValues.PEOPLE_: People,
        PathValues.PEOPLE_ID_: PeopleId,
        PathValues.TAGS_: Tags,
        PathValues.TAGS_ID_: TagsId,
        PathValues.TASKS_: Tasks,
        PathValues.TASKS_ID_: TasksId,
    }
)
