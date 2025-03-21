from mstrio.connection import Connection

from ..schedule import Schedule
from .base_subscription import Subscription
from .content import Content
from .delivery import CacheType, Delivery, LibraryCacheTypes, ShortcutCacheFormat


class CacheUpdateSubscription(Subscription):
    """Class representation of MicroStrategy Cache Update Subscription
    object."""

    def __init__(
        self,
        connection: Connection,
        id: str | None = None,
        subscription_id: str | None = None,
        project_id: str | None = None,
        project_name: str | None = None,
    ):
        """Initialize CacheUpdateSubscription object, populates it with
        I-Server data if id or subscription_id is passed.
        Specify either `project_id` or `project_name`.
        When `project_id` is provided (not `None`), `project_name` is omitted.

        Args:
            connection (Connection): MicroStrategy connection object returned
                by `connection.Connection()`
            id (str, optional): ID of the subscription to be initialized, only
                id or subscription_id have to be provided at once, if both are
                provided id will take precedence
            subscription_id (str, optional): ID of the subscription to be
                initialized
            project_id (str, optional): Project ID
            project_name (str, optional): Project name
        """
        super().__init__(connection, id, subscription_id, project_id, project_name)

    @classmethod
    def create(
        cls,
        connection: Connection,
        name: str,
        project_id: str | None = None,
        project_name: str | None = None,
        allow_delivery_changes: bool | None = None,
        allow_personalization_changes: bool | None = None,
        allow_unsubscribe: bool | None = None,
        send_now: bool | None = None,
        owner_id: str | None = None,
        schedules: str | list[str] | Schedule | list[Schedule] | None = None,
        contents: Content | None = None,
        recipients: list[dict] | list[str] | None = None,
        delivery: Delivery | dict | None = None,
        delivery_expiration_date: str | None = None,
        delivery_expiration_timezone: str | None = None,
        contact_security: bool = True,
        cache_cache_type: CacheType | str | None = None,
        cache_shortcut_cache_format: ShortcutCacheFormat | str | None = None,
        cache_library_cache_types: list[LibraryCacheTypes | str] | None = None,
        cache_reuse_dataset_cache: bool = False,
        cache_is_all_library_users: bool = False,
        delivery_notification_enabled: bool = False,
        delivery_personal_notification_address_id: str | None = None,
    ) -> "CacheUpdateSubscription":
        """Creates a new cache update subscription.

        Args:
            connection (Connection): a MicroStrategy connection object
            name (str): name of the subscription,
            project_id (str, optional): project ID,
            project_name (str, optional): project name,
            allow_delivery_changes (bool, optional): whether the recipients can
                change the delivery of the subscription,
            allow_personalization_changes (bool, optional): whether the
                recipients can personalize the subscription,
            allow_unsubscribe (bool, optional): whether the recipients can
                unsubscribe from the subscription,
            send_now (bool, optional): indicates whether to execute the
                subscription immediately,
            owner_id (str, optional): ID of the subscription owner, by default
                logged in user ID,
            schedules (str | list[str] | Schedule | list[Schedule], optional):
                Schedules IDs or Schedule objects,
            contents (Content, optional): The content settings.
            recipients (list[str] | list[dict], optional): list of recipients
                IDs or dicts,
            delivery (Delivery | dict, optional): delivery object or dict
            delivery_expiration_date (str, optional): expiration date of the
                subscription, format should be yyyy - MM - dd,
            delivery_expiration_timezone (str, optional): expiration timezone
                of the subscription, example value 'Europe/London'
            contact_security (bool): whether to use contact security for each
                contact group member
            cache_cache_type (CacheType | str, optional):
                [RESERVED, SHORTCUT, SHORTCUTWITHBOOKMARK]
            cache_shortcut_cache_format (ShortcutCacheFormat | str, optional):
                [RESERVED, JSON, BINARY, BOTH]
            cache_library_cache_types (list[LibraryCacheTypes | str], optional):
                Set of library cache types, available types can be
                web, android, ios
            cache_reuse_dataset_cache (bool): Whether to reuse dataset cache
            cache_is_all_library_users (bool): Whether for all library users
            delivery_notification_enabled (bool): Whether notification is
                enabled, notification applies to cache
            delivery_personal_notification_address_id (str, optional):
                Notification details

        Notes:
            To create a subscription with prompts, you need to provide
            the report instance ID with answered prompts for the content.
            Example:
            >>>contents=Content(
            >>>    id="<report_id>",
            >>>    type=Content.Type.REPORT,
            >>>    personalization=Content.Properties(
            >>>        format_type=Content.Properties.FormatType.PDF,
            >>>        prompt=Content.Properties.Prompt(
            >>>            enabled=True,
            >>>            instance_id="<instance_id>",
            >>>        ),
            >>>    ),
            >>>)
        """
        notification_address_id = delivery_personal_notification_address_id

        return super()._Subscription__create(
            connection=connection,
            name=name,
            project_id=project_id,
            project_name=project_name,
            allow_delivery_changes=allow_delivery_changes,
            allow_personalization_changes=allow_personalization_changes,
            allow_unsubscribe=allow_unsubscribe,
            send_now=send_now,
            owner_id=owner_id,
            schedules=schedules,
            contents=contents,
            recipients=recipients,
            delivery=delivery,
            delivery_mode=Delivery.DeliveryMode.CACHE,
            delivery_expiration_date=delivery_expiration_date,
            delivery_expiration_timezone=delivery_expiration_timezone,
            contact_security=contact_security,
            cache_cache_type=cache_cache_type or CacheType.RESERVED,
            cache_shortcut_cache_format=cache_shortcut_cache_format
            or ShortcutCacheFormat.RESERVED,
            cache_library_cache_types=cache_library_cache_types
            or [LibraryCacheTypes.WEB],
            cache_reuse_dataset_cache=cache_reuse_dataset_cache,
            cache_is_all_library_users=cache_is_all_library_users,
            delivery_notification_enabled=delivery_notification_enabled,
            delivery_personal_notification_address_id=notification_address_id,
        )

    def alter(
        self,
        name: str | None = None,
        allow_delivery_changes: bool | None = None,
        allow_personalization_changes: bool | None = None,
        allow_unsubscribe: bool | None = None,
        send_now: bool | None = None,
        owner_id: str | None = None,
        schedules: str | list[str] | Schedule | list[Schedule] | None = None,
        contents: Content | None = None,
        recipients: list[dict] | list[str] | None = None,
        delivery: Delivery | dict | None = None,
        custom_msg: str | None = None,
        delivery_expiration_date: str | None = None,
        delivery_expiration_timezone: str | None = None,
        contact_security: bool = True,
        cache_cache_type: CacheType | str | None = None,
        cache_shortcut_cache_format: ShortcutCacheFormat | str | None = None,
        cache_library_cache_types: list[LibraryCacheTypes | str] | None = None,
        cache_reuse_dataset_cache: bool = False,
        cache_is_all_library_users: bool = False,
        delivery_notification_enabled: bool = False,
        delivery_personal_notification_address_id: str | None = None,
    ):
        """Alter the subscription.

        Args:
            name (str): name of the subscription,
            allow_delivery_changes (bool, optional): whether the recipients can
                change the delivery of the subscription,
            allow_personalization_changes (bool, optional): whether the
                recipients can personalize the subscription,
            allow_unsubscribe (bool, optional): whether the recipients can
                unsubscribe from the subscription,
            send_now (bool, optional): indicates whether to execute the
                subscription immediately,
            owner_id (str, optional): ID of the subscription owner, by default
                logged in user ID,
            schedules (str | list[str] | Schedule | list[Schedule], optional):
                Schedules IDs or Schedule objects,
            contents (Content, optional): The content settings.
            recipients (list[str] | list[dict], optional): list of recipients
                IDs or dicts,
            delivery (Delivery | dict, optional): delivery object or dict
            delivery_expiration_date (str, optional): expiration date of the
                subscription, format should be yyyy - MM - dd,
            delivery_expiration_timezone (str, optional): expiration timezone
                of the subscription
            contact_security (bool): whether to use contact security for each
                contact group member
            cache_cache_type (CacheType | str, optional):
                [RESERVED, SHORTCUT, SHORTCUTWITHBOOKMARK]
            cache_shortcut_cache_format (ShortcutCacheFormat | str, optional):
                [RESERVED, JSON, BINARY, BOTH]
            cache_library_cache_types (list[LibraryCacheTypes | str], optional):
                Set of library cache types, available types can be
                web, android, ios
            cache_reuse_dataset_cache (bool): Whether to reuse dataset cache
            cache_is_all_library_users (bool): Whether for all library users
            delivery_notification_enabled (bool): Whether notification is
                enabled, notification applies to cache
            delivery_personal_notification_address_id (str, optional):
                Notification details
        """
        notification_address_id = delivery_personal_notification_address_id

        return super().alter(
            name=name,
            allow_delivery_changes=allow_delivery_changes,
            allow_personalization_changes=allow_personalization_changes,
            allow_unsubscribe=allow_unsubscribe,
            send_now=send_now,
            owner_id=owner_id,
            schedules=schedules,
            contents=contents,
            recipients=recipients,
            delivery=delivery,
            custom_msg=custom_msg,
            delivery_expiration_date=delivery_expiration_date,
            delivery_expiration_timezone=delivery_expiration_timezone,
            contact_security=contact_security,
            cache_cache_type=cache_cache_type or CacheType.RESERVED,
            cache_shortcut_cache_format=cache_shortcut_cache_format
            or ShortcutCacheFormat.RESERVED,
            cache_library_cache_types=cache_library_cache_types
            or [LibraryCacheTypes.WEB],
            cache_reuse_dataset_cache=cache_reuse_dataset_cache,
            cache_is_all_library_users=cache_is_all_library_users,
            delivery_notification_enabled=delivery_notification_enabled,
            delivery_personal_notification_address_id=notification_address_id,
        )
