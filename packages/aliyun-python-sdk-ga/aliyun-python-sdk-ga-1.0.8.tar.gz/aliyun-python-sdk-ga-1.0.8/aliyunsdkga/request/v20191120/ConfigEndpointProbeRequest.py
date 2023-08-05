# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkga.endpoint import endpoint_data

class ConfigEndpointProbeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ga', '2019-11-20', 'ConfigEndpointProbe','gaplus')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_Endpoint(self): # String
		return self.get_query_params().get('Endpoint')

	def set_Endpoint(self, Endpoint):  # String
		self.add_query_param('Endpoint', Endpoint)
	def get_EndpointType(self): # String
		return self.get_query_params().get('EndpointType')

	def set_EndpointType(self, EndpointType):  # String
		self.add_query_param('EndpointType', EndpointType)
	def get_Enable(self): # String
		return self.get_query_params().get('Enable')

	def set_Enable(self, Enable):  # String
		self.add_query_param('Enable', Enable)
	def get_ProbeProtocol(self): # String
		return self.get_query_params().get('ProbeProtocol')

	def set_ProbeProtocol(self, ProbeProtocol):  # String
		self.add_query_param('ProbeProtocol', ProbeProtocol)
	def get_ProbePort(self): # String
		return self.get_query_params().get('ProbePort')

	def set_ProbePort(self, ProbePort):  # String
		self.add_query_param('ProbePort', ProbePort)
	def get_EndpointGroupId(self): # String
		return self.get_query_params().get('EndpointGroupId')

	def set_EndpointGroupId(self, EndpointGroupId):  # String
		self.add_query_param('EndpointGroupId', EndpointGroupId)
