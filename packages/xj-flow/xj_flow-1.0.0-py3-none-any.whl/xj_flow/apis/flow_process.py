# _*_coding:utf-8_*_

from rest_framework.views import APIView
from ..services.flow_process_service import FlowProcessService
from ..utils.custom_response import util_response
from ..utils.request_params_wrapper import request_params_wrapper

class FlowProcess(APIView):
    def __init__(self):
        pass

    @request_params_wrapper
    def post(self, request, request_params=None):
        """
        流程作业
        """
        # print("FlowProcess: request_params:", request_params)
        flow_node_id = request_params.pop('flow_node_id', None)
        flow_action_id = request_params.pop('flow_action_id', None)
        # print("FlowProcess: request_params 2:", request_params)
        if not flow_node_id:
            return util_response(err=1001, msg='flow_node_id 必填')
        if not flow_action_id:
            return util_response(err=1001, msg='flow_action_id 必填')
        new_params, error_text = FlowProcessService.do_once_flow(flow_node_id=flow_node_id,
                                                                 flow_action_id=flow_action_id,
                                                                 source_params=request_params)

        return util_response(data={"flow_node_id": flow_node_id, "flow_action_id": flow_action_id, "params": new_params,
                                   "old_params": request_params})
