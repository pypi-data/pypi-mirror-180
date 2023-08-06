# _*_coding:utf-8_*_

from ..models import FlowNodeActionRule
from ..utils.j_dict import JDict


class FlowProcessService:

    @staticmethod
    def do_once_flow(flow_node_id, flow_action_id, source_params={}):
        """
        执行一次流程处理
        @param flow_node_id 流程节点ID
        @param flow_action_id 希望处理的流程动作ID
        @param source_params 需要处理的原数据
        """

        flow_rule_list = list(FlowNodeActionRule.objects.filter(flow_node_to_action_id__flow_node_id=flow_node_id, \
                                                                flow_node_to_action_id__flow_action_id=flow_action_id,\
                                                                ).values())
        # print("flow_rule_list:", flow_rule_list)

        new_params = JDict(source_params.copy())
        # print("new_params:", new_params)

        for index, rule in enumerate(flow_rule_list):
            # print("rule:", rule)
            rr = JDict(rule)
            if not rr.inflow_field:
                continue

            if not rr.default_value:
                continue

            if rr.inflow_module == 'ENROLL':
                # print("current module:", rr.inflow_module)
                pass
            if rr.inflow_module == 'THREAD':
                # print("current module:", rr.inflow_module)
                pass

            # print("rule 2:", rule)

            new_params[rr.inflow_field] = rr.default_value

        # print("new_params:", new_params)

        return new_params, None
