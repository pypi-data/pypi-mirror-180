# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Pager:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page': 'int',
        'page_size': 'int',
        'total_rows': 'int'
    }

    attribute_map = {
        'page': 'page',
        'page_size': 'page_size',
        'total_rows': 'total_rows'
    }

    def __init__(self, page=None, page_size=None, total_rows=None):
        """Pager

        The model defined in huaweicloud sdk

        :param page: 页码
        :type page: int
        :param page_size: 每页大小
        :type page_size: int
        :param total_rows: 总条数
        :type total_rows: int
        """
        
        

        self._page = None
        self._page_size = None
        self._total_rows = None
        self.discriminator = None

        if page is not None:
            self.page = page
        if page_size is not None:
            self.page_size = page_size
        if total_rows is not None:
            self.total_rows = total_rows

    @property
    def page(self):
        """Gets the page of this Pager.

        页码

        :return: The page of this Pager.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this Pager.

        页码

        :param page: The page of this Pager.
        :type page: int
        """
        self._page = page

    @property
    def page_size(self):
        """Gets the page_size of this Pager.

        每页大小

        :return: The page_size of this Pager.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this Pager.

        每页大小

        :param page_size: The page_size of this Pager.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def total_rows(self):
        """Gets the total_rows of this Pager.

        总条数

        :return: The total_rows of this Pager.
        :rtype: int
        """
        return self._total_rows

    @total_rows.setter
    def total_rows(self, total_rows):
        """Sets the total_rows of this Pager.

        总条数

        :param total_rows: The total_rows of this Pager.
        :type total_rows: int
        """
        self._total_rows = total_rows

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Pager):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
