# coding: utf-8

"""
    Lightly API

    Lightly.ai enables you to do self-supervised learning in an easy and intuitive way. The lightly.ai OpenAPI spec defines how one can interact with our REST API to unleash the full potential of lightly.ai  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@lightly.ai
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from lightly.openapi_generated.swagger_client.configuration import Configuration


class SampleDataModes(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'MongoObjectID',
        'type': 'SampleType',
        'dataset_id': 'MongoObjectID',
        'file_name': 'str',
        'thumb_name': 'str',
        'exif': 'dict(str, object)',
        'index': 'int',
        'created_at': 'Timestamp',
        'last_modified_at': 'Timestamp',
        'meta_data': 'SampleMetaData',
        'custom_meta_data': 'CustomSampleMetaData',
        'video_frame_data': 'VideoFrameData',
        'crop_data': 'CropData'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'dataset_id': 'datasetId',
        'file_name': 'fileName',
        'thumb_name': 'thumbName',
        'exif': 'exif',
        'index': 'index',
        'created_at': 'createdAt',
        'last_modified_at': 'lastModifiedAt',
        'meta_data': 'metaData',
        'custom_meta_data': 'customMetaData',
        'video_frame_data': 'videoFrameData',
        'crop_data': 'cropData'
    }

    def __init__(self, id=None, type=None, dataset_id=None, file_name=None, thumb_name=None, exif=None, index=None, created_at=None, last_modified_at=None, meta_data=None, custom_meta_data=None, video_frame_data=None, crop_data=None, _configuration=None):  # noqa: E501
        """SampleDataModes - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._type = None
        self._dataset_id = None
        self._file_name = None
        self._thumb_name = None
        self._exif = None
        self._index = None
        self._created_at = None
        self._last_modified_at = None
        self._meta_data = None
        self._custom_meta_data = None
        self._video_frame_data = None
        self._crop_data = None
        self.discriminator = None

        self.id = id
        if type is not None:
            self.type = type
        if dataset_id is not None:
            self.dataset_id = dataset_id
        if file_name is not None:
            self.file_name = file_name
        if thumb_name is not None:
            self.thumb_name = thumb_name
        if exif is not None:
            self.exif = exif
        if index is not None:
            self.index = index
        if created_at is not None:
            self.created_at = created_at
        if last_modified_at is not None:
            self.last_modified_at = last_modified_at
        if meta_data is not None:
            self.meta_data = meta_data
        if custom_meta_data is not None:
            self.custom_meta_data = custom_meta_data
        if video_frame_data is not None:
            self.video_frame_data = video_frame_data
        if crop_data is not None:
            self.crop_data = crop_data

    @property
    def id(self):
        """Gets the id of this SampleDataModes.  # noqa: E501


        :return: The id of this SampleDataModes.  # noqa: E501
        :rtype: MongoObjectID
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SampleDataModes.


        :param id: The id of this SampleDataModes.  # noqa: E501
        :type: MongoObjectID
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this SampleDataModes.  # noqa: E501


        :return: The type of this SampleDataModes.  # noqa: E501
        :rtype: SampleType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SampleDataModes.


        :param type: The type of this SampleDataModes.  # noqa: E501
        :type: SampleType
        """

        self._type = type

    @property
    def dataset_id(self):
        """Gets the dataset_id of this SampleDataModes.  # noqa: E501


        :return: The dataset_id of this SampleDataModes.  # noqa: E501
        :rtype: MongoObjectID
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        """Sets the dataset_id of this SampleDataModes.


        :param dataset_id: The dataset_id of this SampleDataModes.  # noqa: E501
        :type: MongoObjectID
        """

        self._dataset_id = dataset_id

    @property
    def file_name(self):
        """Gets the file_name of this SampleDataModes.  # noqa: E501


        :return: The file_name of this SampleDataModes.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this SampleDataModes.


        :param file_name: The file_name of this SampleDataModes.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def thumb_name(self):
        """Gets the thumb_name of this SampleDataModes.  # noqa: E501


        :return: The thumb_name of this SampleDataModes.  # noqa: E501
        :rtype: str
        """
        return self._thumb_name

    @thumb_name.setter
    def thumb_name(self, thumb_name):
        """Sets the thumb_name of this SampleDataModes.


        :param thumb_name: The thumb_name of this SampleDataModes.  # noqa: E501
        :type: str
        """

        self._thumb_name = thumb_name

    @property
    def exif(self):
        """Gets the exif of this SampleDataModes.  # noqa: E501


        :return: The exif of this SampleDataModes.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._exif

    @exif.setter
    def exif(self, exif):
        """Sets the exif of this SampleDataModes.


        :param exif: The exif of this SampleDataModes.  # noqa: E501
        :type: dict(str, object)
        """

        self._exif = exif

    @property
    def index(self):
        """Gets the index of this SampleDataModes.  # noqa: E501


        :return: The index of this SampleDataModes.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this SampleDataModes.


        :param index: The index of this SampleDataModes.  # noqa: E501
        :type: int
        """

        self._index = index

    @property
    def created_at(self):
        """Gets the created_at of this SampleDataModes.  # noqa: E501


        :return: The created_at of this SampleDataModes.  # noqa: E501
        :rtype: Timestamp
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SampleDataModes.


        :param created_at: The created_at of this SampleDataModes.  # noqa: E501
        :type: Timestamp
        """

        self._created_at = created_at

    @property
    def last_modified_at(self):
        """Gets the last_modified_at of this SampleDataModes.  # noqa: E501


        :return: The last_modified_at of this SampleDataModes.  # noqa: E501
        :rtype: Timestamp
        """
        return self._last_modified_at

    @last_modified_at.setter
    def last_modified_at(self, last_modified_at):
        """Sets the last_modified_at of this SampleDataModes.


        :param last_modified_at: The last_modified_at of this SampleDataModes.  # noqa: E501
        :type: Timestamp
        """

        self._last_modified_at = last_modified_at

    @property
    def meta_data(self):
        """Gets the meta_data of this SampleDataModes.  # noqa: E501


        :return: The meta_data of this SampleDataModes.  # noqa: E501
        :rtype: SampleMetaData
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """Sets the meta_data of this SampleDataModes.


        :param meta_data: The meta_data of this SampleDataModes.  # noqa: E501
        :type: SampleMetaData
        """

        self._meta_data = meta_data

    @property
    def custom_meta_data(self):
        """Gets the custom_meta_data of this SampleDataModes.  # noqa: E501


        :return: The custom_meta_data of this SampleDataModes.  # noqa: E501
        :rtype: CustomSampleMetaData
        """
        return self._custom_meta_data

    @custom_meta_data.setter
    def custom_meta_data(self, custom_meta_data):
        """Sets the custom_meta_data of this SampleDataModes.


        :param custom_meta_data: The custom_meta_data of this SampleDataModes.  # noqa: E501
        :type: CustomSampleMetaData
        """

        self._custom_meta_data = custom_meta_data

    @property
    def video_frame_data(self):
        """Gets the video_frame_data of this SampleDataModes.  # noqa: E501


        :return: The video_frame_data of this SampleDataModes.  # noqa: E501
        :rtype: VideoFrameData
        """
        return self._video_frame_data

    @video_frame_data.setter
    def video_frame_data(self, video_frame_data):
        """Sets the video_frame_data of this SampleDataModes.


        :param video_frame_data: The video_frame_data of this SampleDataModes.  # noqa: E501
        :type: VideoFrameData
        """

        self._video_frame_data = video_frame_data

    @property
    def crop_data(self):
        """Gets the crop_data of this SampleDataModes.  # noqa: E501


        :return: The crop_data of this SampleDataModes.  # noqa: E501
        :rtype: CropData
        """
        return self._crop_data

    @crop_data.setter
    def crop_data(self, crop_data):
        """Sets the crop_data of this SampleDataModes.


        :param crop_data: The crop_data of this SampleDataModes.  # noqa: E501
        :type: CropData
        """

        self._crop_data = crop_data

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
                result[attr] = value
        if issubclass(SampleDataModes, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SampleDataModes):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SampleDataModes):
            return True

        return self.to_dict() != other.to_dict()
