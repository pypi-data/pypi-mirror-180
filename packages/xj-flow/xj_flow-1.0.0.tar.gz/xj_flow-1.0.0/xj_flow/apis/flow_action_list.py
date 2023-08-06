# _*_coding:utf-8_*_

from rest_framework.views import APIView
from ..services.flow_process_service import FlowProcessService
from ..services.flow_basic_service import FlowBasicService
from ..utils.custom_response import util_response
from ..utils.request_params_wrapper import request_params_wrapper

class FlowActionList(APIView):
    def __init__(self):
        pass

    @request_params_wrapper
    def get(self, request, request_params=None):
        """
        流程作业
        """
        print("FlowProcess: request_params:", request_params)
        flow_id = request_params.get('flow_id', None)
        flow_node_id = request_params.get('flow_node_id', None)
        user_id = request_params.get('user_id', None)
        role_id = request_params.get('role_id', None)
        flow_action_list, error_text = FlowBasicService.get_flow_action_list(flow_id=flow_id, flow_node_id=flow_node_id,
                                                                             user_id=user_id, role_id=role_id)

        return util_response(data=flow_action_list)
