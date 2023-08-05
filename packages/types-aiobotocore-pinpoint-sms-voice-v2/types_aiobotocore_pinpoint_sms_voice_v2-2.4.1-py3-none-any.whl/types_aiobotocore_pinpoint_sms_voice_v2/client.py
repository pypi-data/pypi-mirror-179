"""
Type annotations for pinpoint-sms-voice-v2 service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_pinpoint_sms_voice_v2.client import PinpointSMSVoiceV2Client

    session = get_session()
    async with session.create_client("pinpoint-sms-voice-v2") as client:
        client: PinpointSMSVoiceV2Client
    ```
"""
import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import (
    DestinationCountryParameterKeyType,
    EventTypeType,
    KeywordActionType,
    MessageTypeType,
    NumberCapabilityType,
    RequestableNumberTypeType,
    VoiceIdType,
    VoiceMessageBodyTextTypeType,
)
from .paginator import (
    DescribeAccountAttributesPaginator,
    DescribeAccountLimitsPaginator,
    DescribeConfigurationSetsPaginator,
    DescribeKeywordsPaginator,
    DescribeOptedOutNumbersPaginator,
    DescribeOptOutListsPaginator,
    DescribePhoneNumbersPaginator,
    DescribePoolsPaginator,
    DescribeSenderIdsPaginator,
    DescribeSpendLimitsPaginator,
    ListPoolOriginationIdentitiesPaginator,
)
from .type_defs import (
    AssociateOriginationIdentityResultTypeDef,
    CloudWatchLogsDestinationTypeDef,
    ConfigurationSetFilterTypeDef,
    CreateConfigurationSetResultTypeDef,
    CreateEventDestinationResultTypeDef,
    CreateOptOutListResultTypeDef,
    CreatePoolResultTypeDef,
    DeleteConfigurationSetResultTypeDef,
    DeleteDefaultMessageTypeResultTypeDef,
    DeleteDefaultSenderIdResultTypeDef,
    DeleteEventDestinationResultTypeDef,
    DeleteKeywordResultTypeDef,
    DeleteOptedOutNumberResultTypeDef,
    DeleteOptOutListResultTypeDef,
    DeletePoolResultTypeDef,
    DeleteTextMessageSpendLimitOverrideResultTypeDef,
    DeleteVoiceMessageSpendLimitOverrideResultTypeDef,
    DescribeAccountAttributesResultTypeDef,
    DescribeAccountLimitsResultTypeDef,
    DescribeConfigurationSetsResultTypeDef,
    DescribeKeywordsResultTypeDef,
    DescribeOptedOutNumbersResultTypeDef,
    DescribeOptOutListsResultTypeDef,
    DescribePhoneNumbersResultTypeDef,
    DescribePoolsResultTypeDef,
    DescribeSenderIdsResultTypeDef,
    DescribeSpendLimitsResultTypeDef,
    DisassociateOriginationIdentityResultTypeDef,
    KeywordFilterTypeDef,
    KinesisFirehoseDestinationTypeDef,
    ListPoolOriginationIdentitiesResultTypeDef,
    ListTagsForResourceResultTypeDef,
    OptedOutFilterTypeDef,
    PhoneNumberFilterTypeDef,
    PoolFilterTypeDef,
    PoolOriginationIdentitiesFilterTypeDef,
    PutKeywordResultTypeDef,
    PutOptedOutNumberResultTypeDef,
    ReleasePhoneNumberResultTypeDef,
    RequestPhoneNumberResultTypeDef,
    SenderIdAndCountryTypeDef,
    SenderIdFilterTypeDef,
    SendTextMessageResultTypeDef,
    SendVoiceMessageResultTypeDef,
    SetDefaultMessageTypeResultTypeDef,
    SetDefaultSenderIdResultTypeDef,
    SetTextMessageSpendLimitOverrideResultTypeDef,
    SetVoiceMessageSpendLimitOverrideResultTypeDef,
    SnsDestinationTypeDef,
    TagTypeDef,
    UpdateEventDestinationResultTypeDef,
    UpdatePhoneNumberResultTypeDef,
    UpdatePoolResultTypeDef,
)

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("PinpointSMSVoiceV2Client",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class PinpointSMSVoiceV2Client(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        PinpointSMSVoiceV2Client exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#exceptions)
        """

    async def associate_origination_identity(
        self, *, PoolId: str, OriginationIdentity: str, IsoCountryCode: str, ClientToken: str = ...
    ) -> AssociateOriginationIdentityResultTypeDef:
        """
        Associates the specified origination identity with a pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.associate_origination_identity)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#associate_origination_identity)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#close)
        """

    async def create_configuration_set(
        self, *, ConfigurationSetName: str, Tags: Sequence[TagTypeDef] = ..., ClientToken: str = ...
    ) -> CreateConfigurationSetResultTypeDef:
        """
        Creates a new configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.create_configuration_set)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#create_configuration_set)
        """

    async def create_event_destination(
        self,
        *,
        ConfigurationSetName: str,
        EventDestinationName: str,
        MatchingEventTypes: Sequence[EventTypeType],
        CloudWatchLogsDestination: CloudWatchLogsDestinationTypeDef = ...,
        KinesisFirehoseDestination: KinesisFirehoseDestinationTypeDef = ...,
        SnsDestination: SnsDestinationTypeDef = ...,
        ClientToken: str = ...
    ) -> CreateEventDestinationResultTypeDef:
        """
        Creates a new event destination in a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.create_event_destination)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#create_event_destination)
        """

    async def create_opt_out_list(
        self, *, OptOutListName: str, Tags: Sequence[TagTypeDef] = ..., ClientToken: str = ...
    ) -> CreateOptOutListResultTypeDef:
        """
        Creates a new opt-out list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.create_opt_out_list)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#create_opt_out_list)
        """

    async def create_pool(
        self,
        *,
        OriginationIdentity: str,
        IsoCountryCode: str,
        MessageType: MessageTypeType,
        DeletionProtectionEnabled: bool = ...,
        Tags: Sequence[TagTypeDef] = ...,
        ClientToken: str = ...
    ) -> CreatePoolResultTypeDef:
        """
        Creates a new pool and associates the specified origination identity to the
        pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.create_pool)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#create_pool)
        """

    async def delete_configuration_set(
        self, *, ConfigurationSetName: str
    ) -> DeleteConfigurationSetResultTypeDef:
        """
        Deletes an existing configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_configuration_set)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#delete_configuration_set)
        """

    async def delete_default_message_type(
        self, *, ConfigurationSetName: str
    ) -> DeleteDefaultMessageTypeResultTypeDef:
        """
        Deletes an existing default message type on a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_default_message_type)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#delete_default_message_type)
        """

    async def delete_default_sender_id(
        self, *, ConfigurationSetName: str
    ) -> DeleteDefaultSenderIdResultTypeDef:
        """
        Deletes an existing default sender ID on a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_default_sender_id)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#delete_default_sender_id)
        """

    async def delete_event_destination(
        self, *, ConfigurationSetName: str, EventDestinationName: str
    ) -> DeleteEventDestinationResultTypeDef:
        """
        Deletes an existing event destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_event_destination)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#delete_event_destination)
        """

    async def delete_keyword(
        self, *, OriginationIdentity: str, Keyword: str
    ) -> DeleteKeywordResultTypeDef:
        """
        Deletes an existing keyword from an origination phone number or pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_keyword)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#delete_keyword)
        """

    async def delete_opt_out_list(self, *, OptOutListName: str) -> DeleteOptOutListResultTypeDef:
        """
        Deletes an existing opt-out list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_opt_out_list)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#delete_opt_out_list)
        """

    async def delete_opted_out_number(
        self, *, OptOutListName: str, OptedOutNumber: str
    ) -> DeleteOptedOutNumberResultTypeDef:
        """
        Deletes an existing opted out destination phone number from the specified opt-
        out list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_opted_out_number)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#delete_opted_out_number)
        """

    async def delete_pool(self, *, PoolId: str) -> DeletePoolResultTypeDef:
        """
        Deletes an existing pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_pool)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#delete_pool)
        """

    async def delete_text_message_spend_limit_override(
        self,
    ) -> DeleteTextMessageSpendLimitOverrideResultTypeDef:
        """
        Deletes an account-level monthly spending limit override for sending text
        messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_text_message_spend_limit_override)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#delete_text_message_spend_limit_override)
        """

    async def delete_voice_message_spend_limit_override(
        self,
    ) -> DeleteVoiceMessageSpendLimitOverrideResultTypeDef:
        """
        Deletes an account level monthly spend limit override for sending voice
        messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_voice_message_spend_limit_override)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#delete_voice_message_spend_limit_override)
        """

    async def describe_account_attributes(
        self, *, NextToken: str = ..., MaxResults: int = ...
    ) -> DescribeAccountAttributesResultTypeDef:
        """
        Describes attributes of your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_account_attributes)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#describe_account_attributes)
        """

    async def describe_account_limits(
        self, *, NextToken: str = ..., MaxResults: int = ...
    ) -> DescribeAccountLimitsResultTypeDef:
        """
        Describes the current Amazon Pinpoint SMS Voice V2 resource quotas for your
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_account_limits)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#describe_account_limits)
        """

    async def describe_configuration_sets(
        self,
        *,
        ConfigurationSetNames: Sequence[str] = ...,
        Filters: Sequence[ConfigurationSetFilterTypeDef] = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> DescribeConfigurationSetsResultTypeDef:
        """
        Describes the specified configuration sets or all in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_configuration_sets)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#describe_configuration_sets)
        """

    async def describe_keywords(
        self,
        *,
        OriginationIdentity: str,
        Keywords: Sequence[str] = ...,
        Filters: Sequence[KeywordFilterTypeDef] = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> DescribeKeywordsResultTypeDef:
        """
        Describes the specified keywords or all keywords on your origination phone
        number or pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_keywords)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#describe_keywords)
        """

    async def describe_opt_out_lists(
        self, *, OptOutListNames: Sequence[str] = ..., NextToken: str = ..., MaxResults: int = ...
    ) -> DescribeOptOutListsResultTypeDef:
        """
        Describes the specified opt-out list or all opt-out lists in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_opt_out_lists)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#describe_opt_out_lists)
        """

    async def describe_opted_out_numbers(
        self,
        *,
        OptOutListName: str,
        OptedOutNumbers: Sequence[str] = ...,
        Filters: Sequence[OptedOutFilterTypeDef] = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> DescribeOptedOutNumbersResultTypeDef:
        """
        Describes the specified opted out destination numbers or all opted out
        destination numbers in an opt-out list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_opted_out_numbers)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#describe_opted_out_numbers)
        """

    async def describe_phone_numbers(
        self,
        *,
        PhoneNumberIds: Sequence[str] = ...,
        Filters: Sequence[PhoneNumberFilterTypeDef] = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> DescribePhoneNumbersResultTypeDef:
        """
        Describes the specified origination phone number, or all the phone numbers in
        your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_phone_numbers)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#describe_phone_numbers)
        """

    async def describe_pools(
        self,
        *,
        PoolIds: Sequence[str] = ...,
        Filters: Sequence[PoolFilterTypeDef] = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> DescribePoolsResultTypeDef:
        """
        Retrieves the specified pools or all pools associated with your Amazon Web
        Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_pools)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#describe_pools)
        """

    async def describe_sender_ids(
        self,
        *,
        SenderIds: Sequence[SenderIdAndCountryTypeDef] = ...,
        Filters: Sequence[SenderIdFilterTypeDef] = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> DescribeSenderIdsResultTypeDef:
        """
        Describes the specified SenderIds or all SenderIds associated with your Amazon
        Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_sender_ids)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#describe_sender_ids)
        """

    async def describe_spend_limits(
        self, *, NextToken: str = ..., MaxResults: int = ...
    ) -> DescribeSpendLimitsResultTypeDef:
        """
        Describes the current Amazon Pinpoint monthly spend limits for sending voice and
        text messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_spend_limits)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#describe_spend_limits)
        """

    async def disassociate_origination_identity(
        self, *, PoolId: str, OriginationIdentity: str, IsoCountryCode: str, ClientToken: str = ...
    ) -> DisassociateOriginationIdentityResultTypeDef:
        """
        Removes the specified origination identity from an existing pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.disassociate_origination_identity)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#disassociate_origination_identity)
        """

    async def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#generate_presigned_url)
        """

    async def list_pool_origination_identities(
        self,
        *,
        PoolId: str,
        Filters: Sequence[PoolOriginationIdentitiesFilterTypeDef] = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> ListPoolOriginationIdentitiesResultTypeDef:
        """
        Lists all associated origination identities in your pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.list_pool_origination_identities)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#list_pool_origination_identities)
        """

    async def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResultTypeDef:
        """
        List all tags associated with a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#list_tags_for_resource)
        """

    async def put_keyword(
        self,
        *,
        OriginationIdentity: str,
        Keyword: str,
        KeywordMessage: str,
        KeywordAction: KeywordActionType = ...
    ) -> PutKeywordResultTypeDef:
        """
        Creates or updates a keyword configuration on an origination phone number or
        pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.put_keyword)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#put_keyword)
        """

    async def put_opted_out_number(
        self, *, OptOutListName: str, OptedOutNumber: str
    ) -> PutOptedOutNumberResultTypeDef:
        """
        Creates an opted out destination phone number in the opt-out list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.put_opted_out_number)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#put_opted_out_number)
        """

    async def release_phone_number(self, *, PhoneNumberId: str) -> ReleasePhoneNumberResultTypeDef:
        """
        Releases an existing origination phone number in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.release_phone_number)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#release_phone_number)
        """

    async def request_phone_number(
        self,
        *,
        IsoCountryCode: str,
        MessageType: MessageTypeType,
        NumberCapabilities: Sequence[NumberCapabilityType],
        NumberType: RequestableNumberTypeType,
        OptOutListName: str = ...,
        PoolId: str = ...,
        RegistrationId: str = ...,
        DeletionProtectionEnabled: bool = ...,
        Tags: Sequence[TagTypeDef] = ...,
        ClientToken: str = ...
    ) -> RequestPhoneNumberResultTypeDef:
        """
        Request an origination phone number for use in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.request_phone_number)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#request_phone_number)
        """

    async def send_text_message(
        self,
        *,
        DestinationPhoneNumber: str,
        OriginationIdentity: str = ...,
        MessageBody: str = ...,
        MessageType: MessageTypeType = ...,
        Keyword: str = ...,
        ConfigurationSetName: str = ...,
        MaxPrice: str = ...,
        TimeToLive: int = ...,
        Context: Mapping[str, str] = ...,
        DestinationCountryParameters: Mapping[DestinationCountryParameterKeyType, str] = ...,
        DryRun: bool = ...
    ) -> SendTextMessageResultTypeDef:
        """
        Creates a new text message and sends it to a recipient's phone number.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.send_text_message)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#send_text_message)
        """

    async def send_voice_message(
        self,
        *,
        DestinationPhoneNumber: str,
        OriginationIdentity: str,
        MessageBody: str = ...,
        MessageBodyTextType: VoiceMessageBodyTextTypeType = ...,
        VoiceId: VoiceIdType = ...,
        ConfigurationSetName: str = ...,
        MaxPricePerMinute: str = ...,
        TimeToLive: int = ...,
        Context: Mapping[str, str] = ...,
        DryRun: bool = ...
    ) -> SendVoiceMessageResultTypeDef:
        """
        Allows you to send a request that sends a text message through Amazon Pinpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.send_voice_message)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#send_voice_message)
        """

    async def set_default_message_type(
        self, *, ConfigurationSetName: str, MessageType: MessageTypeType
    ) -> SetDefaultMessageTypeResultTypeDef:
        """
        Sets the default message type on a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.set_default_message_type)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#set_default_message_type)
        """

    async def set_default_sender_id(
        self, *, ConfigurationSetName: str, SenderId: str
    ) -> SetDefaultSenderIdResultTypeDef:
        """
        Sets default sender ID on a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.set_default_sender_id)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#set_default_sender_id)
        """

    async def set_text_message_spend_limit_override(
        self, *, MonthlyLimit: int
    ) -> SetTextMessageSpendLimitOverrideResultTypeDef:
        """
        Sets an account level monthly spend limit override for sending text messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.set_text_message_spend_limit_override)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#set_text_message_spend_limit_override)
        """

    async def set_voice_message_spend_limit_override(
        self, *, MonthlyLimit: int
    ) -> SetVoiceMessageSpendLimitOverrideResultTypeDef:
        """
        Sets an account level monthly spend limit override for sending voice messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.set_voice_message_spend_limit_override)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#set_voice_message_spend_limit_override)
        """

    async def tag_resource(self, *, ResourceArn: str, Tags: Sequence[TagTypeDef]) -> Dict[str, Any]:
        """
        Adds or overwrites only the specified tags for the specified Amazon Pinpoint SMS
        Voice, version 2 resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#tag_resource)
        """

    async def untag_resource(self, *, ResourceArn: str, TagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Removes the association of the specified tags from an Amazon Pinpoint SMS Voice
        V2 resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#untag_resource)
        """

    async def update_event_destination(
        self,
        *,
        ConfigurationSetName: str,
        EventDestinationName: str,
        Enabled: bool = ...,
        MatchingEventTypes: Sequence[EventTypeType] = ...,
        CloudWatchLogsDestination: CloudWatchLogsDestinationTypeDef = ...,
        KinesisFirehoseDestination: KinesisFirehoseDestinationTypeDef = ...,
        SnsDestination: SnsDestinationTypeDef = ...
    ) -> UpdateEventDestinationResultTypeDef:
        """
        Updates an existing event destination in a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.update_event_destination)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#update_event_destination)
        """

    async def update_phone_number(
        self,
        *,
        PhoneNumberId: str,
        TwoWayEnabled: bool = ...,
        TwoWayChannelArn: str = ...,
        SelfManagedOptOutsEnabled: bool = ...,
        OptOutListName: str = ...,
        DeletionProtectionEnabled: bool = ...
    ) -> UpdatePhoneNumberResultTypeDef:
        """
        Updates the configuration of an existing origination phone number.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.update_phone_number)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#update_phone_number)
        """

    async def update_pool(
        self,
        *,
        PoolId: str,
        TwoWayEnabled: bool = ...,
        TwoWayChannelArn: str = ...,
        SelfManagedOptOutsEnabled: bool = ...,
        OptOutListName: str = ...,
        SharedRoutesEnabled: bool = ...,
        DeletionProtectionEnabled: bool = ...
    ) -> UpdatePoolResultTypeDef:
        """
        Updates the configuration of an existing pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.update_pool)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#update_pool)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_account_attributes"]
    ) -> DescribeAccountAttributesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_account_limits"]
    ) -> DescribeAccountLimitsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_configuration_sets"]
    ) -> DescribeConfigurationSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_keywords"]
    ) -> DescribeKeywordsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_opt_out_lists"]
    ) -> DescribeOptOutListsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_opted_out_numbers"]
    ) -> DescribeOptedOutNumbersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_phone_numbers"]
    ) -> DescribePhoneNumbersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_pools"]) -> DescribePoolsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_sender_ids"]
    ) -> DescribeSenderIdsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_spend_limits"]
    ) -> DescribeSpendLimitsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_pool_origination_identities"]
    ) -> ListPoolOriginationIdentitiesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    async def __aenter__(self) -> "PinpointSMSVoiceV2Client":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/)
        """
