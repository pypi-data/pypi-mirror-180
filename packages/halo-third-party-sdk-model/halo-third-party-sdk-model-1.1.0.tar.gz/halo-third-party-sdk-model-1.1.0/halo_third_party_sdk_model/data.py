# coding: utf-8

#
# Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file
# except in compliance with the License. A copy of the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for
# the specific language governing permissions and limitations under the License.
#

import pprint
import re  # noqa: F401
import six
import typing
from enum import Enum


if typing.TYPE_CHECKING:
    from typing import Dict, List, Optional, Union, Any
    from datetime import datetime
    from halo_third_party_sdk_model.record import Record as Record_63aab970
    from halo_third_party_sdk_model.deauthorization import Deauthorization as Deauthorization_d70cc964


class Data(object):
    """
    An object containing the data payload of the message.


    :param records: An array of daily summaries (records).
    :type records: (optional) list[halo_third_party_sdk_model.record.Record]
    :param deauthorization: 
    :type deauthorization: (optional) halo_third_party_sdk_model.deauthorization.Deauthorization

    """
    deserialized_types = {
        'records': 'list[halo_third_party_sdk_model.record.Record]',
        'deauthorization': 'halo_third_party_sdk_model.deauthorization.Deauthorization'
    }  # type: Dict

    attribute_map = {
        'records': 'records',
        'deauthorization': 'deauthorization'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, records=None, deauthorization=None):
        # type: (Optional[List[Record_63aab970]], Optional[Deauthorization_d70cc964]) -> None
        """An object containing the data payload of the message.

        :param records: An array of daily summaries (records).
        :type records: (optional) list[halo_third_party_sdk_model.record.Record]
        :param deauthorization: 
        :type deauthorization: (optional) halo_third_party_sdk_model.deauthorization.Deauthorization
        """
        self.__discriminator_value = None  # type: str

        self.records = records
        self.deauthorization = deauthorization

    def to_dict(self):
        # type: () -> Dict[str, object]
        """Returns the model properties as a dict"""
        result = {}  # type: Dict

        for attr, _ in six.iteritems(self.deserialized_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else
                    x.value if isinstance(x, Enum) else x,
                    value
                ))
            elif isinstance(value, Enum):
                result[attr] = value.value
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else
                    (item[0], item[1].value)
                    if isinstance(item[1], Enum) else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        # type: () -> str
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        # type: () -> str
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are equal"""
        if not isinstance(other, Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
