"""
Type annotations for rolesanywhere service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/type_defs/)

Usage::

    ```python
    from types_aiobotocore_rolesanywhere.type_defs import TagTypeDef

    data: TagTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Sequence, Union

from aiobotocore.response import StreamingBody

from .literals import TrustAnchorTypeType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "TagTypeDef",
    "CredentialSummaryTypeDef",
    "CrlDetailTypeDef",
    "ResponseMetadataTypeDef",
    "InstancePropertyTypeDef",
    "ProfileDetailTypeDef",
    "PaginatorConfigTypeDef",
    "ListRequestRequestTypeDef",
    "SubjectSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ScalarCrlRequestRequestTypeDef",
    "ScalarProfileRequestRequestTypeDef",
    "ScalarSubjectRequestRequestTypeDef",
    "ScalarTrustAnchorRequestRequestTypeDef",
    "SourceDataTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateCrlRequestRequestTypeDef",
    "UpdateProfileRequestRequestTypeDef",
    "CreateProfileRequestRequestTypeDef",
    "ImportCrlRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CrlDetailResponseTypeDef",
    "ListCrlsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "SubjectDetailTypeDef",
    "ListProfilesResponseTypeDef",
    "ProfileDetailResponseTypeDef",
    "ListRequestListCrlsPaginateTypeDef",
    "ListRequestListProfilesPaginateTypeDef",
    "ListRequestListSubjectsPaginateTypeDef",
    "ListRequestListTrustAnchorsPaginateTypeDef",
    "ListSubjectsResponseTypeDef",
    "SourceTypeDef",
    "SubjectDetailResponseTypeDef",
    "CreateTrustAnchorRequestRequestTypeDef",
    "TrustAnchorDetailTypeDef",
    "UpdateTrustAnchorRequestRequestTypeDef",
    "ListTrustAnchorsResponseTypeDef",
    "TrustAnchorDetailResponseTypeDef",
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)

CredentialSummaryTypeDef = TypedDict(
    "CredentialSummaryTypeDef",
    {
        "enabled": bool,
        "failed": bool,
        "issuer": str,
        "seenAt": datetime,
        "serialNumber": str,
        "x509CertificateData": str,
    },
    total=False,
)

CrlDetailTypeDef = TypedDict(
    "CrlDetailTypeDef",
    {
        "createdAt": datetime,
        "crlArn": str,
        "crlData": bytes,
        "crlId": str,
        "enabled": bool,
        "name": str,
        "trustAnchorArn": str,
        "updatedAt": datetime,
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
    },
)

InstancePropertyTypeDef = TypedDict(
    "InstancePropertyTypeDef",
    {
        "failed": bool,
        "properties": Dict[str, str],
        "seenAt": datetime,
    },
    total=False,
)

ProfileDetailTypeDef = TypedDict(
    "ProfileDetailTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "durationSeconds": int,
        "enabled": bool,
        "managedPolicyArns": List[str],
        "name": str,
        "profileArn": str,
        "profileId": str,
        "requireInstanceProperties": bool,
        "roleArns": List[str],
        "sessionPolicy": str,
        "updatedAt": datetime,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

ListRequestRequestTypeDef = TypedDict(
    "ListRequestRequestTypeDef",
    {
        "nextToken": str,
        "pageSize": int,
    },
    total=False,
)

SubjectSummaryTypeDef = TypedDict(
    "SubjectSummaryTypeDef",
    {
        "createdAt": datetime,
        "enabled": bool,
        "lastSeenAt": datetime,
        "subjectArn": str,
        "subjectId": str,
        "updatedAt": datetime,
        "x509Subject": str,
    },
    total=False,
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ScalarCrlRequestRequestTypeDef = TypedDict(
    "ScalarCrlRequestRequestTypeDef",
    {
        "crlId": str,
    },
)

ScalarProfileRequestRequestTypeDef = TypedDict(
    "ScalarProfileRequestRequestTypeDef",
    {
        "profileId": str,
    },
)

ScalarSubjectRequestRequestTypeDef = TypedDict(
    "ScalarSubjectRequestRequestTypeDef",
    {
        "subjectId": str,
    },
)

ScalarTrustAnchorRequestRequestTypeDef = TypedDict(
    "ScalarTrustAnchorRequestRequestTypeDef",
    {
        "trustAnchorId": str,
    },
)

SourceDataTypeDef = TypedDict(
    "SourceDataTypeDef",
    {
        "acmPcaArn": str,
        "x509CertificateData": str,
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

_RequiredUpdateCrlRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateCrlRequestRequestTypeDef",
    {
        "crlId": str,
    },
)
_OptionalUpdateCrlRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateCrlRequestRequestTypeDef",
    {
        "crlData": Union[str, bytes, IO[Any], StreamingBody],
        "name": str,
    },
    total=False,
)


class UpdateCrlRequestRequestTypeDef(
    _RequiredUpdateCrlRequestRequestTypeDef, _OptionalUpdateCrlRequestRequestTypeDef
):
    pass


_RequiredUpdateProfileRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateProfileRequestRequestTypeDef",
    {
        "profileId": str,
    },
)
_OptionalUpdateProfileRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateProfileRequestRequestTypeDef",
    {
        "durationSeconds": int,
        "managedPolicyArns": Sequence[str],
        "name": str,
        "roleArns": Sequence[str],
        "sessionPolicy": str,
    },
    total=False,
)


class UpdateProfileRequestRequestTypeDef(
    _RequiredUpdateProfileRequestRequestTypeDef, _OptionalUpdateProfileRequestRequestTypeDef
):
    pass


_RequiredCreateProfileRequestRequestTypeDef = TypedDict(
    "_RequiredCreateProfileRequestRequestTypeDef",
    {
        "name": str,
        "roleArns": Sequence[str],
    },
)
_OptionalCreateProfileRequestRequestTypeDef = TypedDict(
    "_OptionalCreateProfileRequestRequestTypeDef",
    {
        "durationSeconds": int,
        "enabled": bool,
        "managedPolicyArns": Sequence[str],
        "requireInstanceProperties": bool,
        "sessionPolicy": str,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateProfileRequestRequestTypeDef(
    _RequiredCreateProfileRequestRequestTypeDef, _OptionalCreateProfileRequestRequestTypeDef
):
    pass


_RequiredImportCrlRequestRequestTypeDef = TypedDict(
    "_RequiredImportCrlRequestRequestTypeDef",
    {
        "crlData": Union[str, bytes, IO[Any], StreamingBody],
        "name": str,
        "trustAnchorArn": str,
    },
)
_OptionalImportCrlRequestRequestTypeDef = TypedDict(
    "_OptionalImportCrlRequestRequestTypeDef",
    {
        "enabled": bool,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)


class ImportCrlRequestRequestTypeDef(
    _RequiredImportCrlRequestRequestTypeDef, _OptionalImportCrlRequestRequestTypeDef
):
    pass


TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence[TagTypeDef],
    },
)

CrlDetailResponseTypeDef = TypedDict(
    "CrlDetailResponseTypeDef",
    {
        "crl": CrlDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListCrlsResponseTypeDef = TypedDict(
    "ListCrlsResponseTypeDef",
    {
        "crls": List[CrlDetailTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

SubjectDetailTypeDef = TypedDict(
    "SubjectDetailTypeDef",
    {
        "createdAt": datetime,
        "credentials": List[CredentialSummaryTypeDef],
        "enabled": bool,
        "instanceProperties": List[InstancePropertyTypeDef],
        "lastSeenAt": datetime,
        "subjectArn": str,
        "subjectId": str,
        "updatedAt": datetime,
        "x509Subject": str,
    },
    total=False,
)

ListProfilesResponseTypeDef = TypedDict(
    "ListProfilesResponseTypeDef",
    {
        "nextToken": str,
        "profiles": List[ProfileDetailTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ProfileDetailResponseTypeDef = TypedDict(
    "ProfileDetailResponseTypeDef",
    {
        "profile": ProfileDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListRequestListCrlsPaginateTypeDef = TypedDict(
    "ListRequestListCrlsPaginateTypeDef",
    {
        "pageSize": int,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListRequestListProfilesPaginateTypeDef = TypedDict(
    "ListRequestListProfilesPaginateTypeDef",
    {
        "pageSize": int,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListRequestListSubjectsPaginateTypeDef = TypedDict(
    "ListRequestListSubjectsPaginateTypeDef",
    {
        "pageSize": int,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListRequestListTrustAnchorsPaginateTypeDef = TypedDict(
    "ListRequestListTrustAnchorsPaginateTypeDef",
    {
        "pageSize": int,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListSubjectsResponseTypeDef = TypedDict(
    "ListSubjectsResponseTypeDef",
    {
        "nextToken": str,
        "subjects": List[SubjectSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

SourceTypeDef = TypedDict(
    "SourceTypeDef",
    {
        "sourceData": SourceDataTypeDef,
        "sourceType": TrustAnchorTypeType,
    },
    total=False,
)

SubjectDetailResponseTypeDef = TypedDict(
    "SubjectDetailResponseTypeDef",
    {
        "subject": SubjectDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateTrustAnchorRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTrustAnchorRequestRequestTypeDef",
    {
        "name": str,
        "source": SourceTypeDef,
    },
)
_OptionalCreateTrustAnchorRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTrustAnchorRequestRequestTypeDef",
    {
        "enabled": bool,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateTrustAnchorRequestRequestTypeDef(
    _RequiredCreateTrustAnchorRequestRequestTypeDef, _OptionalCreateTrustAnchorRequestRequestTypeDef
):
    pass


TrustAnchorDetailTypeDef = TypedDict(
    "TrustAnchorDetailTypeDef",
    {
        "createdAt": datetime,
        "enabled": bool,
        "name": str,
        "source": SourceTypeDef,
        "trustAnchorArn": str,
        "trustAnchorId": str,
        "updatedAt": datetime,
    },
    total=False,
)

_RequiredUpdateTrustAnchorRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTrustAnchorRequestRequestTypeDef",
    {
        "trustAnchorId": str,
    },
)
_OptionalUpdateTrustAnchorRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTrustAnchorRequestRequestTypeDef",
    {
        "name": str,
        "source": SourceTypeDef,
    },
    total=False,
)


class UpdateTrustAnchorRequestRequestTypeDef(
    _RequiredUpdateTrustAnchorRequestRequestTypeDef, _OptionalUpdateTrustAnchorRequestRequestTypeDef
):
    pass


ListTrustAnchorsResponseTypeDef = TypedDict(
    "ListTrustAnchorsResponseTypeDef",
    {
        "nextToken": str,
        "trustAnchors": List[TrustAnchorDetailTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

TrustAnchorDetailResponseTypeDef = TypedDict(
    "TrustAnchorDetailResponseTypeDef",
    {
        "trustAnchor": TrustAnchorDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
