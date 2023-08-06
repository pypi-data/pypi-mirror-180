# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cbn20170912 import models as cbn_20170912_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('cbn', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(
        self,
        product_id: str,
        region_id: str,
        endpoint_rule: str,
        network: str,
        suffix: str,
        endpoint_map: Dict[str, str],
        endpoint: str,
    ) -> str:
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def active_flow_log_with_options(
        self,
        request: cbn_20170912_models.ActiveFlowLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ActiveFlowLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ActiveFlowLog',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ActiveFlowLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def active_flow_log_with_options_async(
        self,
        request: cbn_20170912_models.ActiveFlowLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ActiveFlowLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ActiveFlowLog',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ActiveFlowLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def active_flow_log(
        self,
        request: cbn_20170912_models.ActiveFlowLogRequest,
    ) -> cbn_20170912_models.ActiveFlowLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.active_flow_log_with_options(request, runtime)

    async def active_flow_log_async(
        self,
        request: cbn_20170912_models.ActiveFlowLogRequest,
    ) -> cbn_20170912_models.ActiveFlowLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.active_flow_log_with_options_async(request, runtime)

    def add_traffic_match_rule_to_traffic_marking_policy_with_options(
        self,
        request: cbn_20170912_models.AddTrafficMatchRuleToTrafficMarkingPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.AddTrafficMatchRuleToTrafficMarkingPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.traffic_marking_policy_id):
            query['TrafficMarkingPolicyId'] = request.traffic_marking_policy_id
        if not UtilClient.is_unset(request.traffic_match_rules):
            query['TrafficMatchRules'] = request.traffic_match_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTrafficMatchRuleToTrafficMarkingPolicy',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.AddTrafficMatchRuleToTrafficMarkingPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_traffic_match_rule_to_traffic_marking_policy_with_options_async(
        self,
        request: cbn_20170912_models.AddTrafficMatchRuleToTrafficMarkingPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.AddTrafficMatchRuleToTrafficMarkingPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.traffic_marking_policy_id):
            query['TrafficMarkingPolicyId'] = request.traffic_marking_policy_id
        if not UtilClient.is_unset(request.traffic_match_rules):
            query['TrafficMatchRules'] = request.traffic_match_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTrafficMatchRuleToTrafficMarkingPolicy',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.AddTrafficMatchRuleToTrafficMarkingPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_traffic_match_rule_to_traffic_marking_policy(
        self,
        request: cbn_20170912_models.AddTrafficMatchRuleToTrafficMarkingPolicyRequest,
    ) -> cbn_20170912_models.AddTrafficMatchRuleToTrafficMarkingPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_traffic_match_rule_to_traffic_marking_policy_with_options(request, runtime)

    async def add_traffic_match_rule_to_traffic_marking_policy_async(
        self,
        request: cbn_20170912_models.AddTrafficMatchRuleToTrafficMarkingPolicyRequest,
    ) -> cbn_20170912_models.AddTrafficMatchRuleToTrafficMarkingPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_traffic_match_rule_to_traffic_marking_policy_with_options_async(request, runtime)

    def add_trafic_match_rule_to_traffic_marking_policy_with_options(
        self,
        request: cbn_20170912_models.AddTraficMatchRuleToTrafficMarkingPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.AddTraficMatchRuleToTrafficMarkingPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.traffic_marking_policy_id):
            query['TrafficMarkingPolicyId'] = request.traffic_marking_policy_id
        if not UtilClient.is_unset(request.traffic_match_rules):
            query['TrafficMatchRules'] = request.traffic_match_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTraficMatchRuleToTrafficMarkingPolicy',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.AddTraficMatchRuleToTrafficMarkingPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_trafic_match_rule_to_traffic_marking_policy_with_options_async(
        self,
        request: cbn_20170912_models.AddTraficMatchRuleToTrafficMarkingPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.AddTraficMatchRuleToTrafficMarkingPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.traffic_marking_policy_id):
            query['TrafficMarkingPolicyId'] = request.traffic_marking_policy_id
        if not UtilClient.is_unset(request.traffic_match_rules):
            query['TrafficMatchRules'] = request.traffic_match_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTraficMatchRuleToTrafficMarkingPolicy',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.AddTraficMatchRuleToTrafficMarkingPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_trafic_match_rule_to_traffic_marking_policy(
        self,
        request: cbn_20170912_models.AddTraficMatchRuleToTrafficMarkingPolicyRequest,
    ) -> cbn_20170912_models.AddTraficMatchRuleToTrafficMarkingPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_trafic_match_rule_to_traffic_marking_policy_with_options(request, runtime)

    async def add_trafic_match_rule_to_traffic_marking_policy_async(
        self,
        request: cbn_20170912_models.AddTraficMatchRuleToTrafficMarkingPolicyRequest,
    ) -> cbn_20170912_models.AddTraficMatchRuleToTrafficMarkingPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_trafic_match_rule_to_traffic_marking_policy_with_options_async(request, runtime)

    def associate_cen_bandwidth_package_with_options(
        self,
        request: cbn_20170912_models.AssociateCenBandwidthPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.AssociateCenBandwidthPackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_bandwidth_package_id):
            query['CenBandwidthPackageId'] = request.cen_bandwidth_package_id
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateCenBandwidthPackage',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.AssociateCenBandwidthPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_cen_bandwidth_package_with_options_async(
        self,
        request: cbn_20170912_models.AssociateCenBandwidthPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.AssociateCenBandwidthPackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_bandwidth_package_id):
            query['CenBandwidthPackageId'] = request.cen_bandwidth_package_id
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateCenBandwidthPackage',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.AssociateCenBandwidthPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_cen_bandwidth_package(
        self,
        request: cbn_20170912_models.AssociateCenBandwidthPackageRequest,
    ) -> cbn_20170912_models.AssociateCenBandwidthPackageResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_cen_bandwidth_package_with_options(request, runtime)

    async def associate_cen_bandwidth_package_async(
        self,
        request: cbn_20170912_models.AssociateCenBandwidthPackageRequest,
    ) -> cbn_20170912_models.AssociateCenBandwidthPackageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_cen_bandwidth_package_with_options_async(request, runtime)

    def associate_transit_router_attachment_with_route_table_with_options(
        self,
        request: cbn_20170912_models.AssociateTransitRouterAttachmentWithRouteTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.AssociateTransitRouterAttachmentWithRouteTableResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateTransitRouterAttachmentWithRouteTable',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.AssociateTransitRouterAttachmentWithRouteTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_transit_router_attachment_with_route_table_with_options_async(
        self,
        request: cbn_20170912_models.AssociateTransitRouterAttachmentWithRouteTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.AssociateTransitRouterAttachmentWithRouteTableResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateTransitRouterAttachmentWithRouteTable',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.AssociateTransitRouterAttachmentWithRouteTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_transit_router_attachment_with_route_table(
        self,
        request: cbn_20170912_models.AssociateTransitRouterAttachmentWithRouteTableRequest,
    ) -> cbn_20170912_models.AssociateTransitRouterAttachmentWithRouteTableResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_transit_router_attachment_with_route_table_with_options(request, runtime)

    async def associate_transit_router_attachment_with_route_table_async(
        self,
        request: cbn_20170912_models.AssociateTransitRouterAttachmentWithRouteTableRequest,
    ) -> cbn_20170912_models.AssociateTransitRouterAttachmentWithRouteTableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_transit_router_attachment_with_route_table_with_options_async(request, runtime)

    def associate_transit_router_multicast_domain_with_options(
        self,
        request: cbn_20170912_models.AssociateTransitRouterMulticastDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.AssociateTransitRouterMulticastDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        if not UtilClient.is_unset(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateTransitRouterMulticastDomain',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.AssociateTransitRouterMulticastDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_transit_router_multicast_domain_with_options_async(
        self,
        request: cbn_20170912_models.AssociateTransitRouterMulticastDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.AssociateTransitRouterMulticastDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        if not UtilClient.is_unset(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateTransitRouterMulticastDomain',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.AssociateTransitRouterMulticastDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_transit_router_multicast_domain(
        self,
        request: cbn_20170912_models.AssociateTransitRouterMulticastDomainRequest,
    ) -> cbn_20170912_models.AssociateTransitRouterMulticastDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_transit_router_multicast_domain_with_options(request, runtime)

    async def associate_transit_router_multicast_domain_async(
        self,
        request: cbn_20170912_models.AssociateTransitRouterMulticastDomainRequest,
    ) -> cbn_20170912_models.AssociateTransitRouterMulticastDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_transit_router_multicast_domain_with_options_async(request, runtime)

    def attach_cen_child_instance_with_options(
        self,
        request: cbn_20170912_models.AttachCenChildInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.AttachCenChildInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not UtilClient.is_unset(request.child_instance_owner_id):
            query['ChildInstanceOwnerId'] = request.child_instance_owner_id
        if not UtilClient.is_unset(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not UtilClient.is_unset(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachCenChildInstance',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.AttachCenChildInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_cen_child_instance_with_options_async(
        self,
        request: cbn_20170912_models.AttachCenChildInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.AttachCenChildInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not UtilClient.is_unset(request.child_instance_owner_id):
            query['ChildInstanceOwnerId'] = request.child_instance_owner_id
        if not UtilClient.is_unset(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not UtilClient.is_unset(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachCenChildInstance',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.AttachCenChildInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_cen_child_instance(
        self,
        request: cbn_20170912_models.AttachCenChildInstanceRequest,
    ) -> cbn_20170912_models.AttachCenChildInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_cen_child_instance_with_options(request, runtime)

    async def attach_cen_child_instance_async(
        self,
        request: cbn_20170912_models.AttachCenChildInstanceRequest,
    ) -> cbn_20170912_models.AttachCenChildInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_cen_child_instance_with_options_async(request, runtime)

    def check_transit_router_service_with_options(
        self,
        request: cbn_20170912_models.CheckTransitRouterServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CheckTransitRouterServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckTransitRouterService',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CheckTransitRouterServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_transit_router_service_with_options_async(
        self,
        request: cbn_20170912_models.CheckTransitRouterServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CheckTransitRouterServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckTransitRouterService',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CheckTransitRouterServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_transit_router_service(
        self,
        request: cbn_20170912_models.CheckTransitRouterServiceRequest,
    ) -> cbn_20170912_models.CheckTransitRouterServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_transit_router_service_with_options(request, runtime)

    async def check_transit_router_service_async(
        self,
        request: cbn_20170912_models.CheckTransitRouterServiceRequest,
    ) -> cbn_20170912_models.CheckTransitRouterServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_transit_router_service_with_options_async(request, runtime)

    def create_cen_with_options(
        self,
        request: cbn_20170912_models.CreateCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateCenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.protection_level):
            query['ProtectionLevel'] = request.protection_level
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCen',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateCenResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cen_with_options_async(
        self,
        request: cbn_20170912_models.CreateCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateCenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.protection_level):
            query['ProtectionLevel'] = request.protection_level
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCen',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateCenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cen(
        self,
        request: cbn_20170912_models.CreateCenRequest,
    ) -> cbn_20170912_models.CreateCenResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cen_with_options(request, runtime)

    async def create_cen_async(
        self,
        request: cbn_20170912_models.CreateCenRequest,
    ) -> cbn_20170912_models.CreateCenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cen_with_options_async(request, runtime)

    def create_cen_bandwidth_package_with_options(
        self,
        request: cbn_20170912_models.CreateCenBandwidthPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateCenBandwidthPackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_duration):
            query['AutoRenewDuration'] = request.auto_renew_duration
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.bandwidth_package_charge_type):
            query['BandwidthPackageChargeType'] = request.bandwidth_package_charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.geographic_region_aid):
            query['GeographicRegionAId'] = request.geographic_region_aid
        if not UtilClient.is_unset(request.geographic_region_bid):
            query['GeographicRegionBId'] = request.geographic_region_bid
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCenBandwidthPackage',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateCenBandwidthPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cen_bandwidth_package_with_options_async(
        self,
        request: cbn_20170912_models.CreateCenBandwidthPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateCenBandwidthPackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_duration):
            query['AutoRenewDuration'] = request.auto_renew_duration
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.bandwidth_package_charge_type):
            query['BandwidthPackageChargeType'] = request.bandwidth_package_charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.geographic_region_aid):
            query['GeographicRegionAId'] = request.geographic_region_aid
        if not UtilClient.is_unset(request.geographic_region_bid):
            query['GeographicRegionBId'] = request.geographic_region_bid
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCenBandwidthPackage',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateCenBandwidthPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cen_bandwidth_package(
        self,
        request: cbn_20170912_models.CreateCenBandwidthPackageRequest,
    ) -> cbn_20170912_models.CreateCenBandwidthPackageResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cen_bandwidth_package_with_options(request, runtime)

    async def create_cen_bandwidth_package_async(
        self,
        request: cbn_20170912_models.CreateCenBandwidthPackageRequest,
    ) -> cbn_20170912_models.CreateCenBandwidthPackageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cen_bandwidth_package_with_options_async(request, runtime)

    def create_cen_child_instance_route_entry_to_attachment_with_options(
        self,
        request: cbn_20170912_models.CreateCenChildInstanceRouteEntryToAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateCenChildInstanceRouteEntryToAttachmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.route_table_id):
            query['RouteTableId'] = request.route_table_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCenChildInstanceRouteEntryToAttachment',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateCenChildInstanceRouteEntryToAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cen_child_instance_route_entry_to_attachment_with_options_async(
        self,
        request: cbn_20170912_models.CreateCenChildInstanceRouteEntryToAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateCenChildInstanceRouteEntryToAttachmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.route_table_id):
            query['RouteTableId'] = request.route_table_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCenChildInstanceRouteEntryToAttachment',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateCenChildInstanceRouteEntryToAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cen_child_instance_route_entry_to_attachment(
        self,
        request: cbn_20170912_models.CreateCenChildInstanceRouteEntryToAttachmentRequest,
    ) -> cbn_20170912_models.CreateCenChildInstanceRouteEntryToAttachmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cen_child_instance_route_entry_to_attachment_with_options(request, runtime)

    async def create_cen_child_instance_route_entry_to_attachment_async(
        self,
        request: cbn_20170912_models.CreateCenChildInstanceRouteEntryToAttachmentRequest,
    ) -> cbn_20170912_models.CreateCenChildInstanceRouteEntryToAttachmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cen_child_instance_route_entry_to_attachment_with_options_async(request, runtime)

    def create_cen_child_instance_route_entry_to_cen_with_options(
        self,
        request: cbn_20170912_models.CreateCenChildInstanceRouteEntryToCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateCenChildInstanceRouteEntryToCenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.child_instance_ali_uid):
            query['ChildInstanceAliUid'] = request.child_instance_ali_uid
        if not UtilClient.is_unset(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not UtilClient.is_unset(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not UtilClient.is_unset(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not UtilClient.is_unset(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.route_table_id):
            query['RouteTableId'] = request.route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCenChildInstanceRouteEntryToCen',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateCenChildInstanceRouteEntryToCenResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cen_child_instance_route_entry_to_cen_with_options_async(
        self,
        request: cbn_20170912_models.CreateCenChildInstanceRouteEntryToCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateCenChildInstanceRouteEntryToCenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.child_instance_ali_uid):
            query['ChildInstanceAliUid'] = request.child_instance_ali_uid
        if not UtilClient.is_unset(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not UtilClient.is_unset(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not UtilClient.is_unset(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not UtilClient.is_unset(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.route_table_id):
            query['RouteTableId'] = request.route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCenChildInstanceRouteEntryToCen',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateCenChildInstanceRouteEntryToCenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cen_child_instance_route_entry_to_cen(
        self,
        request: cbn_20170912_models.CreateCenChildInstanceRouteEntryToCenRequest,
    ) -> cbn_20170912_models.CreateCenChildInstanceRouteEntryToCenResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cen_child_instance_route_entry_to_cen_with_options(request, runtime)

    async def create_cen_child_instance_route_entry_to_cen_async(
        self,
        request: cbn_20170912_models.CreateCenChildInstanceRouteEntryToCenRequest,
    ) -> cbn_20170912_models.CreateCenChildInstanceRouteEntryToCenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cen_child_instance_route_entry_to_cen_with_options_async(request, runtime)

    def create_cen_inter_region_traffic_qos_policy_with_options(
        self,
        request: cbn_20170912_models.CreateCenInterRegionTrafficQosPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateCenInterRegionTrafficQosPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.traffic_qos_policy_description):
            query['TrafficQosPolicyDescription'] = request.traffic_qos_policy_description
        if not UtilClient.is_unset(request.traffic_qos_policy_name):
            query['TrafficQosPolicyName'] = request.traffic_qos_policy_name
        if not UtilClient.is_unset(request.traffic_qos_queues):
            query['TrafficQosQueues'] = request.traffic_qos_queues
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCenInterRegionTrafficQosPolicy',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateCenInterRegionTrafficQosPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cen_inter_region_traffic_qos_policy_with_options_async(
        self,
        request: cbn_20170912_models.CreateCenInterRegionTrafficQosPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateCenInterRegionTrafficQosPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.traffic_qos_policy_description):
            query['TrafficQosPolicyDescription'] = request.traffic_qos_policy_description
        if not UtilClient.is_unset(request.traffic_qos_policy_name):
            query['TrafficQosPolicyName'] = request.traffic_qos_policy_name
        if not UtilClient.is_unset(request.traffic_qos_queues):
            query['TrafficQosQueues'] = request.traffic_qos_queues
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCenInterRegionTrafficQosPolicy',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateCenInterRegionTrafficQosPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cen_inter_region_traffic_qos_policy(
        self,
        request: cbn_20170912_models.CreateCenInterRegionTrafficQosPolicyRequest,
    ) -> cbn_20170912_models.CreateCenInterRegionTrafficQosPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cen_inter_region_traffic_qos_policy_with_options(request, runtime)

    async def create_cen_inter_region_traffic_qos_policy_async(
        self,
        request: cbn_20170912_models.CreateCenInterRegionTrafficQosPolicyRequest,
    ) -> cbn_20170912_models.CreateCenInterRegionTrafficQosPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cen_inter_region_traffic_qos_policy_with_options_async(request, runtime)

    def create_cen_inter_region_traffic_qos_queue_with_options(
        self,
        request: cbn_20170912_models.CreateCenInterRegionTrafficQosQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateCenInterRegionTrafficQosQueueResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.dscps):
            query['Dscps'] = request.dscps
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qos_queue_description):
            query['QosQueueDescription'] = request.qos_queue_description
        if not UtilClient.is_unset(request.qos_queue_name):
            query['QosQueueName'] = request.qos_queue_name
        if not UtilClient.is_unset(request.remain_bandwidth_percent):
            query['RemainBandwidthPercent'] = request.remain_bandwidth_percent
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.traffic_qos_policy_id):
            query['TrafficQosPolicyId'] = request.traffic_qos_policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCenInterRegionTrafficQosQueue',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateCenInterRegionTrafficQosQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cen_inter_region_traffic_qos_queue_with_options_async(
        self,
        request: cbn_20170912_models.CreateCenInterRegionTrafficQosQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateCenInterRegionTrafficQosQueueResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.dscps):
            query['Dscps'] = request.dscps
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qos_queue_description):
            query['QosQueueDescription'] = request.qos_queue_description
        if not UtilClient.is_unset(request.qos_queue_name):
            query['QosQueueName'] = request.qos_queue_name
        if not UtilClient.is_unset(request.remain_bandwidth_percent):
            query['RemainBandwidthPercent'] = request.remain_bandwidth_percent
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.traffic_qos_policy_id):
            query['TrafficQosPolicyId'] = request.traffic_qos_policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCenInterRegionTrafficQosQueue',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateCenInterRegionTrafficQosQueueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cen_inter_region_traffic_qos_queue(
        self,
        request: cbn_20170912_models.CreateCenInterRegionTrafficQosQueueRequest,
    ) -> cbn_20170912_models.CreateCenInterRegionTrafficQosQueueResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cen_inter_region_traffic_qos_queue_with_options(request, runtime)

    async def create_cen_inter_region_traffic_qos_queue_async(
        self,
        request: cbn_20170912_models.CreateCenInterRegionTrafficQosQueueRequest,
    ) -> cbn_20170912_models.CreateCenInterRegionTrafficQosQueueResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cen_inter_region_traffic_qos_queue_with_options_async(request, runtime)

    def create_cen_route_map_with_options(
        self,
        request: cbn_20170912_models.CreateCenRouteMapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateCenRouteMapResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.as_path_match_mode):
            query['AsPathMatchMode'] = request.as_path_match_mode
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.cen_region_id):
            query['CenRegionId'] = request.cen_region_id
        if not UtilClient.is_unset(request.cidr_match_mode):
            query['CidrMatchMode'] = request.cidr_match_mode
        if not UtilClient.is_unset(request.community_match_mode):
            query['CommunityMatchMode'] = request.community_match_mode
        if not UtilClient.is_unset(request.community_operate_mode):
            query['CommunityOperateMode'] = request.community_operate_mode
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination_child_instance_types):
            query['DestinationChildInstanceTypes'] = request.destination_child_instance_types
        if not UtilClient.is_unset(request.destination_cidr_blocks):
            query['DestinationCidrBlocks'] = request.destination_cidr_blocks
        if not UtilClient.is_unset(request.destination_instance_ids):
            query['DestinationInstanceIds'] = request.destination_instance_ids
        if not UtilClient.is_unset(request.destination_instance_ids_reverse_match):
            query['DestinationInstanceIdsReverseMatch'] = request.destination_instance_ids_reverse_match
        if not UtilClient.is_unset(request.destination_route_table_ids):
            query['DestinationRouteTableIds'] = request.destination_route_table_ids
        if not UtilClient.is_unset(request.map_result):
            query['MapResult'] = request.map_result
        if not UtilClient.is_unset(request.match_address_type):
            query['MatchAddressType'] = request.match_address_type
        if not UtilClient.is_unset(request.match_asns):
            query['MatchAsns'] = request.match_asns
        if not UtilClient.is_unset(request.match_community_set):
            query['MatchCommunitySet'] = request.match_community_set
        if not UtilClient.is_unset(request.next_priority):
            query['NextPriority'] = request.next_priority
        if not UtilClient.is_unset(request.operate_community_set):
            query['OperateCommunitySet'] = request.operate_community_set
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.preference):
            query['Preference'] = request.preference
        if not UtilClient.is_unset(request.prepend_as_path):
            query['PrependAsPath'] = request.prepend_as_path
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.route_types):
            query['RouteTypes'] = request.route_types
        if not UtilClient.is_unset(request.source_child_instance_types):
            query['SourceChildInstanceTypes'] = request.source_child_instance_types
        if not UtilClient.is_unset(request.source_instance_ids):
            query['SourceInstanceIds'] = request.source_instance_ids
        if not UtilClient.is_unset(request.source_instance_ids_reverse_match):
            query['SourceInstanceIdsReverseMatch'] = request.source_instance_ids_reverse_match
        if not UtilClient.is_unset(request.source_region_ids):
            query['SourceRegionIds'] = request.source_region_ids
        if not UtilClient.is_unset(request.source_route_table_ids):
            query['SourceRouteTableIds'] = request.source_route_table_ids
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        if not UtilClient.is_unset(request.transmit_direction):
            query['TransmitDirection'] = request.transmit_direction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCenRouteMap',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateCenRouteMapResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cen_route_map_with_options_async(
        self,
        request: cbn_20170912_models.CreateCenRouteMapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateCenRouteMapResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.as_path_match_mode):
            query['AsPathMatchMode'] = request.as_path_match_mode
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.cen_region_id):
            query['CenRegionId'] = request.cen_region_id
        if not UtilClient.is_unset(request.cidr_match_mode):
            query['CidrMatchMode'] = request.cidr_match_mode
        if not UtilClient.is_unset(request.community_match_mode):
            query['CommunityMatchMode'] = request.community_match_mode
        if not UtilClient.is_unset(request.community_operate_mode):
            query['CommunityOperateMode'] = request.community_operate_mode
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination_child_instance_types):
            query['DestinationChildInstanceTypes'] = request.destination_child_instance_types
        if not UtilClient.is_unset(request.destination_cidr_blocks):
            query['DestinationCidrBlocks'] = request.destination_cidr_blocks
        if not UtilClient.is_unset(request.destination_instance_ids):
            query['DestinationInstanceIds'] = request.destination_instance_ids
        if not UtilClient.is_unset(request.destination_instance_ids_reverse_match):
            query['DestinationInstanceIdsReverseMatch'] = request.destination_instance_ids_reverse_match
        if not UtilClient.is_unset(request.destination_route_table_ids):
            query['DestinationRouteTableIds'] = request.destination_route_table_ids
        if not UtilClient.is_unset(request.map_result):
            query['MapResult'] = request.map_result
        if not UtilClient.is_unset(request.match_address_type):
            query['MatchAddressType'] = request.match_address_type
        if not UtilClient.is_unset(request.match_asns):
            query['MatchAsns'] = request.match_asns
        if not UtilClient.is_unset(request.match_community_set):
            query['MatchCommunitySet'] = request.match_community_set
        if not UtilClient.is_unset(request.next_priority):
            query['NextPriority'] = request.next_priority
        if not UtilClient.is_unset(request.operate_community_set):
            query['OperateCommunitySet'] = request.operate_community_set
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.preference):
            query['Preference'] = request.preference
        if not UtilClient.is_unset(request.prepend_as_path):
            query['PrependAsPath'] = request.prepend_as_path
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.route_types):
            query['RouteTypes'] = request.route_types
        if not UtilClient.is_unset(request.source_child_instance_types):
            query['SourceChildInstanceTypes'] = request.source_child_instance_types
        if not UtilClient.is_unset(request.source_instance_ids):
            query['SourceInstanceIds'] = request.source_instance_ids
        if not UtilClient.is_unset(request.source_instance_ids_reverse_match):
            query['SourceInstanceIdsReverseMatch'] = request.source_instance_ids_reverse_match
        if not UtilClient.is_unset(request.source_region_ids):
            query['SourceRegionIds'] = request.source_region_ids
        if not UtilClient.is_unset(request.source_route_table_ids):
            query['SourceRouteTableIds'] = request.source_route_table_ids
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        if not UtilClient.is_unset(request.transmit_direction):
            query['TransmitDirection'] = request.transmit_direction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCenRouteMap',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateCenRouteMapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cen_route_map(
        self,
        request: cbn_20170912_models.CreateCenRouteMapRequest,
    ) -> cbn_20170912_models.CreateCenRouteMapResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cen_route_map_with_options(request, runtime)

    async def create_cen_route_map_async(
        self,
        request: cbn_20170912_models.CreateCenRouteMapRequest,
    ) -> cbn_20170912_models.CreateCenRouteMapResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cen_route_map_with_options_async(request, runtime)

    def create_flowlog_with_options(
        self,
        request: cbn_20170912_models.CreateFlowlogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateFlowlogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.flow_log_name):
            query['FlowLogName'] = request.flow_log_name
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.log_store_name):
            query['LogStoreName'] = request.log_store_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFlowlog',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateFlowlogResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_flowlog_with_options_async(
        self,
        request: cbn_20170912_models.CreateFlowlogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateFlowlogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.flow_log_name):
            query['FlowLogName'] = request.flow_log_name
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.log_store_name):
            query['LogStoreName'] = request.log_store_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFlowlog',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateFlowlogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_flowlog(
        self,
        request: cbn_20170912_models.CreateFlowlogRequest,
    ) -> cbn_20170912_models.CreateFlowlogResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_flowlog_with_options(request, runtime)

    async def create_flowlog_async(
        self,
        request: cbn_20170912_models.CreateFlowlogRequest,
    ) -> cbn_20170912_models.CreateFlowlogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_flowlog_with_options_async(request, runtime)

    def create_traffic_marking_policy_with_options(
        self,
        request: cbn_20170912_models.CreateTrafficMarkingPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateTrafficMarkingPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.marking_dscp):
            query['MarkingDscp'] = request.marking_dscp
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.traffic_marking_policy_description):
            query['TrafficMarkingPolicyDescription'] = request.traffic_marking_policy_description
        if not UtilClient.is_unset(request.traffic_marking_policy_name):
            query['TrafficMarkingPolicyName'] = request.traffic_marking_policy_name
        if not UtilClient.is_unset(request.traffic_match_rules):
            query['TrafficMatchRules'] = request.traffic_match_rules
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTrafficMarkingPolicy',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateTrafficMarkingPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_traffic_marking_policy_with_options_async(
        self,
        request: cbn_20170912_models.CreateTrafficMarkingPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateTrafficMarkingPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.marking_dscp):
            query['MarkingDscp'] = request.marking_dscp
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.traffic_marking_policy_description):
            query['TrafficMarkingPolicyDescription'] = request.traffic_marking_policy_description
        if not UtilClient.is_unset(request.traffic_marking_policy_name):
            query['TrafficMarkingPolicyName'] = request.traffic_marking_policy_name
        if not UtilClient.is_unset(request.traffic_match_rules):
            query['TrafficMatchRules'] = request.traffic_match_rules
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTrafficMarkingPolicy',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateTrafficMarkingPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_traffic_marking_policy(
        self,
        request: cbn_20170912_models.CreateTrafficMarkingPolicyRequest,
    ) -> cbn_20170912_models.CreateTrafficMarkingPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_traffic_marking_policy_with_options(request, runtime)

    async def create_traffic_marking_policy_async(
        self,
        request: cbn_20170912_models.CreateTrafficMarkingPolicyRequest,
    ) -> cbn_20170912_models.CreateTrafficMarkingPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_traffic_marking_policy_with_options_async(request, runtime)

    def create_transit_router_with_options(
        self,
        tmp_req: cbn_20170912_models.CreateTransitRouterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateTransitRouterResponse:
        UtilClient.validate_model(tmp_req)
        request = cbn_20170912_models.CreateTransitRouterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.transit_router_cidr_list):
            request.transit_router_cidr_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.transit_router_cidr_list, 'TransitRouterCidrList', 'json')
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.support_multicast):
            query['SupportMulticast'] = request.support_multicast
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.transit_router_cidr_list_shrink):
            query['TransitRouterCidrList'] = request.transit_router_cidr_list_shrink
        if not UtilClient.is_unset(request.transit_router_description):
            query['TransitRouterDescription'] = request.transit_router_description
        if not UtilClient.is_unset(request.transit_router_name):
            query['TransitRouterName'] = request.transit_router_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTransitRouter',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateTransitRouterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_transit_router_with_options_async(
        self,
        tmp_req: cbn_20170912_models.CreateTransitRouterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateTransitRouterResponse:
        UtilClient.validate_model(tmp_req)
        request = cbn_20170912_models.CreateTransitRouterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.transit_router_cidr_list):
            request.transit_router_cidr_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.transit_router_cidr_list, 'TransitRouterCidrList', 'json')
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.support_multicast):
            query['SupportMulticast'] = request.support_multicast
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.transit_router_cidr_list_shrink):
            query['TransitRouterCidrList'] = request.transit_router_cidr_list_shrink
        if not UtilClient.is_unset(request.transit_router_description):
            query['TransitRouterDescription'] = request.transit_router_description
        if not UtilClient.is_unset(request.transit_router_name):
            query['TransitRouterName'] = request.transit_router_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTransitRouter',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateTransitRouterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_transit_router(
        self,
        request: cbn_20170912_models.CreateTransitRouterRequest,
    ) -> cbn_20170912_models.CreateTransitRouterResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_transit_router_with_options(request, runtime)

    async def create_transit_router_async(
        self,
        request: cbn_20170912_models.CreateTransitRouterRequest,
    ) -> cbn_20170912_models.CreateTransitRouterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_transit_router_with_options_async(request, runtime)

    def create_transit_router_cidr_with_options(
        self,
        request: cbn_20170912_models.CreateTransitRouterCidrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateTransitRouterCidrResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cidr):
            query['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.publish_cidr_route):
            query['PublishCidrRoute'] = request.publish_cidr_route
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTransitRouterCidr',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateTransitRouterCidrResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_transit_router_cidr_with_options_async(
        self,
        request: cbn_20170912_models.CreateTransitRouterCidrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateTransitRouterCidrResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cidr):
            query['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.publish_cidr_route):
            query['PublishCidrRoute'] = request.publish_cidr_route
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTransitRouterCidr',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateTransitRouterCidrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_transit_router_cidr(
        self,
        request: cbn_20170912_models.CreateTransitRouterCidrRequest,
    ) -> cbn_20170912_models.CreateTransitRouterCidrResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_transit_router_cidr_with_options(request, runtime)

    async def create_transit_router_cidr_async(
        self,
        request: cbn_20170912_models.CreateTransitRouterCidrRequest,
    ) -> cbn_20170912_models.CreateTransitRouterCidrResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_transit_router_cidr_with_options_async(request, runtime)

    def create_transit_router_multicast_domain_with_options(
        self,
        request: cbn_20170912_models.CreateTransitRouterMulticastDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateTransitRouterMulticastDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not UtilClient.is_unset(request.transit_router_multicast_domain_description):
            query['TransitRouterMulticastDomainDescription'] = request.transit_router_multicast_domain_description
        if not UtilClient.is_unset(request.transit_router_multicast_domain_name):
            query['TransitRouterMulticastDomainName'] = request.transit_router_multicast_domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTransitRouterMulticastDomain',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateTransitRouterMulticastDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_transit_router_multicast_domain_with_options_async(
        self,
        request: cbn_20170912_models.CreateTransitRouterMulticastDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateTransitRouterMulticastDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not UtilClient.is_unset(request.transit_router_multicast_domain_description):
            query['TransitRouterMulticastDomainDescription'] = request.transit_router_multicast_domain_description
        if not UtilClient.is_unset(request.transit_router_multicast_domain_name):
            query['TransitRouterMulticastDomainName'] = request.transit_router_multicast_domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTransitRouterMulticastDomain',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateTransitRouterMulticastDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_transit_router_multicast_domain(
        self,
        request: cbn_20170912_models.CreateTransitRouterMulticastDomainRequest,
    ) -> cbn_20170912_models.CreateTransitRouterMulticastDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_transit_router_multicast_domain_with_options(request, runtime)

    async def create_transit_router_multicast_domain_async(
        self,
        request: cbn_20170912_models.CreateTransitRouterMulticastDomainRequest,
    ) -> cbn_20170912_models.CreateTransitRouterMulticastDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_transit_router_multicast_domain_with_options_async(request, runtime)

    def create_transit_router_peer_attachment_with_options(
        self,
        request: cbn_20170912_models.CreateTransitRouterPeerAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateTransitRouterPeerAttachmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_publish_route_enabled):
            query['AutoPublishRouteEnabled'] = request.auto_publish_route_enabled
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.bandwidth_type):
            query['BandwidthType'] = request.bandwidth_type
        if not UtilClient.is_unset(request.cen_bandwidth_package_id):
            query['CenBandwidthPackageId'] = request.cen_bandwidth_package_id
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.peer_transit_router_id):
            query['PeerTransitRouterId'] = request.peer_transit_router_id
        if not UtilClient.is_unset(request.peer_transit_router_region_id):
            query['PeerTransitRouterRegionId'] = request.peer_transit_router_region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not UtilClient.is_unset(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTransitRouterPeerAttachment',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateTransitRouterPeerAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_transit_router_peer_attachment_with_options_async(
        self,
        request: cbn_20170912_models.CreateTransitRouterPeerAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateTransitRouterPeerAttachmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_publish_route_enabled):
            query['AutoPublishRouteEnabled'] = request.auto_publish_route_enabled
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.bandwidth_type):
            query['BandwidthType'] = request.bandwidth_type
        if not UtilClient.is_unset(request.cen_bandwidth_package_id):
            query['CenBandwidthPackageId'] = request.cen_bandwidth_package_id
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.peer_transit_router_id):
            query['PeerTransitRouterId'] = request.peer_transit_router_id
        if not UtilClient.is_unset(request.peer_transit_router_region_id):
            query['PeerTransitRouterRegionId'] = request.peer_transit_router_region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not UtilClient.is_unset(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTransitRouterPeerAttachment',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateTransitRouterPeerAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_transit_router_peer_attachment(
        self,
        request: cbn_20170912_models.CreateTransitRouterPeerAttachmentRequest,
    ) -> cbn_20170912_models.CreateTransitRouterPeerAttachmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_transit_router_peer_attachment_with_options(request, runtime)

    async def create_transit_router_peer_attachment_async(
        self,
        request: cbn_20170912_models.CreateTransitRouterPeerAttachmentRequest,
    ) -> cbn_20170912_models.CreateTransitRouterPeerAttachmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_transit_router_peer_attachment_with_options_async(request, runtime)

    def create_transit_router_prefix_list_association_with_options(
        self,
        request: cbn_20170912_models.CreateTransitRouterPrefixListAssociationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateTransitRouterPrefixListAssociationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.next_hop):
            query['NextHop'] = request.next_hop
        if not UtilClient.is_unset(request.next_hop_type):
            query['NextHopType'] = request.next_hop_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_uid):
            query['OwnerUid'] = request.owner_uid
        if not UtilClient.is_unset(request.prefix_list_id):
            query['PrefixListId'] = request.prefix_list_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not UtilClient.is_unset(request.transit_router_table_id):
            query['TransitRouterTableId'] = request.transit_router_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTransitRouterPrefixListAssociation',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateTransitRouterPrefixListAssociationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_transit_router_prefix_list_association_with_options_async(
        self,
        request: cbn_20170912_models.CreateTransitRouterPrefixListAssociationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateTransitRouterPrefixListAssociationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.next_hop):
            query['NextHop'] = request.next_hop
        if not UtilClient.is_unset(request.next_hop_type):
            query['NextHopType'] = request.next_hop_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_uid):
            query['OwnerUid'] = request.owner_uid
        if not UtilClient.is_unset(request.prefix_list_id):
            query['PrefixListId'] = request.prefix_list_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not UtilClient.is_unset(request.transit_router_table_id):
            query['TransitRouterTableId'] = request.transit_router_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTransitRouterPrefixListAssociation',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateTransitRouterPrefixListAssociationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_transit_router_prefix_list_association(
        self,
        request: cbn_20170912_models.CreateTransitRouterPrefixListAssociationRequest,
    ) -> cbn_20170912_models.CreateTransitRouterPrefixListAssociationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_transit_router_prefix_list_association_with_options(request, runtime)

    async def create_transit_router_prefix_list_association_async(
        self,
        request: cbn_20170912_models.CreateTransitRouterPrefixListAssociationRequest,
    ) -> cbn_20170912_models.CreateTransitRouterPrefixListAssociationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_transit_router_prefix_list_association_with_options_async(request, runtime)

    def create_transit_router_route_entry_with_options(
        self,
        request: cbn_20170912_models.CreateTransitRouterRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateTransitRouterRouteEntryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_route_entry_description):
            query['TransitRouterRouteEntryDescription'] = request.transit_router_route_entry_description
        if not UtilClient.is_unset(request.transit_router_route_entry_destination_cidr_block):
            query['TransitRouterRouteEntryDestinationCidrBlock'] = request.transit_router_route_entry_destination_cidr_block
        if not UtilClient.is_unset(request.transit_router_route_entry_name):
            query['TransitRouterRouteEntryName'] = request.transit_router_route_entry_name
        if not UtilClient.is_unset(request.transit_router_route_entry_next_hop_id):
            query['TransitRouterRouteEntryNextHopId'] = request.transit_router_route_entry_next_hop_id
        if not UtilClient.is_unset(request.transit_router_route_entry_next_hop_type):
            query['TransitRouterRouteEntryNextHopType'] = request.transit_router_route_entry_next_hop_type
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTransitRouterRouteEntry',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateTransitRouterRouteEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_transit_router_route_entry_with_options_async(
        self,
        request: cbn_20170912_models.CreateTransitRouterRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateTransitRouterRouteEntryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_route_entry_description):
            query['TransitRouterRouteEntryDescription'] = request.transit_router_route_entry_description
        if not UtilClient.is_unset(request.transit_router_route_entry_destination_cidr_block):
            query['TransitRouterRouteEntryDestinationCidrBlock'] = request.transit_router_route_entry_destination_cidr_block
        if not UtilClient.is_unset(request.transit_router_route_entry_name):
            query['TransitRouterRouteEntryName'] = request.transit_router_route_entry_name
        if not UtilClient.is_unset(request.transit_router_route_entry_next_hop_id):
            query['TransitRouterRouteEntryNextHopId'] = request.transit_router_route_entry_next_hop_id
        if not UtilClient.is_unset(request.transit_router_route_entry_next_hop_type):
            query['TransitRouterRouteEntryNextHopType'] = request.transit_router_route_entry_next_hop_type
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTransitRouterRouteEntry',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateTransitRouterRouteEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_transit_router_route_entry(
        self,
        request: cbn_20170912_models.CreateTransitRouterRouteEntryRequest,
    ) -> cbn_20170912_models.CreateTransitRouterRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_transit_router_route_entry_with_options(request, runtime)

    async def create_transit_router_route_entry_async(
        self,
        request: cbn_20170912_models.CreateTransitRouterRouteEntryRequest,
    ) -> cbn_20170912_models.CreateTransitRouterRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_transit_router_route_entry_with_options_async(request, runtime)

    def create_transit_router_route_table_with_options(
        self,
        request: cbn_20170912_models.CreateTransitRouterRouteTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateTransitRouterRouteTableResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not UtilClient.is_unset(request.transit_router_route_table_description):
            query['TransitRouterRouteTableDescription'] = request.transit_router_route_table_description
        if not UtilClient.is_unset(request.transit_router_route_table_name):
            query['TransitRouterRouteTableName'] = request.transit_router_route_table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTransitRouterRouteTable',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateTransitRouterRouteTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_transit_router_route_table_with_options_async(
        self,
        request: cbn_20170912_models.CreateTransitRouterRouteTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateTransitRouterRouteTableResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not UtilClient.is_unset(request.transit_router_route_table_description):
            query['TransitRouterRouteTableDescription'] = request.transit_router_route_table_description
        if not UtilClient.is_unset(request.transit_router_route_table_name):
            query['TransitRouterRouteTableName'] = request.transit_router_route_table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTransitRouterRouteTable',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateTransitRouterRouteTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_transit_router_route_table(
        self,
        request: cbn_20170912_models.CreateTransitRouterRouteTableRequest,
    ) -> cbn_20170912_models.CreateTransitRouterRouteTableResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_transit_router_route_table_with_options(request, runtime)

    async def create_transit_router_route_table_async(
        self,
        request: cbn_20170912_models.CreateTransitRouterRouteTableRequest,
    ) -> cbn_20170912_models.CreateTransitRouterRouteTableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_transit_router_route_table_with_options_async(request, runtime)

    def create_transit_router_vbr_attachment_with_options(
        self,
        request: cbn_20170912_models.CreateTransitRouterVbrAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateTransitRouterVbrAttachmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_publish_route_enabled):
            query['AutoPublishRouteEnabled'] = request.auto_publish_route_enabled
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not UtilClient.is_unset(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not UtilClient.is_unset(request.vbr_id):
            query['VbrId'] = request.vbr_id
        if not UtilClient.is_unset(request.vbr_owner_id):
            query['VbrOwnerId'] = request.vbr_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTransitRouterVbrAttachment',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateTransitRouterVbrAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_transit_router_vbr_attachment_with_options_async(
        self,
        request: cbn_20170912_models.CreateTransitRouterVbrAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateTransitRouterVbrAttachmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_publish_route_enabled):
            query['AutoPublishRouteEnabled'] = request.auto_publish_route_enabled
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not UtilClient.is_unset(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not UtilClient.is_unset(request.vbr_id):
            query['VbrId'] = request.vbr_id
        if not UtilClient.is_unset(request.vbr_owner_id):
            query['VbrOwnerId'] = request.vbr_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTransitRouterVbrAttachment',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateTransitRouterVbrAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_transit_router_vbr_attachment(
        self,
        request: cbn_20170912_models.CreateTransitRouterVbrAttachmentRequest,
    ) -> cbn_20170912_models.CreateTransitRouterVbrAttachmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_transit_router_vbr_attachment_with_options(request, runtime)

    async def create_transit_router_vbr_attachment_async(
        self,
        request: cbn_20170912_models.CreateTransitRouterVbrAttachmentRequest,
    ) -> cbn_20170912_models.CreateTransitRouterVbrAttachmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_transit_router_vbr_attachment_with_options_async(request, runtime)

    def create_transit_router_vpc_attachment_with_options(
        self,
        request: cbn_20170912_models.CreateTransitRouterVpcAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateTransitRouterVpcAttachmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not UtilClient.is_unset(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpc_owner_id):
            query['VpcOwnerId'] = request.vpc_owner_id
        if not UtilClient.is_unset(request.zone_mappings):
            query['ZoneMappings'] = request.zone_mappings
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTransitRouterVpcAttachment',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateTransitRouterVpcAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_transit_router_vpc_attachment_with_options_async(
        self,
        request: cbn_20170912_models.CreateTransitRouterVpcAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateTransitRouterVpcAttachmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not UtilClient.is_unset(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpc_owner_id):
            query['VpcOwnerId'] = request.vpc_owner_id
        if not UtilClient.is_unset(request.zone_mappings):
            query['ZoneMappings'] = request.zone_mappings
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTransitRouterVpcAttachment',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateTransitRouterVpcAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_transit_router_vpc_attachment(
        self,
        request: cbn_20170912_models.CreateTransitRouterVpcAttachmentRequest,
    ) -> cbn_20170912_models.CreateTransitRouterVpcAttachmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_transit_router_vpc_attachment_with_options(request, runtime)

    async def create_transit_router_vpc_attachment_async(
        self,
        request: cbn_20170912_models.CreateTransitRouterVpcAttachmentRequest,
    ) -> cbn_20170912_models.CreateTransitRouterVpcAttachmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_transit_router_vpc_attachment_with_options_async(request, runtime)

    def create_transit_router_vpn_attachment_with_options(
        self,
        request: cbn_20170912_models.CreateTransitRouterVpnAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateTransitRouterVpnAttachmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_publish_route_enabled):
            query['AutoPublishRouteEnabled'] = request.auto_publish_route_enabled
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not UtilClient.is_unset(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not UtilClient.is_unset(request.vpn_id):
            query['VpnId'] = request.vpn_id
        if not UtilClient.is_unset(request.vpn_owner_id):
            query['VpnOwnerId'] = request.vpn_owner_id
        if not UtilClient.is_unset(request.zone):
            query['Zone'] = request.zone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTransitRouterVpnAttachment',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateTransitRouterVpnAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_transit_router_vpn_attachment_with_options_async(
        self,
        request: cbn_20170912_models.CreateTransitRouterVpnAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateTransitRouterVpnAttachmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_publish_route_enabled):
            query['AutoPublishRouteEnabled'] = request.auto_publish_route_enabled
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not UtilClient.is_unset(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not UtilClient.is_unset(request.vpn_id):
            query['VpnId'] = request.vpn_id
        if not UtilClient.is_unset(request.vpn_owner_id):
            query['VpnOwnerId'] = request.vpn_owner_id
        if not UtilClient.is_unset(request.zone):
            query['Zone'] = request.zone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTransitRouterVpnAttachment',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateTransitRouterVpnAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_transit_router_vpn_attachment(
        self,
        request: cbn_20170912_models.CreateTransitRouterVpnAttachmentRequest,
    ) -> cbn_20170912_models.CreateTransitRouterVpnAttachmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_transit_router_vpn_attachment_with_options(request, runtime)

    async def create_transit_router_vpn_attachment_async(
        self,
        request: cbn_20170912_models.CreateTransitRouterVpnAttachmentRequest,
    ) -> cbn_20170912_models.CreateTransitRouterVpnAttachmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_transit_router_vpn_attachment_with_options_async(request, runtime)

    def deactive_flow_log_with_options(
        self,
        request: cbn_20170912_models.DeactiveFlowLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeactiveFlowLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeactiveFlowLog',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeactiveFlowLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def deactive_flow_log_with_options_async(
        self,
        request: cbn_20170912_models.DeactiveFlowLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeactiveFlowLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeactiveFlowLog',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeactiveFlowLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deactive_flow_log(
        self,
        request: cbn_20170912_models.DeactiveFlowLogRequest,
    ) -> cbn_20170912_models.DeactiveFlowLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.deactive_flow_log_with_options(request, runtime)

    async def deactive_flow_log_async(
        self,
        request: cbn_20170912_models.DeactiveFlowLogRequest,
    ) -> cbn_20170912_models.DeactiveFlowLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deactive_flow_log_with_options_async(request, runtime)

    def delete_cen_with_options(
        self,
        request: cbn_20170912_models.DeleteCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteCenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCen',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteCenResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cen_with_options_async(
        self,
        request: cbn_20170912_models.DeleteCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteCenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCen',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteCenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cen(
        self,
        request: cbn_20170912_models.DeleteCenRequest,
    ) -> cbn_20170912_models.DeleteCenResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_cen_with_options(request, runtime)

    async def delete_cen_async(
        self,
        request: cbn_20170912_models.DeleteCenRequest,
    ) -> cbn_20170912_models.DeleteCenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cen_with_options_async(request, runtime)

    def delete_cen_bandwidth_package_with_options(
        self,
        request: cbn_20170912_models.DeleteCenBandwidthPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteCenBandwidthPackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_bandwidth_package_id):
            query['CenBandwidthPackageId'] = request.cen_bandwidth_package_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCenBandwidthPackage',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteCenBandwidthPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cen_bandwidth_package_with_options_async(
        self,
        request: cbn_20170912_models.DeleteCenBandwidthPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteCenBandwidthPackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_bandwidth_package_id):
            query['CenBandwidthPackageId'] = request.cen_bandwidth_package_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCenBandwidthPackage',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteCenBandwidthPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cen_bandwidth_package(
        self,
        request: cbn_20170912_models.DeleteCenBandwidthPackageRequest,
    ) -> cbn_20170912_models.DeleteCenBandwidthPackageResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_cen_bandwidth_package_with_options(request, runtime)

    async def delete_cen_bandwidth_package_async(
        self,
        request: cbn_20170912_models.DeleteCenBandwidthPackageRequest,
    ) -> cbn_20170912_models.DeleteCenBandwidthPackageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cen_bandwidth_package_with_options_async(request, runtime)

    def delete_cen_child_instance_route_entry_to_attachment_with_options(
        self,
        request: cbn_20170912_models.DeleteCenChildInstanceRouteEntryToAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteCenChildInstanceRouteEntryToAttachmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.route_table_id):
            query['RouteTableId'] = request.route_table_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCenChildInstanceRouteEntryToAttachment',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteCenChildInstanceRouteEntryToAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cen_child_instance_route_entry_to_attachment_with_options_async(
        self,
        request: cbn_20170912_models.DeleteCenChildInstanceRouteEntryToAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteCenChildInstanceRouteEntryToAttachmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.route_table_id):
            query['RouteTableId'] = request.route_table_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCenChildInstanceRouteEntryToAttachment',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteCenChildInstanceRouteEntryToAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cen_child_instance_route_entry_to_attachment(
        self,
        request: cbn_20170912_models.DeleteCenChildInstanceRouteEntryToAttachmentRequest,
    ) -> cbn_20170912_models.DeleteCenChildInstanceRouteEntryToAttachmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_cen_child_instance_route_entry_to_attachment_with_options(request, runtime)

    async def delete_cen_child_instance_route_entry_to_attachment_async(
        self,
        request: cbn_20170912_models.DeleteCenChildInstanceRouteEntryToAttachmentRequest,
    ) -> cbn_20170912_models.DeleteCenChildInstanceRouteEntryToAttachmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cen_child_instance_route_entry_to_attachment_with_options_async(request, runtime)

    def delete_cen_child_instance_route_entry_to_cen_with_options(
        self,
        request: cbn_20170912_models.DeleteCenChildInstanceRouteEntryToCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteCenChildInstanceRouteEntryToCenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.child_instance_ali_uid):
            query['ChildInstanceAliUid'] = request.child_instance_ali_uid
        if not UtilClient.is_unset(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not UtilClient.is_unset(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not UtilClient.is_unset(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not UtilClient.is_unset(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.route_table_id):
            query['RouteTableId'] = request.route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCenChildInstanceRouteEntryToCen',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteCenChildInstanceRouteEntryToCenResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cen_child_instance_route_entry_to_cen_with_options_async(
        self,
        request: cbn_20170912_models.DeleteCenChildInstanceRouteEntryToCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteCenChildInstanceRouteEntryToCenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.child_instance_ali_uid):
            query['ChildInstanceAliUid'] = request.child_instance_ali_uid
        if not UtilClient.is_unset(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not UtilClient.is_unset(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not UtilClient.is_unset(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not UtilClient.is_unset(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.route_table_id):
            query['RouteTableId'] = request.route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCenChildInstanceRouteEntryToCen',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteCenChildInstanceRouteEntryToCenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cen_child_instance_route_entry_to_cen(
        self,
        request: cbn_20170912_models.DeleteCenChildInstanceRouteEntryToCenRequest,
    ) -> cbn_20170912_models.DeleteCenChildInstanceRouteEntryToCenResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_cen_child_instance_route_entry_to_cen_with_options(request, runtime)

    async def delete_cen_child_instance_route_entry_to_cen_async(
        self,
        request: cbn_20170912_models.DeleteCenChildInstanceRouteEntryToCenRequest,
    ) -> cbn_20170912_models.DeleteCenChildInstanceRouteEntryToCenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cen_child_instance_route_entry_to_cen_with_options_async(request, runtime)

    def delete_cen_inter_region_traffic_qos_policy_with_options(
        self,
        request: cbn_20170912_models.DeleteCenInterRegionTrafficQosPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteCenInterRegionTrafficQosPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.traffic_qos_policy_id):
            query['TrafficQosPolicyId'] = request.traffic_qos_policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCenInterRegionTrafficQosPolicy',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteCenInterRegionTrafficQosPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cen_inter_region_traffic_qos_policy_with_options_async(
        self,
        request: cbn_20170912_models.DeleteCenInterRegionTrafficQosPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteCenInterRegionTrafficQosPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.traffic_qos_policy_id):
            query['TrafficQosPolicyId'] = request.traffic_qos_policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCenInterRegionTrafficQosPolicy',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteCenInterRegionTrafficQosPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cen_inter_region_traffic_qos_policy(
        self,
        request: cbn_20170912_models.DeleteCenInterRegionTrafficQosPolicyRequest,
    ) -> cbn_20170912_models.DeleteCenInterRegionTrafficQosPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_cen_inter_region_traffic_qos_policy_with_options(request, runtime)

    async def delete_cen_inter_region_traffic_qos_policy_async(
        self,
        request: cbn_20170912_models.DeleteCenInterRegionTrafficQosPolicyRequest,
    ) -> cbn_20170912_models.DeleteCenInterRegionTrafficQosPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cen_inter_region_traffic_qos_policy_with_options_async(request, runtime)

    def delete_cen_inter_region_traffic_qos_queue_with_options(
        self,
        request: cbn_20170912_models.DeleteCenInterRegionTrafficQosQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteCenInterRegionTrafficQosQueueResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qos_queue_id):
            query['QosQueueId'] = request.qos_queue_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCenInterRegionTrafficQosQueue',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteCenInterRegionTrafficQosQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cen_inter_region_traffic_qos_queue_with_options_async(
        self,
        request: cbn_20170912_models.DeleteCenInterRegionTrafficQosQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteCenInterRegionTrafficQosQueueResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qos_queue_id):
            query['QosQueueId'] = request.qos_queue_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCenInterRegionTrafficQosQueue',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteCenInterRegionTrafficQosQueueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cen_inter_region_traffic_qos_queue(
        self,
        request: cbn_20170912_models.DeleteCenInterRegionTrafficQosQueueRequest,
    ) -> cbn_20170912_models.DeleteCenInterRegionTrafficQosQueueResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_cen_inter_region_traffic_qos_queue_with_options(request, runtime)

    async def delete_cen_inter_region_traffic_qos_queue_async(
        self,
        request: cbn_20170912_models.DeleteCenInterRegionTrafficQosQueueRequest,
    ) -> cbn_20170912_models.DeleteCenInterRegionTrafficQosQueueResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cen_inter_region_traffic_qos_queue_with_options_async(request, runtime)

    def delete_cen_route_map_with_options(
        self,
        request: cbn_20170912_models.DeleteCenRouteMapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteCenRouteMapResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.cen_region_id):
            query['CenRegionId'] = request.cen_region_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.route_map_id):
            query['RouteMapId'] = request.route_map_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCenRouteMap',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteCenRouteMapResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cen_route_map_with_options_async(
        self,
        request: cbn_20170912_models.DeleteCenRouteMapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteCenRouteMapResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.cen_region_id):
            query['CenRegionId'] = request.cen_region_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.route_map_id):
            query['RouteMapId'] = request.route_map_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCenRouteMap',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteCenRouteMapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cen_route_map(
        self,
        request: cbn_20170912_models.DeleteCenRouteMapRequest,
    ) -> cbn_20170912_models.DeleteCenRouteMapResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_cen_route_map_with_options(request, runtime)

    async def delete_cen_route_map_async(
        self,
        request: cbn_20170912_models.DeleteCenRouteMapRequest,
    ) -> cbn_20170912_models.DeleteCenRouteMapResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cen_route_map_with_options_async(request, runtime)

    def delete_flowlog_with_options(
        self,
        request: cbn_20170912_models.DeleteFlowlogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteFlowlogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFlowlog',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteFlowlogResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_flowlog_with_options_async(
        self,
        request: cbn_20170912_models.DeleteFlowlogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteFlowlogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFlowlog',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteFlowlogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_flowlog(
        self,
        request: cbn_20170912_models.DeleteFlowlogRequest,
    ) -> cbn_20170912_models.DeleteFlowlogResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_flowlog_with_options(request, runtime)

    async def delete_flowlog_async(
        self,
        request: cbn_20170912_models.DeleteFlowlogRequest,
    ) -> cbn_20170912_models.DeleteFlowlogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_flowlog_with_options_async(request, runtime)

    def delete_route_service_in_cen_with_options(
        self,
        request: cbn_20170912_models.DeleteRouteServiceInCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteRouteServiceInCenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_region_id):
            query['AccessRegionId'] = request.access_region_id
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.host):
            query['Host'] = request.host
        if not UtilClient.is_unset(request.host_region_id):
            query['HostRegionId'] = request.host_region_id
        if not UtilClient.is_unset(request.host_vpc_id):
            query['HostVpcId'] = request.host_vpc_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRouteServiceInCen',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteRouteServiceInCenResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_route_service_in_cen_with_options_async(
        self,
        request: cbn_20170912_models.DeleteRouteServiceInCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteRouteServiceInCenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_region_id):
            query['AccessRegionId'] = request.access_region_id
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.host):
            query['Host'] = request.host
        if not UtilClient.is_unset(request.host_region_id):
            query['HostRegionId'] = request.host_region_id
        if not UtilClient.is_unset(request.host_vpc_id):
            query['HostVpcId'] = request.host_vpc_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRouteServiceInCen',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteRouteServiceInCenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_route_service_in_cen(
        self,
        request: cbn_20170912_models.DeleteRouteServiceInCenRequest,
    ) -> cbn_20170912_models.DeleteRouteServiceInCenResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_route_service_in_cen_with_options(request, runtime)

    async def delete_route_service_in_cen_async(
        self,
        request: cbn_20170912_models.DeleteRouteServiceInCenRequest,
    ) -> cbn_20170912_models.DeleteRouteServiceInCenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_route_service_in_cen_with_options_async(request, runtime)

    def delete_traffic_marking_policy_with_options(
        self,
        request: cbn_20170912_models.DeleteTrafficMarkingPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteTrafficMarkingPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.traffic_marking_policy_id):
            query['TrafficMarkingPolicyId'] = request.traffic_marking_policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTrafficMarkingPolicy',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteTrafficMarkingPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_traffic_marking_policy_with_options_async(
        self,
        request: cbn_20170912_models.DeleteTrafficMarkingPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteTrafficMarkingPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.traffic_marking_policy_id):
            query['TrafficMarkingPolicyId'] = request.traffic_marking_policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTrafficMarkingPolicy',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteTrafficMarkingPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_traffic_marking_policy(
        self,
        request: cbn_20170912_models.DeleteTrafficMarkingPolicyRequest,
    ) -> cbn_20170912_models.DeleteTrafficMarkingPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_traffic_marking_policy_with_options(request, runtime)

    async def delete_traffic_marking_policy_async(
        self,
        request: cbn_20170912_models.DeleteTrafficMarkingPolicyRequest,
    ) -> cbn_20170912_models.DeleteTrafficMarkingPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_traffic_marking_policy_with_options_async(request, runtime)

    def delete_transit_router_with_options(
        self,
        request: cbn_20170912_models.DeleteTransitRouterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteTransitRouterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTransitRouter',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteTransitRouterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_transit_router_with_options_async(
        self,
        request: cbn_20170912_models.DeleteTransitRouterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteTransitRouterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTransitRouter',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteTransitRouterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_transit_router(
        self,
        request: cbn_20170912_models.DeleteTransitRouterRequest,
    ) -> cbn_20170912_models.DeleteTransitRouterResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_transit_router_with_options(request, runtime)

    async def delete_transit_router_async(
        self,
        request: cbn_20170912_models.DeleteTransitRouterRequest,
    ) -> cbn_20170912_models.DeleteTransitRouterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_transit_router_with_options_async(request, runtime)

    def delete_transit_router_cidr_with_options(
        self,
        request: cbn_20170912_models.DeleteTransitRouterCidrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteTransitRouterCidrResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_cidr_id):
            query['TransitRouterCidrId'] = request.transit_router_cidr_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTransitRouterCidr',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteTransitRouterCidrResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_transit_router_cidr_with_options_async(
        self,
        request: cbn_20170912_models.DeleteTransitRouterCidrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteTransitRouterCidrResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_cidr_id):
            query['TransitRouterCidrId'] = request.transit_router_cidr_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTransitRouterCidr',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteTransitRouterCidrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_transit_router_cidr(
        self,
        request: cbn_20170912_models.DeleteTransitRouterCidrRequest,
    ) -> cbn_20170912_models.DeleteTransitRouterCidrResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_transit_router_cidr_with_options(request, runtime)

    async def delete_transit_router_cidr_async(
        self,
        request: cbn_20170912_models.DeleteTransitRouterCidrRequest,
    ) -> cbn_20170912_models.DeleteTransitRouterCidrResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_transit_router_cidr_with_options_async(request, runtime)

    def delete_transit_router_multicast_domain_with_options(
        self,
        request: cbn_20170912_models.DeleteTransitRouterMulticastDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteTransitRouterMulticastDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTransitRouterMulticastDomain',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteTransitRouterMulticastDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_transit_router_multicast_domain_with_options_async(
        self,
        request: cbn_20170912_models.DeleteTransitRouterMulticastDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteTransitRouterMulticastDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTransitRouterMulticastDomain',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteTransitRouterMulticastDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_transit_router_multicast_domain(
        self,
        request: cbn_20170912_models.DeleteTransitRouterMulticastDomainRequest,
    ) -> cbn_20170912_models.DeleteTransitRouterMulticastDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_transit_router_multicast_domain_with_options(request, runtime)

    async def delete_transit_router_multicast_domain_async(
        self,
        request: cbn_20170912_models.DeleteTransitRouterMulticastDomainRequest,
    ) -> cbn_20170912_models.DeleteTransitRouterMulticastDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_transit_router_multicast_domain_with_options_async(request, runtime)

    def delete_transit_router_peer_attachment_with_options(
        self,
        request: cbn_20170912_models.DeleteTransitRouterPeerAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteTransitRouterPeerAttachmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTransitRouterPeerAttachment',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteTransitRouterPeerAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_transit_router_peer_attachment_with_options_async(
        self,
        request: cbn_20170912_models.DeleteTransitRouterPeerAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteTransitRouterPeerAttachmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTransitRouterPeerAttachment',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteTransitRouterPeerAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_transit_router_peer_attachment(
        self,
        request: cbn_20170912_models.DeleteTransitRouterPeerAttachmentRequest,
    ) -> cbn_20170912_models.DeleteTransitRouterPeerAttachmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_transit_router_peer_attachment_with_options(request, runtime)

    async def delete_transit_router_peer_attachment_async(
        self,
        request: cbn_20170912_models.DeleteTransitRouterPeerAttachmentRequest,
    ) -> cbn_20170912_models.DeleteTransitRouterPeerAttachmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_transit_router_peer_attachment_with_options_async(request, runtime)

    def delete_transit_router_prefix_list_association_with_options(
        self,
        request: cbn_20170912_models.DeleteTransitRouterPrefixListAssociationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteTransitRouterPrefixListAssociationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.next_hop):
            query['NextHop'] = request.next_hop
        if not UtilClient.is_unset(request.next_hop_type):
            query['NextHopType'] = request.next_hop_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prefix_list_id):
            query['PrefixListId'] = request.prefix_list_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not UtilClient.is_unset(request.transit_router_table_id):
            query['TransitRouterTableId'] = request.transit_router_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTransitRouterPrefixListAssociation',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteTransitRouterPrefixListAssociationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_transit_router_prefix_list_association_with_options_async(
        self,
        request: cbn_20170912_models.DeleteTransitRouterPrefixListAssociationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteTransitRouterPrefixListAssociationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.next_hop):
            query['NextHop'] = request.next_hop
        if not UtilClient.is_unset(request.next_hop_type):
            query['NextHopType'] = request.next_hop_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prefix_list_id):
            query['PrefixListId'] = request.prefix_list_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not UtilClient.is_unset(request.transit_router_table_id):
            query['TransitRouterTableId'] = request.transit_router_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTransitRouterPrefixListAssociation',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteTransitRouterPrefixListAssociationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_transit_router_prefix_list_association(
        self,
        request: cbn_20170912_models.DeleteTransitRouterPrefixListAssociationRequest,
    ) -> cbn_20170912_models.DeleteTransitRouterPrefixListAssociationResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_transit_router_prefix_list_association_with_options(request, runtime)

    async def delete_transit_router_prefix_list_association_async(
        self,
        request: cbn_20170912_models.DeleteTransitRouterPrefixListAssociationRequest,
    ) -> cbn_20170912_models.DeleteTransitRouterPrefixListAssociationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_transit_router_prefix_list_association_with_options_async(request, runtime)

    def delete_transit_router_route_entry_with_options(
        self,
        request: cbn_20170912_models.DeleteTransitRouterRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteTransitRouterRouteEntryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_route_entry_destination_cidr_block):
            query['TransitRouterRouteEntryDestinationCidrBlock'] = request.transit_router_route_entry_destination_cidr_block
        if not UtilClient.is_unset(request.transit_router_route_entry_id):
            query['TransitRouterRouteEntryId'] = request.transit_router_route_entry_id
        if not UtilClient.is_unset(request.transit_router_route_entry_next_hop_id):
            query['TransitRouterRouteEntryNextHopId'] = request.transit_router_route_entry_next_hop_id
        if not UtilClient.is_unset(request.transit_router_route_entry_next_hop_type):
            query['TransitRouterRouteEntryNextHopType'] = request.transit_router_route_entry_next_hop_type
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTransitRouterRouteEntry',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteTransitRouterRouteEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_transit_router_route_entry_with_options_async(
        self,
        request: cbn_20170912_models.DeleteTransitRouterRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteTransitRouterRouteEntryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_route_entry_destination_cidr_block):
            query['TransitRouterRouteEntryDestinationCidrBlock'] = request.transit_router_route_entry_destination_cidr_block
        if not UtilClient.is_unset(request.transit_router_route_entry_id):
            query['TransitRouterRouteEntryId'] = request.transit_router_route_entry_id
        if not UtilClient.is_unset(request.transit_router_route_entry_next_hop_id):
            query['TransitRouterRouteEntryNextHopId'] = request.transit_router_route_entry_next_hop_id
        if not UtilClient.is_unset(request.transit_router_route_entry_next_hop_type):
            query['TransitRouterRouteEntryNextHopType'] = request.transit_router_route_entry_next_hop_type
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTransitRouterRouteEntry',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteTransitRouterRouteEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_transit_router_route_entry(
        self,
        request: cbn_20170912_models.DeleteTransitRouterRouteEntryRequest,
    ) -> cbn_20170912_models.DeleteTransitRouterRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_transit_router_route_entry_with_options(request, runtime)

    async def delete_transit_router_route_entry_async(
        self,
        request: cbn_20170912_models.DeleteTransitRouterRouteEntryRequest,
    ) -> cbn_20170912_models.DeleteTransitRouterRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_transit_router_route_entry_with_options_async(request, runtime)

    def delete_transit_router_route_table_with_options(
        self,
        request: cbn_20170912_models.DeleteTransitRouterRouteTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteTransitRouterRouteTableResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTransitRouterRouteTable',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteTransitRouterRouteTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_transit_router_route_table_with_options_async(
        self,
        request: cbn_20170912_models.DeleteTransitRouterRouteTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteTransitRouterRouteTableResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTransitRouterRouteTable',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteTransitRouterRouteTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_transit_router_route_table(
        self,
        request: cbn_20170912_models.DeleteTransitRouterRouteTableRequest,
    ) -> cbn_20170912_models.DeleteTransitRouterRouteTableResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_transit_router_route_table_with_options(request, runtime)

    async def delete_transit_router_route_table_async(
        self,
        request: cbn_20170912_models.DeleteTransitRouterRouteTableRequest,
    ) -> cbn_20170912_models.DeleteTransitRouterRouteTableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_transit_router_route_table_with_options_async(request, runtime)

    def delete_transit_router_vbr_attachment_with_options(
        self,
        request: cbn_20170912_models.DeleteTransitRouterVbrAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteTransitRouterVbrAttachmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTransitRouterVbrAttachment',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteTransitRouterVbrAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_transit_router_vbr_attachment_with_options_async(
        self,
        request: cbn_20170912_models.DeleteTransitRouterVbrAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteTransitRouterVbrAttachmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTransitRouterVbrAttachment',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteTransitRouterVbrAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_transit_router_vbr_attachment(
        self,
        request: cbn_20170912_models.DeleteTransitRouterVbrAttachmentRequest,
    ) -> cbn_20170912_models.DeleteTransitRouterVbrAttachmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_transit_router_vbr_attachment_with_options(request, runtime)

    async def delete_transit_router_vbr_attachment_async(
        self,
        request: cbn_20170912_models.DeleteTransitRouterVbrAttachmentRequest,
    ) -> cbn_20170912_models.DeleteTransitRouterVbrAttachmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_transit_router_vbr_attachment_with_options_async(request, runtime)

    def delete_transit_router_vpc_attachment_with_options(
        self,
        request: cbn_20170912_models.DeleteTransitRouterVpcAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteTransitRouterVpcAttachmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTransitRouterVpcAttachment',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteTransitRouterVpcAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_transit_router_vpc_attachment_with_options_async(
        self,
        request: cbn_20170912_models.DeleteTransitRouterVpcAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteTransitRouterVpcAttachmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTransitRouterVpcAttachment',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteTransitRouterVpcAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_transit_router_vpc_attachment(
        self,
        request: cbn_20170912_models.DeleteTransitRouterVpcAttachmentRequest,
    ) -> cbn_20170912_models.DeleteTransitRouterVpcAttachmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_transit_router_vpc_attachment_with_options(request, runtime)

    async def delete_transit_router_vpc_attachment_async(
        self,
        request: cbn_20170912_models.DeleteTransitRouterVpcAttachmentRequest,
    ) -> cbn_20170912_models.DeleteTransitRouterVpcAttachmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_transit_router_vpc_attachment_with_options_async(request, runtime)

    def delete_transit_router_vpn_attachment_with_options(
        self,
        request: cbn_20170912_models.DeleteTransitRouterVpnAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteTransitRouterVpnAttachmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTransitRouterVpnAttachment',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteTransitRouterVpnAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_transit_router_vpn_attachment_with_options_async(
        self,
        request: cbn_20170912_models.DeleteTransitRouterVpnAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteTransitRouterVpnAttachmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTransitRouterVpnAttachment',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteTransitRouterVpnAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_transit_router_vpn_attachment(
        self,
        request: cbn_20170912_models.DeleteTransitRouterVpnAttachmentRequest,
    ) -> cbn_20170912_models.DeleteTransitRouterVpnAttachmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_transit_router_vpn_attachment_with_options(request, runtime)

    async def delete_transit_router_vpn_attachment_async(
        self,
        request: cbn_20170912_models.DeleteTransitRouterVpnAttachmentRequest,
    ) -> cbn_20170912_models.DeleteTransitRouterVpnAttachmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_transit_router_vpn_attachment_with_options_async(request, runtime)

    def deregister_transit_router_multicast_group_members_with_options(
        self,
        request: cbn_20170912_models.DeregisterTransitRouterMulticastGroupMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeregisterTransitRouterMulticastGroupMembersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.group_ip_address):
            query['GroupIpAddress'] = request.group_ip_address
        if not UtilClient.is_unset(request.network_interface_ids):
            query['NetworkInterfaceIds'] = request.network_interface_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.peer_transit_router_multicast_domains):
            query['PeerTransitRouterMulticastDomains'] = request.peer_transit_router_multicast_domains
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeregisterTransitRouterMulticastGroupMembers',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeregisterTransitRouterMulticastGroupMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def deregister_transit_router_multicast_group_members_with_options_async(
        self,
        request: cbn_20170912_models.DeregisterTransitRouterMulticastGroupMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeregisterTransitRouterMulticastGroupMembersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.group_ip_address):
            query['GroupIpAddress'] = request.group_ip_address
        if not UtilClient.is_unset(request.network_interface_ids):
            query['NetworkInterfaceIds'] = request.network_interface_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.peer_transit_router_multicast_domains):
            query['PeerTransitRouterMulticastDomains'] = request.peer_transit_router_multicast_domains
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeregisterTransitRouterMulticastGroupMembers',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeregisterTransitRouterMulticastGroupMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deregister_transit_router_multicast_group_members(
        self,
        request: cbn_20170912_models.DeregisterTransitRouterMulticastGroupMembersRequest,
    ) -> cbn_20170912_models.DeregisterTransitRouterMulticastGroupMembersResponse:
        runtime = util_models.RuntimeOptions()
        return self.deregister_transit_router_multicast_group_members_with_options(request, runtime)

    async def deregister_transit_router_multicast_group_members_async(
        self,
        request: cbn_20170912_models.DeregisterTransitRouterMulticastGroupMembersRequest,
    ) -> cbn_20170912_models.DeregisterTransitRouterMulticastGroupMembersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deregister_transit_router_multicast_group_members_with_options_async(request, runtime)

    def deregister_transit_router_multicast_group_sources_with_options(
        self,
        request: cbn_20170912_models.DeregisterTransitRouterMulticastGroupSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeregisterTransitRouterMulticastGroupSourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.group_ip_address):
            query['GroupIpAddress'] = request.group_ip_address
        if not UtilClient.is_unset(request.network_interface_ids):
            query['NetworkInterfaceIds'] = request.network_interface_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeregisterTransitRouterMulticastGroupSources',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeregisterTransitRouterMulticastGroupSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def deregister_transit_router_multicast_group_sources_with_options_async(
        self,
        request: cbn_20170912_models.DeregisterTransitRouterMulticastGroupSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeregisterTransitRouterMulticastGroupSourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.group_ip_address):
            query['GroupIpAddress'] = request.group_ip_address
        if not UtilClient.is_unset(request.network_interface_ids):
            query['NetworkInterfaceIds'] = request.network_interface_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeregisterTransitRouterMulticastGroupSources',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeregisterTransitRouterMulticastGroupSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deregister_transit_router_multicast_group_sources(
        self,
        request: cbn_20170912_models.DeregisterTransitRouterMulticastGroupSourcesRequest,
    ) -> cbn_20170912_models.DeregisterTransitRouterMulticastGroupSourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.deregister_transit_router_multicast_group_sources_with_options(request, runtime)

    async def deregister_transit_router_multicast_group_sources_async(
        self,
        request: cbn_20170912_models.DeregisterTransitRouterMulticastGroupSourcesRequest,
    ) -> cbn_20170912_models.DeregisterTransitRouterMulticastGroupSourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deregister_transit_router_multicast_group_sources_with_options_async(request, runtime)

    def describe_cen_attached_child_instance_attribute_with_options(
        self,
        request: cbn_20170912_models.DescribeCenAttachedChildInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenAttachedChildInstanceAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not UtilClient.is_unset(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not UtilClient.is_unset(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCenAttachedChildInstanceAttribute',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenAttachedChildInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cen_attached_child_instance_attribute_with_options_async(
        self,
        request: cbn_20170912_models.DescribeCenAttachedChildInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenAttachedChildInstanceAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not UtilClient.is_unset(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not UtilClient.is_unset(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCenAttachedChildInstanceAttribute',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenAttachedChildInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cen_attached_child_instance_attribute(
        self,
        request: cbn_20170912_models.DescribeCenAttachedChildInstanceAttributeRequest,
    ) -> cbn_20170912_models.DescribeCenAttachedChildInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cen_attached_child_instance_attribute_with_options(request, runtime)

    async def describe_cen_attached_child_instance_attribute_async(
        self,
        request: cbn_20170912_models.DescribeCenAttachedChildInstanceAttributeRequest,
    ) -> cbn_20170912_models.DescribeCenAttachedChildInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cen_attached_child_instance_attribute_with_options_async(request, runtime)

    def describe_cen_attached_child_instances_with_options(
        self,
        request: cbn_20170912_models.DescribeCenAttachedChildInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenAttachedChildInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not UtilClient.is_unset(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCenAttachedChildInstances',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenAttachedChildInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cen_attached_child_instances_with_options_async(
        self,
        request: cbn_20170912_models.DescribeCenAttachedChildInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenAttachedChildInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not UtilClient.is_unset(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCenAttachedChildInstances',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenAttachedChildInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cen_attached_child_instances(
        self,
        request: cbn_20170912_models.DescribeCenAttachedChildInstancesRequest,
    ) -> cbn_20170912_models.DescribeCenAttachedChildInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cen_attached_child_instances_with_options(request, runtime)

    async def describe_cen_attached_child_instances_async(
        self,
        request: cbn_20170912_models.DescribeCenAttachedChildInstancesRequest,
    ) -> cbn_20170912_models.DescribeCenAttachedChildInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cen_attached_child_instances_with_options_async(request, runtime)

    def describe_cen_bandwidth_packages_with_options(
        self,
        request: cbn_20170912_models.DescribeCenBandwidthPackagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenBandwidthPackagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.include_reservation_data):
            query['IncludeReservationData'] = request.include_reservation_data
        if not UtilClient.is_unset(request.is_or_key):
            query['IsOrKey'] = request.is_or_key
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCenBandwidthPackages',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenBandwidthPackagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cen_bandwidth_packages_with_options_async(
        self,
        request: cbn_20170912_models.DescribeCenBandwidthPackagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenBandwidthPackagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.include_reservation_data):
            query['IncludeReservationData'] = request.include_reservation_data
        if not UtilClient.is_unset(request.is_or_key):
            query['IsOrKey'] = request.is_or_key
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCenBandwidthPackages',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenBandwidthPackagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cen_bandwidth_packages(
        self,
        request: cbn_20170912_models.DescribeCenBandwidthPackagesRequest,
    ) -> cbn_20170912_models.DescribeCenBandwidthPackagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cen_bandwidth_packages_with_options(request, runtime)

    async def describe_cen_bandwidth_packages_async(
        self,
        request: cbn_20170912_models.DescribeCenBandwidthPackagesRequest,
    ) -> cbn_20170912_models.DescribeCenBandwidthPackagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cen_bandwidth_packages_with_options_async(request, runtime)

    def describe_cen_child_instance_route_entries_with_options(
        self,
        request: cbn_20170912_models.DescribeCenChildInstanceRouteEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenChildInstanceRouteEntriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not UtilClient.is_unset(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not UtilClient.is_unset(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCenChildInstanceRouteEntries',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenChildInstanceRouteEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cen_child_instance_route_entries_with_options_async(
        self,
        request: cbn_20170912_models.DescribeCenChildInstanceRouteEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenChildInstanceRouteEntriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not UtilClient.is_unset(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not UtilClient.is_unset(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCenChildInstanceRouteEntries',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenChildInstanceRouteEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cen_child_instance_route_entries(
        self,
        request: cbn_20170912_models.DescribeCenChildInstanceRouteEntriesRequest,
    ) -> cbn_20170912_models.DescribeCenChildInstanceRouteEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cen_child_instance_route_entries_with_options(request, runtime)

    async def describe_cen_child_instance_route_entries_async(
        self,
        request: cbn_20170912_models.DescribeCenChildInstanceRouteEntriesRequest,
    ) -> cbn_20170912_models.DescribeCenChildInstanceRouteEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cen_child_instance_route_entries_with_options_async(request, runtime)

    def describe_cen_geographic_span_remaining_bandwidth_with_options(
        self,
        request: cbn_20170912_models.DescribeCenGeographicSpanRemainingBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenGeographicSpanRemainingBandwidthResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.geographic_region_aid):
            query['GeographicRegionAId'] = request.geographic_region_aid
        if not UtilClient.is_unset(request.geographic_region_bid):
            query['GeographicRegionBId'] = request.geographic_region_bid
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCenGeographicSpanRemainingBandwidth',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenGeographicSpanRemainingBandwidthResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cen_geographic_span_remaining_bandwidth_with_options_async(
        self,
        request: cbn_20170912_models.DescribeCenGeographicSpanRemainingBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenGeographicSpanRemainingBandwidthResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.geographic_region_aid):
            query['GeographicRegionAId'] = request.geographic_region_aid
        if not UtilClient.is_unset(request.geographic_region_bid):
            query['GeographicRegionBId'] = request.geographic_region_bid
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCenGeographicSpanRemainingBandwidth',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenGeographicSpanRemainingBandwidthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cen_geographic_span_remaining_bandwidth(
        self,
        request: cbn_20170912_models.DescribeCenGeographicSpanRemainingBandwidthRequest,
    ) -> cbn_20170912_models.DescribeCenGeographicSpanRemainingBandwidthResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cen_geographic_span_remaining_bandwidth_with_options(request, runtime)

    async def describe_cen_geographic_span_remaining_bandwidth_async(
        self,
        request: cbn_20170912_models.DescribeCenGeographicSpanRemainingBandwidthRequest,
    ) -> cbn_20170912_models.DescribeCenGeographicSpanRemainingBandwidthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cen_geographic_span_remaining_bandwidth_with_options_async(request, runtime)

    def describe_cen_geographic_spans_with_options(
        self,
        request: cbn_20170912_models.DescribeCenGeographicSpansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenGeographicSpansResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.geographic_span_id):
            query['GeographicSpanId'] = request.geographic_span_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCenGeographicSpans',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenGeographicSpansResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cen_geographic_spans_with_options_async(
        self,
        request: cbn_20170912_models.DescribeCenGeographicSpansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenGeographicSpansResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.geographic_span_id):
            query['GeographicSpanId'] = request.geographic_span_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCenGeographicSpans',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenGeographicSpansResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cen_geographic_spans(
        self,
        request: cbn_20170912_models.DescribeCenGeographicSpansRequest,
    ) -> cbn_20170912_models.DescribeCenGeographicSpansResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cen_geographic_spans_with_options(request, runtime)

    async def describe_cen_geographic_spans_async(
        self,
        request: cbn_20170912_models.DescribeCenGeographicSpansRequest,
    ) -> cbn_20170912_models.DescribeCenGeographicSpansResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cen_geographic_spans_with_options_async(request, runtime)

    def describe_cen_inter_region_bandwidth_limits_with_options(
        self,
        request: cbn_20170912_models.DescribeCenInterRegionBandwidthLimitsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenInterRegionBandwidthLimitsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCenInterRegionBandwidthLimits',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenInterRegionBandwidthLimitsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cen_inter_region_bandwidth_limits_with_options_async(
        self,
        request: cbn_20170912_models.DescribeCenInterRegionBandwidthLimitsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenInterRegionBandwidthLimitsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCenInterRegionBandwidthLimits',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenInterRegionBandwidthLimitsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cen_inter_region_bandwidth_limits(
        self,
        request: cbn_20170912_models.DescribeCenInterRegionBandwidthLimitsRequest,
    ) -> cbn_20170912_models.DescribeCenInterRegionBandwidthLimitsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cen_inter_region_bandwidth_limits_with_options(request, runtime)

    async def describe_cen_inter_region_bandwidth_limits_async(
        self,
        request: cbn_20170912_models.DescribeCenInterRegionBandwidthLimitsRequest,
    ) -> cbn_20170912_models.DescribeCenInterRegionBandwidthLimitsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cen_inter_region_bandwidth_limits_with_options_async(request, runtime)

    def describe_cen_private_zone_routes_with_options(
        self,
        request: cbn_20170912_models.DescribeCenPrivateZoneRoutesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenPrivateZoneRoutesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_region_id):
            query['AccessRegionId'] = request.access_region_id
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.host_region_id):
            query['HostRegionId'] = request.host_region_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCenPrivateZoneRoutes',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenPrivateZoneRoutesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cen_private_zone_routes_with_options_async(
        self,
        request: cbn_20170912_models.DescribeCenPrivateZoneRoutesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenPrivateZoneRoutesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_region_id):
            query['AccessRegionId'] = request.access_region_id
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.host_region_id):
            query['HostRegionId'] = request.host_region_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCenPrivateZoneRoutes',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenPrivateZoneRoutesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cen_private_zone_routes(
        self,
        request: cbn_20170912_models.DescribeCenPrivateZoneRoutesRequest,
    ) -> cbn_20170912_models.DescribeCenPrivateZoneRoutesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cen_private_zone_routes_with_options(request, runtime)

    async def describe_cen_private_zone_routes_async(
        self,
        request: cbn_20170912_models.DescribeCenPrivateZoneRoutesRequest,
    ) -> cbn_20170912_models.DescribeCenPrivateZoneRoutesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cen_private_zone_routes_with_options_async(request, runtime)

    def describe_cen_region_domain_route_entries_with_options(
        self,
        request: cbn_20170912_models.DescribeCenRegionDomainRouteEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenRegionDomainRouteEntriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.cen_region_id):
            query['CenRegionId'] = request.cen_region_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCenRegionDomainRouteEntries',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenRegionDomainRouteEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cen_region_domain_route_entries_with_options_async(
        self,
        request: cbn_20170912_models.DescribeCenRegionDomainRouteEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenRegionDomainRouteEntriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.cen_region_id):
            query['CenRegionId'] = request.cen_region_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCenRegionDomainRouteEntries',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenRegionDomainRouteEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cen_region_domain_route_entries(
        self,
        request: cbn_20170912_models.DescribeCenRegionDomainRouteEntriesRequest,
    ) -> cbn_20170912_models.DescribeCenRegionDomainRouteEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cen_region_domain_route_entries_with_options(request, runtime)

    async def describe_cen_region_domain_route_entries_async(
        self,
        request: cbn_20170912_models.DescribeCenRegionDomainRouteEntriesRequest,
    ) -> cbn_20170912_models.DescribeCenRegionDomainRouteEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cen_region_domain_route_entries_with_options_async(request, runtime)

    def describe_cen_route_maps_with_options(
        self,
        request: cbn_20170912_models.DescribeCenRouteMapsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenRouteMapsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.cen_region_id):
            query['CenRegionId'] = request.cen_region_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.route_map_id):
            query['RouteMapId'] = request.route_map_id
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        if not UtilClient.is_unset(request.transmit_direction):
            query['TransmitDirection'] = request.transmit_direction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCenRouteMaps',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenRouteMapsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cen_route_maps_with_options_async(
        self,
        request: cbn_20170912_models.DescribeCenRouteMapsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenRouteMapsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.cen_region_id):
            query['CenRegionId'] = request.cen_region_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.route_map_id):
            query['RouteMapId'] = request.route_map_id
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        if not UtilClient.is_unset(request.transmit_direction):
            query['TransmitDirection'] = request.transmit_direction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCenRouteMaps',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenRouteMapsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cen_route_maps(
        self,
        request: cbn_20170912_models.DescribeCenRouteMapsRequest,
    ) -> cbn_20170912_models.DescribeCenRouteMapsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cen_route_maps_with_options(request, runtime)

    async def describe_cen_route_maps_async(
        self,
        request: cbn_20170912_models.DescribeCenRouteMapsRequest,
    ) -> cbn_20170912_models.DescribeCenRouteMapsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cen_route_maps_with_options_async(request, runtime)

    def describe_cen_vbr_health_check_with_options(
        self,
        request: cbn_20170912_models.DescribeCenVbrHealthCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenVbrHealthCheckResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vbr_instance_id):
            query['VbrInstanceId'] = request.vbr_instance_id
        if not UtilClient.is_unset(request.vbr_instance_owner_id):
            query['VbrInstanceOwnerId'] = request.vbr_instance_owner_id
        if not UtilClient.is_unset(request.vbr_instance_region_id):
            query['VbrInstanceRegionId'] = request.vbr_instance_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCenVbrHealthCheck',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenVbrHealthCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cen_vbr_health_check_with_options_async(
        self,
        request: cbn_20170912_models.DescribeCenVbrHealthCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenVbrHealthCheckResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vbr_instance_id):
            query['VbrInstanceId'] = request.vbr_instance_id
        if not UtilClient.is_unset(request.vbr_instance_owner_id):
            query['VbrInstanceOwnerId'] = request.vbr_instance_owner_id
        if not UtilClient.is_unset(request.vbr_instance_region_id):
            query['VbrInstanceRegionId'] = request.vbr_instance_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCenVbrHealthCheck',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenVbrHealthCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cen_vbr_health_check(
        self,
        request: cbn_20170912_models.DescribeCenVbrHealthCheckRequest,
    ) -> cbn_20170912_models.DescribeCenVbrHealthCheckResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cen_vbr_health_check_with_options(request, runtime)

    async def describe_cen_vbr_health_check_async(
        self,
        request: cbn_20170912_models.DescribeCenVbrHealthCheckRequest,
    ) -> cbn_20170912_models.DescribeCenVbrHealthCheckResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cen_vbr_health_check_with_options_async(request, runtime)

    def describe_cens_with_options(
        self,
        request: cbn_20170912_models.DescribeCensRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCensResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCens',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCensResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cens_with_options_async(
        self,
        request: cbn_20170912_models.DescribeCensRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCensResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCens',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCensResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cens(
        self,
        request: cbn_20170912_models.DescribeCensRequest,
    ) -> cbn_20170912_models.DescribeCensResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cens_with_options(request, runtime)

    async def describe_cens_async(
        self,
        request: cbn_20170912_models.DescribeCensRequest,
    ) -> cbn_20170912_models.DescribeCensResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cens_with_options_async(request, runtime)

    def describe_child_instance_regions_with_options(
        self,
        request: cbn_20170912_models.DescribeChildInstanceRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeChildInstanceRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChildInstanceRegions',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeChildInstanceRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_child_instance_regions_with_options_async(
        self,
        request: cbn_20170912_models.DescribeChildInstanceRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeChildInstanceRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChildInstanceRegions',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeChildInstanceRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_child_instance_regions(
        self,
        request: cbn_20170912_models.DescribeChildInstanceRegionsRequest,
    ) -> cbn_20170912_models.DescribeChildInstanceRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_child_instance_regions_with_options(request, runtime)

    async def describe_child_instance_regions_async(
        self,
        request: cbn_20170912_models.DescribeChildInstanceRegionsRequest,
    ) -> cbn_20170912_models.DescribeChildInstanceRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_child_instance_regions_with_options_async(request, runtime)

    def describe_flowlogs_with_options(
        self,
        request: cbn_20170912_models.DescribeFlowlogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeFlowlogsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not UtilClient.is_unset(request.flow_log_name):
            query['FlowLogName'] = request.flow_log_name
        if not UtilClient.is_unset(request.log_store_name):
            query['LogStoreName'] = request.log_store_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowlogs',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeFlowlogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flowlogs_with_options_async(
        self,
        request: cbn_20170912_models.DescribeFlowlogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeFlowlogsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not UtilClient.is_unset(request.flow_log_name):
            query['FlowLogName'] = request.flow_log_name
        if not UtilClient.is_unset(request.log_store_name):
            query['LogStoreName'] = request.log_store_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowlogs',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeFlowlogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_flowlogs(
        self,
        request: cbn_20170912_models.DescribeFlowlogsRequest,
    ) -> cbn_20170912_models.DescribeFlowlogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flowlogs_with_options(request, runtime)

    async def describe_flowlogs_async(
        self,
        request: cbn_20170912_models.DescribeFlowlogsRequest,
    ) -> cbn_20170912_models.DescribeFlowlogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flowlogs_with_options_async(request, runtime)

    def describe_geographic_region_membership_with_options(
        self,
        request: cbn_20170912_models.DescribeGeographicRegionMembershipRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeGeographicRegionMembershipResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.geographic_region_id):
            query['GeographicRegionId'] = request.geographic_region_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGeographicRegionMembership',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeGeographicRegionMembershipResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_geographic_region_membership_with_options_async(
        self,
        request: cbn_20170912_models.DescribeGeographicRegionMembershipRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeGeographicRegionMembershipResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.geographic_region_id):
            query['GeographicRegionId'] = request.geographic_region_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGeographicRegionMembership',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeGeographicRegionMembershipResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_geographic_region_membership(
        self,
        request: cbn_20170912_models.DescribeGeographicRegionMembershipRequest,
    ) -> cbn_20170912_models.DescribeGeographicRegionMembershipResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_geographic_region_membership_with_options(request, runtime)

    async def describe_geographic_region_membership_async(
        self,
        request: cbn_20170912_models.DescribeGeographicRegionMembershipRequest,
    ) -> cbn_20170912_models.DescribeGeographicRegionMembershipResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_geographic_region_membership_with_options_async(request, runtime)

    def describe_grant_rules_to_cen_with_options(
        self,
        request: cbn_20170912_models.DescribeGrantRulesToCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeGrantRulesToCenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGrantRulesToCen',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeGrantRulesToCenResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_grant_rules_to_cen_with_options_async(
        self,
        request: cbn_20170912_models.DescribeGrantRulesToCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeGrantRulesToCenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGrantRulesToCen',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeGrantRulesToCenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_grant_rules_to_cen(
        self,
        request: cbn_20170912_models.DescribeGrantRulesToCenRequest,
    ) -> cbn_20170912_models.DescribeGrantRulesToCenResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_grant_rules_to_cen_with_options(request, runtime)

    async def describe_grant_rules_to_cen_async(
        self,
        request: cbn_20170912_models.DescribeGrantRulesToCenRequest,
    ) -> cbn_20170912_models.DescribeGrantRulesToCenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_grant_rules_to_cen_with_options_async(request, runtime)

    def describe_grant_rules_to_resource_with_options(
        self,
        request: cbn_20170912_models.DescribeGrantRulesToResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeGrantRulesToResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGrantRulesToResource',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeGrantRulesToResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_grant_rules_to_resource_with_options_async(
        self,
        request: cbn_20170912_models.DescribeGrantRulesToResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeGrantRulesToResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGrantRulesToResource',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeGrantRulesToResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_grant_rules_to_resource(
        self,
        request: cbn_20170912_models.DescribeGrantRulesToResourceRequest,
    ) -> cbn_20170912_models.DescribeGrantRulesToResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_grant_rules_to_resource_with_options(request, runtime)

    async def describe_grant_rules_to_resource_async(
        self,
        request: cbn_20170912_models.DescribeGrantRulesToResourceRequest,
    ) -> cbn_20170912_models.DescribeGrantRulesToResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_grant_rules_to_resource_with_options_async(request, runtime)

    def describe_published_route_entries_with_options(
        self,
        request: cbn_20170912_models.DescribePublishedRouteEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribePublishedRouteEntriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not UtilClient.is_unset(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not UtilClient.is_unset(request.child_instance_route_table_id):
            query['ChildInstanceRouteTableId'] = request.child_instance_route_table_id
        if not UtilClient.is_unset(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not UtilClient.is_unset(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePublishedRouteEntries',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribePublishedRouteEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_published_route_entries_with_options_async(
        self,
        request: cbn_20170912_models.DescribePublishedRouteEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribePublishedRouteEntriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not UtilClient.is_unset(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not UtilClient.is_unset(request.child_instance_route_table_id):
            query['ChildInstanceRouteTableId'] = request.child_instance_route_table_id
        if not UtilClient.is_unset(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not UtilClient.is_unset(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePublishedRouteEntries',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribePublishedRouteEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_published_route_entries(
        self,
        request: cbn_20170912_models.DescribePublishedRouteEntriesRequest,
    ) -> cbn_20170912_models.DescribePublishedRouteEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_published_route_entries_with_options(request, runtime)

    async def describe_published_route_entries_async(
        self,
        request: cbn_20170912_models.DescribePublishedRouteEntriesRequest,
    ) -> cbn_20170912_models.DescribePublishedRouteEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_published_route_entries_with_options_async(request, runtime)

    def describe_route_conflict_with_options(
        self,
        request: cbn_20170912_models.DescribeRouteConflictRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeRouteConflictResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not UtilClient.is_unset(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not UtilClient.is_unset(request.child_instance_route_table_id):
            query['ChildInstanceRouteTableId'] = request.child_instance_route_table_id
        if not UtilClient.is_unset(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not UtilClient.is_unset(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRouteConflict',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeRouteConflictResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_route_conflict_with_options_async(
        self,
        request: cbn_20170912_models.DescribeRouteConflictRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeRouteConflictResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not UtilClient.is_unset(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not UtilClient.is_unset(request.child_instance_route_table_id):
            query['ChildInstanceRouteTableId'] = request.child_instance_route_table_id
        if not UtilClient.is_unset(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not UtilClient.is_unset(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRouteConflict',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeRouteConflictResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_route_conflict(
        self,
        request: cbn_20170912_models.DescribeRouteConflictRequest,
    ) -> cbn_20170912_models.DescribeRouteConflictResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_route_conflict_with_options(request, runtime)

    async def describe_route_conflict_async(
        self,
        request: cbn_20170912_models.DescribeRouteConflictRequest,
    ) -> cbn_20170912_models.DescribeRouteConflictResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_route_conflict_with_options_async(request, runtime)

    def describe_route_services_in_cen_with_options(
        self,
        request: cbn_20170912_models.DescribeRouteServicesInCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeRouteServicesInCenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_region_id):
            query['AccessRegionId'] = request.access_region_id
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.host):
            query['Host'] = request.host
        if not UtilClient.is_unset(request.host_region_id):
            query['HostRegionId'] = request.host_region_id
        if not UtilClient.is_unset(request.host_vpc_id):
            query['HostVpcId'] = request.host_vpc_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRouteServicesInCen',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeRouteServicesInCenResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_route_services_in_cen_with_options_async(
        self,
        request: cbn_20170912_models.DescribeRouteServicesInCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeRouteServicesInCenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_region_id):
            query['AccessRegionId'] = request.access_region_id
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.host):
            query['Host'] = request.host
        if not UtilClient.is_unset(request.host_region_id):
            query['HostRegionId'] = request.host_region_id
        if not UtilClient.is_unset(request.host_vpc_id):
            query['HostVpcId'] = request.host_vpc_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRouteServicesInCen',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeRouteServicesInCenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_route_services_in_cen(
        self,
        request: cbn_20170912_models.DescribeRouteServicesInCenRequest,
    ) -> cbn_20170912_models.DescribeRouteServicesInCenResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_route_services_in_cen_with_options(request, runtime)

    async def describe_route_services_in_cen_async(
        self,
        request: cbn_20170912_models.DescribeRouteServicesInCenRequest,
    ) -> cbn_20170912_models.DescribeRouteServicesInCenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_route_services_in_cen_with_options_async(request, runtime)

    def detach_cen_child_instance_with_options(
        self,
        request: cbn_20170912_models.DetachCenChildInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DetachCenChildInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.cen_owner_id):
            query['CenOwnerId'] = request.cen_owner_id
        if not UtilClient.is_unset(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not UtilClient.is_unset(request.child_instance_owner_id):
            query['ChildInstanceOwnerId'] = request.child_instance_owner_id
        if not UtilClient.is_unset(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not UtilClient.is_unset(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachCenChildInstance',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DetachCenChildInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_cen_child_instance_with_options_async(
        self,
        request: cbn_20170912_models.DetachCenChildInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DetachCenChildInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.cen_owner_id):
            query['CenOwnerId'] = request.cen_owner_id
        if not UtilClient.is_unset(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not UtilClient.is_unset(request.child_instance_owner_id):
            query['ChildInstanceOwnerId'] = request.child_instance_owner_id
        if not UtilClient.is_unset(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not UtilClient.is_unset(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachCenChildInstance',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DetachCenChildInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_cen_child_instance(
        self,
        request: cbn_20170912_models.DetachCenChildInstanceRequest,
    ) -> cbn_20170912_models.DetachCenChildInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_cen_child_instance_with_options(request, runtime)

    async def detach_cen_child_instance_async(
        self,
        request: cbn_20170912_models.DetachCenChildInstanceRequest,
    ) -> cbn_20170912_models.DetachCenChildInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_cen_child_instance_with_options_async(request, runtime)

    def disable_cen_vbr_health_check_with_options(
        self,
        request: cbn_20170912_models.DisableCenVbrHealthCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DisableCenVbrHealthCheckResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vbr_instance_id):
            query['VbrInstanceId'] = request.vbr_instance_id
        if not UtilClient.is_unset(request.vbr_instance_owner_id):
            query['VbrInstanceOwnerId'] = request.vbr_instance_owner_id
        if not UtilClient.is_unset(request.vbr_instance_region_id):
            query['VbrInstanceRegionId'] = request.vbr_instance_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableCenVbrHealthCheck',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DisableCenVbrHealthCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_cen_vbr_health_check_with_options_async(
        self,
        request: cbn_20170912_models.DisableCenVbrHealthCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DisableCenVbrHealthCheckResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vbr_instance_id):
            query['VbrInstanceId'] = request.vbr_instance_id
        if not UtilClient.is_unset(request.vbr_instance_owner_id):
            query['VbrInstanceOwnerId'] = request.vbr_instance_owner_id
        if not UtilClient.is_unset(request.vbr_instance_region_id):
            query['VbrInstanceRegionId'] = request.vbr_instance_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableCenVbrHealthCheck',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DisableCenVbrHealthCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_cen_vbr_health_check(
        self,
        request: cbn_20170912_models.DisableCenVbrHealthCheckRequest,
    ) -> cbn_20170912_models.DisableCenVbrHealthCheckResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_cen_vbr_health_check_with_options(request, runtime)

    async def disable_cen_vbr_health_check_async(
        self,
        request: cbn_20170912_models.DisableCenVbrHealthCheckRequest,
    ) -> cbn_20170912_models.DisableCenVbrHealthCheckResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_cen_vbr_health_check_with_options_async(request, runtime)

    def disable_transit_router_route_table_propagation_with_options(
        self,
        request: cbn_20170912_models.DisableTransitRouterRouteTablePropagationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DisableTransitRouterRouteTablePropagationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableTransitRouterRouteTablePropagation',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DisableTransitRouterRouteTablePropagationResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_transit_router_route_table_propagation_with_options_async(
        self,
        request: cbn_20170912_models.DisableTransitRouterRouteTablePropagationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DisableTransitRouterRouteTablePropagationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableTransitRouterRouteTablePropagation',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DisableTransitRouterRouteTablePropagationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_transit_router_route_table_propagation(
        self,
        request: cbn_20170912_models.DisableTransitRouterRouteTablePropagationRequest,
    ) -> cbn_20170912_models.DisableTransitRouterRouteTablePropagationResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_transit_router_route_table_propagation_with_options(request, runtime)

    async def disable_transit_router_route_table_propagation_async(
        self,
        request: cbn_20170912_models.DisableTransitRouterRouteTablePropagationRequest,
    ) -> cbn_20170912_models.DisableTransitRouterRouteTablePropagationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_transit_router_route_table_propagation_with_options_async(request, runtime)

    def disassociate_transit_router_multicast_domain_with_options(
        self,
        request: cbn_20170912_models.DisassociateTransitRouterMulticastDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DisassociateTransitRouterMulticastDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        if not UtilClient.is_unset(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisassociateTransitRouterMulticastDomain',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DisassociateTransitRouterMulticastDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def disassociate_transit_router_multicast_domain_with_options_async(
        self,
        request: cbn_20170912_models.DisassociateTransitRouterMulticastDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DisassociateTransitRouterMulticastDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        if not UtilClient.is_unset(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisassociateTransitRouterMulticastDomain',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DisassociateTransitRouterMulticastDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disassociate_transit_router_multicast_domain(
        self,
        request: cbn_20170912_models.DisassociateTransitRouterMulticastDomainRequest,
    ) -> cbn_20170912_models.DisassociateTransitRouterMulticastDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.disassociate_transit_router_multicast_domain_with_options(request, runtime)

    async def disassociate_transit_router_multicast_domain_async(
        self,
        request: cbn_20170912_models.DisassociateTransitRouterMulticastDomainRequest,
    ) -> cbn_20170912_models.DisassociateTransitRouterMulticastDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disassociate_transit_router_multicast_domain_with_options_async(request, runtime)

    def dissociate_transit_router_attachment_from_route_table_with_options(
        self,
        request: cbn_20170912_models.DissociateTransitRouterAttachmentFromRouteTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DissociateTransitRouterAttachmentFromRouteTableResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DissociateTransitRouterAttachmentFromRouteTable',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DissociateTransitRouterAttachmentFromRouteTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def dissociate_transit_router_attachment_from_route_table_with_options_async(
        self,
        request: cbn_20170912_models.DissociateTransitRouterAttachmentFromRouteTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DissociateTransitRouterAttachmentFromRouteTableResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DissociateTransitRouterAttachmentFromRouteTable',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DissociateTransitRouterAttachmentFromRouteTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dissociate_transit_router_attachment_from_route_table(
        self,
        request: cbn_20170912_models.DissociateTransitRouterAttachmentFromRouteTableRequest,
    ) -> cbn_20170912_models.DissociateTransitRouterAttachmentFromRouteTableResponse:
        runtime = util_models.RuntimeOptions()
        return self.dissociate_transit_router_attachment_from_route_table_with_options(request, runtime)

    async def dissociate_transit_router_attachment_from_route_table_async(
        self,
        request: cbn_20170912_models.DissociateTransitRouterAttachmentFromRouteTableRequest,
    ) -> cbn_20170912_models.DissociateTransitRouterAttachmentFromRouteTableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dissociate_transit_router_attachment_from_route_table_with_options_async(request, runtime)

    def enable_cen_vbr_health_check_with_options(
        self,
        request: cbn_20170912_models.EnableCenVbrHealthCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.EnableCenVbrHealthCheckResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_only):
            query['HealthCheckOnly'] = request.health_check_only
        if not UtilClient.is_unset(request.health_check_source_ip):
            query['HealthCheckSourceIp'] = request.health_check_source_ip
        if not UtilClient.is_unset(request.health_check_target_ip):
            query['HealthCheckTargetIp'] = request.health_check_target_ip
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vbr_instance_id):
            query['VbrInstanceId'] = request.vbr_instance_id
        if not UtilClient.is_unset(request.vbr_instance_owner_id):
            query['VbrInstanceOwnerId'] = request.vbr_instance_owner_id
        if not UtilClient.is_unset(request.vbr_instance_region_id):
            query['VbrInstanceRegionId'] = request.vbr_instance_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableCenVbrHealthCheck',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.EnableCenVbrHealthCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_cen_vbr_health_check_with_options_async(
        self,
        request: cbn_20170912_models.EnableCenVbrHealthCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.EnableCenVbrHealthCheckResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_only):
            query['HealthCheckOnly'] = request.health_check_only
        if not UtilClient.is_unset(request.health_check_source_ip):
            query['HealthCheckSourceIp'] = request.health_check_source_ip
        if not UtilClient.is_unset(request.health_check_target_ip):
            query['HealthCheckTargetIp'] = request.health_check_target_ip
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vbr_instance_id):
            query['VbrInstanceId'] = request.vbr_instance_id
        if not UtilClient.is_unset(request.vbr_instance_owner_id):
            query['VbrInstanceOwnerId'] = request.vbr_instance_owner_id
        if not UtilClient.is_unset(request.vbr_instance_region_id):
            query['VbrInstanceRegionId'] = request.vbr_instance_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableCenVbrHealthCheck',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.EnableCenVbrHealthCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_cen_vbr_health_check(
        self,
        request: cbn_20170912_models.EnableCenVbrHealthCheckRequest,
    ) -> cbn_20170912_models.EnableCenVbrHealthCheckResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_cen_vbr_health_check_with_options(request, runtime)

    async def enable_cen_vbr_health_check_async(
        self,
        request: cbn_20170912_models.EnableCenVbrHealthCheckRequest,
    ) -> cbn_20170912_models.EnableCenVbrHealthCheckResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_cen_vbr_health_check_with_options_async(request, runtime)

    def enable_transit_router_route_table_propagation_with_options(
        self,
        request: cbn_20170912_models.EnableTransitRouterRouteTablePropagationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.EnableTransitRouterRouteTablePropagationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableTransitRouterRouteTablePropagation',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.EnableTransitRouterRouteTablePropagationResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_transit_router_route_table_propagation_with_options_async(
        self,
        request: cbn_20170912_models.EnableTransitRouterRouteTablePropagationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.EnableTransitRouterRouteTablePropagationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableTransitRouterRouteTablePropagation',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.EnableTransitRouterRouteTablePropagationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_transit_router_route_table_propagation(
        self,
        request: cbn_20170912_models.EnableTransitRouterRouteTablePropagationRequest,
    ) -> cbn_20170912_models.EnableTransitRouterRouteTablePropagationResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_transit_router_route_table_propagation_with_options(request, runtime)

    async def enable_transit_router_route_table_propagation_async(
        self,
        request: cbn_20170912_models.EnableTransitRouterRouteTablePropagationRequest,
    ) -> cbn_20170912_models.EnableTransitRouterRouteTablePropagationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_transit_router_route_table_propagation_with_options_async(request, runtime)

    def grant_instance_to_transit_router_with_options(
        self,
        request: cbn_20170912_models.GrantInstanceToTransitRouterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.GrantInstanceToTransitRouterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.cen_owner_id):
            query['CenOwnerId'] = request.cen_owner_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GrantInstanceToTransitRouter',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.GrantInstanceToTransitRouterResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_instance_to_transit_router_with_options_async(
        self,
        request: cbn_20170912_models.GrantInstanceToTransitRouterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.GrantInstanceToTransitRouterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.cen_owner_id):
            query['CenOwnerId'] = request.cen_owner_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GrantInstanceToTransitRouter',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.GrantInstanceToTransitRouterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_instance_to_transit_router(
        self,
        request: cbn_20170912_models.GrantInstanceToTransitRouterRequest,
    ) -> cbn_20170912_models.GrantInstanceToTransitRouterResponse:
        runtime = util_models.RuntimeOptions()
        return self.grant_instance_to_transit_router_with_options(request, runtime)

    async def grant_instance_to_transit_router_async(
        self,
        request: cbn_20170912_models.GrantInstanceToTransitRouterRequest,
    ) -> cbn_20170912_models.GrantInstanceToTransitRouterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.grant_instance_to_transit_router_with_options_async(request, runtime)

    def list_cen_inter_region_traffic_qos_policies_with_options(
        self,
        request: cbn_20170912_models.ListCenInterRegionTrafficQosPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListCenInterRegionTrafficQosPoliciesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.traffic_qos_policy_description):
            query['TrafficQosPolicyDescription'] = request.traffic_qos_policy_description
        if not UtilClient.is_unset(request.traffic_qos_policy_id):
            query['TrafficQosPolicyId'] = request.traffic_qos_policy_id
        if not UtilClient.is_unset(request.traffic_qos_policy_name):
            query['TrafficQosPolicyName'] = request.traffic_qos_policy_name
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCenInterRegionTrafficQosPolicies',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListCenInterRegionTrafficQosPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cen_inter_region_traffic_qos_policies_with_options_async(
        self,
        request: cbn_20170912_models.ListCenInterRegionTrafficQosPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListCenInterRegionTrafficQosPoliciesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.traffic_qos_policy_description):
            query['TrafficQosPolicyDescription'] = request.traffic_qos_policy_description
        if not UtilClient.is_unset(request.traffic_qos_policy_id):
            query['TrafficQosPolicyId'] = request.traffic_qos_policy_id
        if not UtilClient.is_unset(request.traffic_qos_policy_name):
            query['TrafficQosPolicyName'] = request.traffic_qos_policy_name
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCenInterRegionTrafficQosPolicies',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListCenInterRegionTrafficQosPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cen_inter_region_traffic_qos_policies(
        self,
        request: cbn_20170912_models.ListCenInterRegionTrafficQosPoliciesRequest,
    ) -> cbn_20170912_models.ListCenInterRegionTrafficQosPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cen_inter_region_traffic_qos_policies_with_options(request, runtime)

    async def list_cen_inter_region_traffic_qos_policies_async(
        self,
        request: cbn_20170912_models.ListCenInterRegionTrafficQosPoliciesRequest,
    ) -> cbn_20170912_models.ListCenInterRegionTrafficQosPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cen_inter_region_traffic_qos_policies_with_options_async(request, runtime)

    def list_grant_vswitch_enis_with_options(
        self,
        request: cbn_20170912_models.ListGrantVSwitchEnisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListGrantVSwitchEnisResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGrantVSwitchEnis',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListGrantVSwitchEnisResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_grant_vswitch_enis_with_options_async(
        self,
        request: cbn_20170912_models.ListGrantVSwitchEnisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListGrantVSwitchEnisResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGrantVSwitchEnis',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListGrantVSwitchEnisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_grant_vswitch_enis(
        self,
        request: cbn_20170912_models.ListGrantVSwitchEnisRequest,
    ) -> cbn_20170912_models.ListGrantVSwitchEnisResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_grant_vswitch_enis_with_options(request, runtime)

    async def list_grant_vswitch_enis_async(
        self,
        request: cbn_20170912_models.ListGrantVSwitchEnisRequest,
    ) -> cbn_20170912_models.ListGrantVSwitchEnisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_grant_vswitch_enis_with_options_async(request, runtime)

    def list_grant_vswitches_to_cen_with_options(
        self,
        request: cbn_20170912_models.ListGrantVSwitchesToCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListGrantVSwitchesToCenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGrantVSwitchesToCen',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListGrantVSwitchesToCenResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_grant_vswitches_to_cen_with_options_async(
        self,
        request: cbn_20170912_models.ListGrantVSwitchesToCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListGrantVSwitchesToCenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGrantVSwitchesToCen',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListGrantVSwitchesToCenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_grant_vswitches_to_cen(
        self,
        request: cbn_20170912_models.ListGrantVSwitchesToCenRequest,
    ) -> cbn_20170912_models.ListGrantVSwitchesToCenResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_grant_vswitches_to_cen_with_options(request, runtime)

    async def list_grant_vswitches_to_cen_async(
        self,
        request: cbn_20170912_models.ListGrantVSwitchesToCenRequest,
    ) -> cbn_20170912_models.ListGrantVSwitchesToCenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_grant_vswitches_to_cen_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: cbn_20170912_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: cbn_20170912_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: cbn_20170912_models.ListTagResourcesRequest,
    ) -> cbn_20170912_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: cbn_20170912_models.ListTagResourcesRequest,
    ) -> cbn_20170912_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_traffic_marking_policies_with_options(
        self,
        request: cbn_20170912_models.ListTrafficMarkingPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListTrafficMarkingPoliciesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.traffic_marking_policy_description):
            query['TrafficMarkingPolicyDescription'] = request.traffic_marking_policy_description
        if not UtilClient.is_unset(request.traffic_marking_policy_id):
            query['TrafficMarkingPolicyId'] = request.traffic_marking_policy_id
        if not UtilClient.is_unset(request.traffic_marking_policy_name):
            query['TrafficMarkingPolicyName'] = request.traffic_marking_policy_name
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTrafficMarkingPolicies',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTrafficMarkingPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_traffic_marking_policies_with_options_async(
        self,
        request: cbn_20170912_models.ListTrafficMarkingPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListTrafficMarkingPoliciesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.traffic_marking_policy_description):
            query['TrafficMarkingPolicyDescription'] = request.traffic_marking_policy_description
        if not UtilClient.is_unset(request.traffic_marking_policy_id):
            query['TrafficMarkingPolicyId'] = request.traffic_marking_policy_id
        if not UtilClient.is_unset(request.traffic_marking_policy_name):
            query['TrafficMarkingPolicyName'] = request.traffic_marking_policy_name
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTrafficMarkingPolicies',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTrafficMarkingPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_traffic_marking_policies(
        self,
        request: cbn_20170912_models.ListTrafficMarkingPoliciesRequest,
    ) -> cbn_20170912_models.ListTrafficMarkingPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_traffic_marking_policies_with_options(request, runtime)

    async def list_traffic_marking_policies_async(
        self,
        request: cbn_20170912_models.ListTrafficMarkingPoliciesRequest,
    ) -> cbn_20170912_models.ListTrafficMarkingPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_traffic_marking_policies_with_options_async(request, runtime)

    def list_transit_router_available_resource_with_options(
        self,
        request: cbn_20170912_models.ListTransitRouterAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListTransitRouterAvailableResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.support_multicast):
            query['SupportMulticast'] = request.support_multicast
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterAvailableResource',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterAvailableResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_transit_router_available_resource_with_options_async(
        self,
        request: cbn_20170912_models.ListTransitRouterAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListTransitRouterAvailableResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.support_multicast):
            query['SupportMulticast'] = request.support_multicast
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterAvailableResource',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterAvailableResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_transit_router_available_resource(
        self,
        request: cbn_20170912_models.ListTransitRouterAvailableResourceRequest,
    ) -> cbn_20170912_models.ListTransitRouterAvailableResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_transit_router_available_resource_with_options(request, runtime)

    async def list_transit_router_available_resource_async(
        self,
        request: cbn_20170912_models.ListTransitRouterAvailableResourceRequest,
    ) -> cbn_20170912_models.ListTransitRouterAvailableResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_transit_router_available_resource_with_options_async(request, runtime)

    def list_transit_router_cidr_with_options(
        self,
        request: cbn_20170912_models.ListTransitRouterCidrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListTransitRouterCidrResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_cidr_id):
            query['TransitRouterCidrId'] = request.transit_router_cidr_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterCidr',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterCidrResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_transit_router_cidr_with_options_async(
        self,
        request: cbn_20170912_models.ListTransitRouterCidrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListTransitRouterCidrResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_cidr_id):
            query['TransitRouterCidrId'] = request.transit_router_cidr_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterCidr',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterCidrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_transit_router_cidr(
        self,
        request: cbn_20170912_models.ListTransitRouterCidrRequest,
    ) -> cbn_20170912_models.ListTransitRouterCidrResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_transit_router_cidr_with_options(request, runtime)

    async def list_transit_router_cidr_async(
        self,
        request: cbn_20170912_models.ListTransitRouterCidrRequest,
    ) -> cbn_20170912_models.ListTransitRouterCidrResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_transit_router_cidr_with_options_async(request, runtime)

    def list_transit_router_cidr_allocation_with_options(
        self,
        request: cbn_20170912_models.ListTransitRouterCidrAllocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListTransitRouterCidrAllocationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attachment_id):
            query['AttachmentId'] = request.attachment_id
        if not UtilClient.is_unset(request.attachment_name):
            query['AttachmentName'] = request.attachment_name
        if not UtilClient.is_unset(request.cidr):
            query['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.cidr_block):
            query['CidrBlock'] = request.cidr_block
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dedicated_owner_id):
            query['DedicatedOwnerId'] = request.dedicated_owner_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_cidr_id):
            query['TransitRouterCidrId'] = request.transit_router_cidr_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterCidrAllocation',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterCidrAllocationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_transit_router_cidr_allocation_with_options_async(
        self,
        request: cbn_20170912_models.ListTransitRouterCidrAllocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListTransitRouterCidrAllocationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attachment_id):
            query['AttachmentId'] = request.attachment_id
        if not UtilClient.is_unset(request.attachment_name):
            query['AttachmentName'] = request.attachment_name
        if not UtilClient.is_unset(request.cidr):
            query['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.cidr_block):
            query['CidrBlock'] = request.cidr_block
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dedicated_owner_id):
            query['DedicatedOwnerId'] = request.dedicated_owner_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_cidr_id):
            query['TransitRouterCidrId'] = request.transit_router_cidr_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterCidrAllocation',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterCidrAllocationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_transit_router_cidr_allocation(
        self,
        request: cbn_20170912_models.ListTransitRouterCidrAllocationRequest,
    ) -> cbn_20170912_models.ListTransitRouterCidrAllocationResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_transit_router_cidr_allocation_with_options(request, runtime)

    async def list_transit_router_cidr_allocation_async(
        self,
        request: cbn_20170912_models.ListTransitRouterCidrAllocationRequest,
    ) -> cbn_20170912_models.ListTransitRouterCidrAllocationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_transit_router_cidr_allocation_with_options_async(request, runtime)

    def list_transit_router_multicast_domain_associations_with_options(
        self,
        request: cbn_20170912_models.ListTransitRouterMulticastDomainAssociationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListTransitRouterMulticastDomainAssociationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        if not UtilClient.is_unset(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterMulticastDomainAssociations',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterMulticastDomainAssociationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_transit_router_multicast_domain_associations_with_options_async(
        self,
        request: cbn_20170912_models.ListTransitRouterMulticastDomainAssociationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListTransitRouterMulticastDomainAssociationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        if not UtilClient.is_unset(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterMulticastDomainAssociations',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterMulticastDomainAssociationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_transit_router_multicast_domain_associations(
        self,
        request: cbn_20170912_models.ListTransitRouterMulticastDomainAssociationsRequest,
    ) -> cbn_20170912_models.ListTransitRouterMulticastDomainAssociationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_transit_router_multicast_domain_associations_with_options(request, runtime)

    async def list_transit_router_multicast_domain_associations_async(
        self,
        request: cbn_20170912_models.ListTransitRouterMulticastDomainAssociationsRequest,
    ) -> cbn_20170912_models.ListTransitRouterMulticastDomainAssociationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_transit_router_multicast_domain_associations_with_options_async(request, runtime)

    def list_transit_router_multicast_domain_vswitches_with_options(
        self,
        request: cbn_20170912_models.ListTransitRouterMulticastDomainVSwitchesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListTransitRouterMulticastDomainVSwitchesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterMulticastDomainVSwitches',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterMulticastDomainVSwitchesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_transit_router_multicast_domain_vswitches_with_options_async(
        self,
        request: cbn_20170912_models.ListTransitRouterMulticastDomainVSwitchesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListTransitRouterMulticastDomainVSwitchesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterMulticastDomainVSwitches',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterMulticastDomainVSwitchesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_transit_router_multicast_domain_vswitches(
        self,
        request: cbn_20170912_models.ListTransitRouterMulticastDomainVSwitchesRequest,
    ) -> cbn_20170912_models.ListTransitRouterMulticastDomainVSwitchesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_transit_router_multicast_domain_vswitches_with_options(request, runtime)

    async def list_transit_router_multicast_domain_vswitches_async(
        self,
        request: cbn_20170912_models.ListTransitRouterMulticastDomainVSwitchesRequest,
    ) -> cbn_20170912_models.ListTransitRouterMulticastDomainVSwitchesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_transit_router_multicast_domain_vswitches_with_options_async(request, runtime)

    def list_transit_router_multicast_domains_with_options(
        self,
        request: cbn_20170912_models.ListTransitRouterMulticastDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListTransitRouterMulticastDomainsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not UtilClient.is_unset(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterMulticastDomains',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterMulticastDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_transit_router_multicast_domains_with_options_async(
        self,
        request: cbn_20170912_models.ListTransitRouterMulticastDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListTransitRouterMulticastDomainsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not UtilClient.is_unset(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterMulticastDomains',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterMulticastDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_transit_router_multicast_domains(
        self,
        request: cbn_20170912_models.ListTransitRouterMulticastDomainsRequest,
    ) -> cbn_20170912_models.ListTransitRouterMulticastDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_transit_router_multicast_domains_with_options(request, runtime)

    async def list_transit_router_multicast_domains_async(
        self,
        request: cbn_20170912_models.ListTransitRouterMulticastDomainsRequest,
    ) -> cbn_20170912_models.ListTransitRouterMulticastDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_transit_router_multicast_domains_with_options_async(request, runtime)

    def list_transit_router_multicast_groups_with_options(
        self,
        request: cbn_20170912_models.ListTransitRouterMulticastGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListTransitRouterMulticastGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.group_ip_address):
            query['GroupIpAddress'] = request.group_ip_address
        if not UtilClient.is_unset(request.is_group_member):
            query['IsGroupMember'] = request.is_group_member
        if not UtilClient.is_unset(request.is_group_source):
            query['IsGroupSource'] = request.is_group_source
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.network_interface_ids):
            query['NetworkInterfaceIds'] = request.network_interface_ids
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.peer_transit_router_multicast_domains):
            query['PeerTransitRouterMulticastDomains'] = request.peer_transit_router_multicast_domains
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        if not UtilClient.is_unset(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterMulticastGroups',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterMulticastGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_transit_router_multicast_groups_with_options_async(
        self,
        request: cbn_20170912_models.ListTransitRouterMulticastGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListTransitRouterMulticastGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.group_ip_address):
            query['GroupIpAddress'] = request.group_ip_address
        if not UtilClient.is_unset(request.is_group_member):
            query['IsGroupMember'] = request.is_group_member
        if not UtilClient.is_unset(request.is_group_source):
            query['IsGroupSource'] = request.is_group_source
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.network_interface_ids):
            query['NetworkInterfaceIds'] = request.network_interface_ids
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.peer_transit_router_multicast_domains):
            query['PeerTransitRouterMulticastDomains'] = request.peer_transit_router_multicast_domains
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        if not UtilClient.is_unset(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterMulticastGroups',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterMulticastGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_transit_router_multicast_groups(
        self,
        request: cbn_20170912_models.ListTransitRouterMulticastGroupsRequest,
    ) -> cbn_20170912_models.ListTransitRouterMulticastGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_transit_router_multicast_groups_with_options(request, runtime)

    async def list_transit_router_multicast_groups_async(
        self,
        request: cbn_20170912_models.ListTransitRouterMulticastGroupsRequest,
    ) -> cbn_20170912_models.ListTransitRouterMulticastGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_transit_router_multicast_groups_with_options_async(request, runtime)

    def list_transit_router_peer_attachments_with_options(
        self,
        request: cbn_20170912_models.ListTransitRouterPeerAttachmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListTransitRouterPeerAttachmentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterPeerAttachments',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterPeerAttachmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_transit_router_peer_attachments_with_options_async(
        self,
        request: cbn_20170912_models.ListTransitRouterPeerAttachmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListTransitRouterPeerAttachmentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterPeerAttachments',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterPeerAttachmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_transit_router_peer_attachments(
        self,
        request: cbn_20170912_models.ListTransitRouterPeerAttachmentsRequest,
    ) -> cbn_20170912_models.ListTransitRouterPeerAttachmentsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_transit_router_peer_attachments_with_options(request, runtime)

    async def list_transit_router_peer_attachments_async(
        self,
        request: cbn_20170912_models.ListTransitRouterPeerAttachmentsRequest,
    ) -> cbn_20170912_models.ListTransitRouterPeerAttachmentsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_transit_router_peer_attachments_with_options_async(request, runtime)

    def list_transit_router_prefix_list_association_with_options(
        self,
        request: cbn_20170912_models.ListTransitRouterPrefixListAssociationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListTransitRouterPrefixListAssociationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_hop):
            query['NextHop'] = request.next_hop
        if not UtilClient.is_unset(request.next_hop_type):
            query['NextHopType'] = request.next_hop_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_uid):
            query['OwnerUid'] = request.owner_uid
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prefix_list_id):
            query['PrefixListId'] = request.prefix_list_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not UtilClient.is_unset(request.transit_router_table_id):
            query['TransitRouterTableId'] = request.transit_router_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterPrefixListAssociation',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterPrefixListAssociationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_transit_router_prefix_list_association_with_options_async(
        self,
        request: cbn_20170912_models.ListTransitRouterPrefixListAssociationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListTransitRouterPrefixListAssociationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_hop):
            query['NextHop'] = request.next_hop
        if not UtilClient.is_unset(request.next_hop_type):
            query['NextHopType'] = request.next_hop_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_uid):
            query['OwnerUid'] = request.owner_uid
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prefix_list_id):
            query['PrefixListId'] = request.prefix_list_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not UtilClient.is_unset(request.transit_router_table_id):
            query['TransitRouterTableId'] = request.transit_router_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterPrefixListAssociation',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterPrefixListAssociationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_transit_router_prefix_list_association(
        self,
        request: cbn_20170912_models.ListTransitRouterPrefixListAssociationRequest,
    ) -> cbn_20170912_models.ListTransitRouterPrefixListAssociationResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_transit_router_prefix_list_association_with_options(request, runtime)

    async def list_transit_router_prefix_list_association_async(
        self,
        request: cbn_20170912_models.ListTransitRouterPrefixListAssociationRequest,
    ) -> cbn_20170912_models.ListTransitRouterPrefixListAssociationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_transit_router_prefix_list_association_with_options_async(request, runtime)

    def list_transit_router_route_entries_with_options(
        self,
        request: cbn_20170912_models.ListTransitRouterRouteEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListTransitRouterRouteEntriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_route_entry_destination_cidr_block):
            query['TransitRouterRouteEntryDestinationCidrBlock'] = request.transit_router_route_entry_destination_cidr_block
        if not UtilClient.is_unset(request.transit_router_route_entry_ids):
            query['TransitRouterRouteEntryIds'] = request.transit_router_route_entry_ids
        if not UtilClient.is_unset(request.transit_router_route_entry_names):
            query['TransitRouterRouteEntryNames'] = request.transit_router_route_entry_names
        if not UtilClient.is_unset(request.transit_router_route_entry_status):
            query['TransitRouterRouteEntryStatus'] = request.transit_router_route_entry_status
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterRouteEntries',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterRouteEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_transit_router_route_entries_with_options_async(
        self,
        request: cbn_20170912_models.ListTransitRouterRouteEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListTransitRouterRouteEntriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_route_entry_destination_cidr_block):
            query['TransitRouterRouteEntryDestinationCidrBlock'] = request.transit_router_route_entry_destination_cidr_block
        if not UtilClient.is_unset(request.transit_router_route_entry_ids):
            query['TransitRouterRouteEntryIds'] = request.transit_router_route_entry_ids
        if not UtilClient.is_unset(request.transit_router_route_entry_names):
            query['TransitRouterRouteEntryNames'] = request.transit_router_route_entry_names
        if not UtilClient.is_unset(request.transit_router_route_entry_status):
            query['TransitRouterRouteEntryStatus'] = request.transit_router_route_entry_status
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterRouteEntries',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterRouteEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_transit_router_route_entries(
        self,
        request: cbn_20170912_models.ListTransitRouterRouteEntriesRequest,
    ) -> cbn_20170912_models.ListTransitRouterRouteEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_transit_router_route_entries_with_options(request, runtime)

    async def list_transit_router_route_entries_async(
        self,
        request: cbn_20170912_models.ListTransitRouterRouteEntriesRequest,
    ) -> cbn_20170912_models.ListTransitRouterRouteEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_transit_router_route_entries_with_options_async(request, runtime)

    def list_transit_router_route_table_associations_with_options(
        self,
        request: cbn_20170912_models.ListTransitRouterRouteTableAssociationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListTransitRouterRouteTableAssociationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterRouteTableAssociations',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterRouteTableAssociationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_transit_router_route_table_associations_with_options_async(
        self,
        request: cbn_20170912_models.ListTransitRouterRouteTableAssociationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListTransitRouterRouteTableAssociationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterRouteTableAssociations',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterRouteTableAssociationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_transit_router_route_table_associations(
        self,
        request: cbn_20170912_models.ListTransitRouterRouteTableAssociationsRequest,
    ) -> cbn_20170912_models.ListTransitRouterRouteTableAssociationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_transit_router_route_table_associations_with_options(request, runtime)

    async def list_transit_router_route_table_associations_async(
        self,
        request: cbn_20170912_models.ListTransitRouterRouteTableAssociationsRequest,
    ) -> cbn_20170912_models.ListTransitRouterRouteTableAssociationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_transit_router_route_table_associations_with_options_async(request, runtime)

    def list_transit_router_route_table_propagations_with_options(
        self,
        request: cbn_20170912_models.ListTransitRouterRouteTablePropagationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListTransitRouterRouteTablePropagationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterRouteTablePropagations',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterRouteTablePropagationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_transit_router_route_table_propagations_with_options_async(
        self,
        request: cbn_20170912_models.ListTransitRouterRouteTablePropagationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListTransitRouterRouteTablePropagationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterRouteTablePropagations',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterRouteTablePropagationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_transit_router_route_table_propagations(
        self,
        request: cbn_20170912_models.ListTransitRouterRouteTablePropagationsRequest,
    ) -> cbn_20170912_models.ListTransitRouterRouteTablePropagationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_transit_router_route_table_propagations_with_options(request, runtime)

    async def list_transit_router_route_table_propagations_async(
        self,
        request: cbn_20170912_models.ListTransitRouterRouteTablePropagationsRequest,
    ) -> cbn_20170912_models.ListTransitRouterRouteTablePropagationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_transit_router_route_table_propagations_with_options_async(request, runtime)

    def list_transit_router_route_tables_with_options(
        self,
        request: cbn_20170912_models.ListTransitRouterRouteTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListTransitRouterRouteTablesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not UtilClient.is_unset(request.transit_router_route_table_ids):
            query['TransitRouterRouteTableIds'] = request.transit_router_route_table_ids
        if not UtilClient.is_unset(request.transit_router_route_table_names):
            query['TransitRouterRouteTableNames'] = request.transit_router_route_table_names
        if not UtilClient.is_unset(request.transit_router_route_table_status):
            query['TransitRouterRouteTableStatus'] = request.transit_router_route_table_status
        if not UtilClient.is_unset(request.transit_router_route_table_type):
            query['TransitRouterRouteTableType'] = request.transit_router_route_table_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterRouteTables',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterRouteTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_transit_router_route_tables_with_options_async(
        self,
        request: cbn_20170912_models.ListTransitRouterRouteTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListTransitRouterRouteTablesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not UtilClient.is_unset(request.transit_router_route_table_ids):
            query['TransitRouterRouteTableIds'] = request.transit_router_route_table_ids
        if not UtilClient.is_unset(request.transit_router_route_table_names):
            query['TransitRouterRouteTableNames'] = request.transit_router_route_table_names
        if not UtilClient.is_unset(request.transit_router_route_table_status):
            query['TransitRouterRouteTableStatus'] = request.transit_router_route_table_status
        if not UtilClient.is_unset(request.transit_router_route_table_type):
            query['TransitRouterRouteTableType'] = request.transit_router_route_table_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterRouteTables',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterRouteTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_transit_router_route_tables(
        self,
        request: cbn_20170912_models.ListTransitRouterRouteTablesRequest,
    ) -> cbn_20170912_models.ListTransitRouterRouteTablesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_transit_router_route_tables_with_options(request, runtime)

    async def list_transit_router_route_tables_async(
        self,
        request: cbn_20170912_models.ListTransitRouterRouteTablesRequest,
    ) -> cbn_20170912_models.ListTransitRouterRouteTablesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_transit_router_route_tables_with_options_async(request, runtime)

    def list_transit_router_vbr_attachments_with_options(
        self,
        request: cbn_20170912_models.ListTransitRouterVbrAttachmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListTransitRouterVbrAttachmentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterVbrAttachments',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterVbrAttachmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_transit_router_vbr_attachments_with_options_async(
        self,
        request: cbn_20170912_models.ListTransitRouterVbrAttachmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListTransitRouterVbrAttachmentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterVbrAttachments',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterVbrAttachmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_transit_router_vbr_attachments(
        self,
        request: cbn_20170912_models.ListTransitRouterVbrAttachmentsRequest,
    ) -> cbn_20170912_models.ListTransitRouterVbrAttachmentsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_transit_router_vbr_attachments_with_options(request, runtime)

    async def list_transit_router_vbr_attachments_async(
        self,
        request: cbn_20170912_models.ListTransitRouterVbrAttachmentsRequest,
    ) -> cbn_20170912_models.ListTransitRouterVbrAttachmentsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_transit_router_vbr_attachments_with_options_async(request, runtime)

    def list_transit_router_vpc_attachments_with_options(
        self,
        request: cbn_20170912_models.ListTransitRouterVpcAttachmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListTransitRouterVpcAttachmentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterVpcAttachments',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterVpcAttachmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_transit_router_vpc_attachments_with_options_async(
        self,
        request: cbn_20170912_models.ListTransitRouterVpcAttachmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListTransitRouterVpcAttachmentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterVpcAttachments',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterVpcAttachmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_transit_router_vpc_attachments(
        self,
        request: cbn_20170912_models.ListTransitRouterVpcAttachmentsRequest,
    ) -> cbn_20170912_models.ListTransitRouterVpcAttachmentsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_transit_router_vpc_attachments_with_options(request, runtime)

    async def list_transit_router_vpc_attachments_async(
        self,
        request: cbn_20170912_models.ListTransitRouterVpcAttachmentsRequest,
    ) -> cbn_20170912_models.ListTransitRouterVpcAttachmentsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_transit_router_vpc_attachments_with_options_async(request, runtime)

    def list_transit_router_vpn_attachments_with_options(
        self,
        request: cbn_20170912_models.ListTransitRouterVpnAttachmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListTransitRouterVpnAttachmentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterVpnAttachments',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterVpnAttachmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_transit_router_vpn_attachments_with_options_async(
        self,
        request: cbn_20170912_models.ListTransitRouterVpnAttachmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListTransitRouterVpnAttachmentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterVpnAttachments',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterVpnAttachmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_transit_router_vpn_attachments(
        self,
        request: cbn_20170912_models.ListTransitRouterVpnAttachmentsRequest,
    ) -> cbn_20170912_models.ListTransitRouterVpnAttachmentsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_transit_router_vpn_attachments_with_options(request, runtime)

    async def list_transit_router_vpn_attachments_async(
        self,
        request: cbn_20170912_models.ListTransitRouterVpnAttachmentsRequest,
    ) -> cbn_20170912_models.ListTransitRouterVpnAttachmentsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_transit_router_vpn_attachments_with_options_async(request, runtime)

    def list_transit_routers_with_options(
        self,
        request: cbn_20170912_models.ListTransitRoutersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListTransitRoutersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouters',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRoutersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_transit_routers_with_options_async(
        self,
        request: cbn_20170912_models.ListTransitRoutersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListTransitRoutersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouters',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRoutersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_transit_routers(
        self,
        request: cbn_20170912_models.ListTransitRoutersRequest,
    ) -> cbn_20170912_models.ListTransitRoutersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_transit_routers_with_options(request, runtime)

    async def list_transit_routers_async(
        self,
        request: cbn_20170912_models.ListTransitRoutersRequest,
    ) -> cbn_20170912_models.ListTransitRoutersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_transit_routers_with_options_async(request, runtime)

    def modify_cen_attribute_with_options(
        self,
        request: cbn_20170912_models.ModifyCenAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ModifyCenAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.protection_level):
            query['ProtectionLevel'] = request.protection_level
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCenAttribute',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ModifyCenAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cen_attribute_with_options_async(
        self,
        request: cbn_20170912_models.ModifyCenAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ModifyCenAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.protection_level):
            query['ProtectionLevel'] = request.protection_level
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCenAttribute',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ModifyCenAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cen_attribute(
        self,
        request: cbn_20170912_models.ModifyCenAttributeRequest,
    ) -> cbn_20170912_models.ModifyCenAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_cen_attribute_with_options(request, runtime)

    async def modify_cen_attribute_async(
        self,
        request: cbn_20170912_models.ModifyCenAttributeRequest,
    ) -> cbn_20170912_models.ModifyCenAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_cen_attribute_with_options_async(request, runtime)

    def modify_cen_bandwidth_package_attribute_with_options(
        self,
        request: cbn_20170912_models.ModifyCenBandwidthPackageAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ModifyCenBandwidthPackageAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_bandwidth_package_id):
            query['CenBandwidthPackageId'] = request.cen_bandwidth_package_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCenBandwidthPackageAttribute',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ModifyCenBandwidthPackageAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cen_bandwidth_package_attribute_with_options_async(
        self,
        request: cbn_20170912_models.ModifyCenBandwidthPackageAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ModifyCenBandwidthPackageAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_bandwidth_package_id):
            query['CenBandwidthPackageId'] = request.cen_bandwidth_package_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCenBandwidthPackageAttribute',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ModifyCenBandwidthPackageAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cen_bandwidth_package_attribute(
        self,
        request: cbn_20170912_models.ModifyCenBandwidthPackageAttributeRequest,
    ) -> cbn_20170912_models.ModifyCenBandwidthPackageAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_cen_bandwidth_package_attribute_with_options(request, runtime)

    async def modify_cen_bandwidth_package_attribute_async(
        self,
        request: cbn_20170912_models.ModifyCenBandwidthPackageAttributeRequest,
    ) -> cbn_20170912_models.ModifyCenBandwidthPackageAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_cen_bandwidth_package_attribute_with_options_async(request, runtime)

    def modify_cen_bandwidth_package_spec_with_options(
        self,
        request: cbn_20170912_models.ModifyCenBandwidthPackageSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ModifyCenBandwidthPackageSpecResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.cen_bandwidth_package_id):
            query['CenBandwidthPackageId'] = request.cen_bandwidth_package_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCenBandwidthPackageSpec',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ModifyCenBandwidthPackageSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cen_bandwidth_package_spec_with_options_async(
        self,
        request: cbn_20170912_models.ModifyCenBandwidthPackageSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ModifyCenBandwidthPackageSpecResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.cen_bandwidth_package_id):
            query['CenBandwidthPackageId'] = request.cen_bandwidth_package_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCenBandwidthPackageSpec',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ModifyCenBandwidthPackageSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cen_bandwidth_package_spec(
        self,
        request: cbn_20170912_models.ModifyCenBandwidthPackageSpecRequest,
    ) -> cbn_20170912_models.ModifyCenBandwidthPackageSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_cen_bandwidth_package_spec_with_options(request, runtime)

    async def modify_cen_bandwidth_package_spec_async(
        self,
        request: cbn_20170912_models.ModifyCenBandwidthPackageSpecRequest,
    ) -> cbn_20170912_models.ModifyCenBandwidthPackageSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_cen_bandwidth_package_spec_with_options_async(request, runtime)

    def modify_cen_route_map_with_options(
        self,
        request: cbn_20170912_models.ModifyCenRouteMapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ModifyCenRouteMapResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.as_path_match_mode):
            query['AsPathMatchMode'] = request.as_path_match_mode
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.cen_region_id):
            query['CenRegionId'] = request.cen_region_id
        if not UtilClient.is_unset(request.cidr_match_mode):
            query['CidrMatchMode'] = request.cidr_match_mode
        if not UtilClient.is_unset(request.community_match_mode):
            query['CommunityMatchMode'] = request.community_match_mode
        if not UtilClient.is_unset(request.community_operate_mode):
            query['CommunityOperateMode'] = request.community_operate_mode
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination_child_instance_types):
            query['DestinationChildInstanceTypes'] = request.destination_child_instance_types
        if not UtilClient.is_unset(request.destination_cidr_blocks):
            query['DestinationCidrBlocks'] = request.destination_cidr_blocks
        if not UtilClient.is_unset(request.destination_instance_ids):
            query['DestinationInstanceIds'] = request.destination_instance_ids
        if not UtilClient.is_unset(request.destination_instance_ids_reverse_match):
            query['DestinationInstanceIdsReverseMatch'] = request.destination_instance_ids_reverse_match
        if not UtilClient.is_unset(request.destination_route_table_ids):
            query['DestinationRouteTableIds'] = request.destination_route_table_ids
        if not UtilClient.is_unset(request.map_result):
            query['MapResult'] = request.map_result
        if not UtilClient.is_unset(request.match_address_type):
            query['MatchAddressType'] = request.match_address_type
        if not UtilClient.is_unset(request.match_asns):
            query['MatchAsns'] = request.match_asns
        if not UtilClient.is_unset(request.match_community_set):
            query['MatchCommunitySet'] = request.match_community_set
        if not UtilClient.is_unset(request.next_priority):
            query['NextPriority'] = request.next_priority
        if not UtilClient.is_unset(request.operate_community_set):
            query['OperateCommunitySet'] = request.operate_community_set
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.preference):
            query['Preference'] = request.preference
        if not UtilClient.is_unset(request.prepend_as_path):
            query['PrependAsPath'] = request.prepend_as_path
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.route_map_id):
            query['RouteMapId'] = request.route_map_id
        if not UtilClient.is_unset(request.route_types):
            query['RouteTypes'] = request.route_types
        if not UtilClient.is_unset(request.source_child_instance_types):
            query['SourceChildInstanceTypes'] = request.source_child_instance_types
        if not UtilClient.is_unset(request.source_instance_ids):
            query['SourceInstanceIds'] = request.source_instance_ids
        if not UtilClient.is_unset(request.source_instance_ids_reverse_match):
            query['SourceInstanceIdsReverseMatch'] = request.source_instance_ids_reverse_match
        if not UtilClient.is_unset(request.source_region_ids):
            query['SourceRegionIds'] = request.source_region_ids
        if not UtilClient.is_unset(request.source_route_table_ids):
            query['SourceRouteTableIds'] = request.source_route_table_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCenRouteMap',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ModifyCenRouteMapResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cen_route_map_with_options_async(
        self,
        request: cbn_20170912_models.ModifyCenRouteMapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ModifyCenRouteMapResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.as_path_match_mode):
            query['AsPathMatchMode'] = request.as_path_match_mode
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.cen_region_id):
            query['CenRegionId'] = request.cen_region_id
        if not UtilClient.is_unset(request.cidr_match_mode):
            query['CidrMatchMode'] = request.cidr_match_mode
        if not UtilClient.is_unset(request.community_match_mode):
            query['CommunityMatchMode'] = request.community_match_mode
        if not UtilClient.is_unset(request.community_operate_mode):
            query['CommunityOperateMode'] = request.community_operate_mode
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination_child_instance_types):
            query['DestinationChildInstanceTypes'] = request.destination_child_instance_types
        if not UtilClient.is_unset(request.destination_cidr_blocks):
            query['DestinationCidrBlocks'] = request.destination_cidr_blocks
        if not UtilClient.is_unset(request.destination_instance_ids):
            query['DestinationInstanceIds'] = request.destination_instance_ids
        if not UtilClient.is_unset(request.destination_instance_ids_reverse_match):
            query['DestinationInstanceIdsReverseMatch'] = request.destination_instance_ids_reverse_match
        if not UtilClient.is_unset(request.destination_route_table_ids):
            query['DestinationRouteTableIds'] = request.destination_route_table_ids
        if not UtilClient.is_unset(request.map_result):
            query['MapResult'] = request.map_result
        if not UtilClient.is_unset(request.match_address_type):
            query['MatchAddressType'] = request.match_address_type
        if not UtilClient.is_unset(request.match_asns):
            query['MatchAsns'] = request.match_asns
        if not UtilClient.is_unset(request.match_community_set):
            query['MatchCommunitySet'] = request.match_community_set
        if not UtilClient.is_unset(request.next_priority):
            query['NextPriority'] = request.next_priority
        if not UtilClient.is_unset(request.operate_community_set):
            query['OperateCommunitySet'] = request.operate_community_set
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.preference):
            query['Preference'] = request.preference
        if not UtilClient.is_unset(request.prepend_as_path):
            query['PrependAsPath'] = request.prepend_as_path
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.route_map_id):
            query['RouteMapId'] = request.route_map_id
        if not UtilClient.is_unset(request.route_types):
            query['RouteTypes'] = request.route_types
        if not UtilClient.is_unset(request.source_child_instance_types):
            query['SourceChildInstanceTypes'] = request.source_child_instance_types
        if not UtilClient.is_unset(request.source_instance_ids):
            query['SourceInstanceIds'] = request.source_instance_ids
        if not UtilClient.is_unset(request.source_instance_ids_reverse_match):
            query['SourceInstanceIdsReverseMatch'] = request.source_instance_ids_reverse_match
        if not UtilClient.is_unset(request.source_region_ids):
            query['SourceRegionIds'] = request.source_region_ids
        if not UtilClient.is_unset(request.source_route_table_ids):
            query['SourceRouteTableIds'] = request.source_route_table_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCenRouteMap',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ModifyCenRouteMapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cen_route_map(
        self,
        request: cbn_20170912_models.ModifyCenRouteMapRequest,
    ) -> cbn_20170912_models.ModifyCenRouteMapResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_cen_route_map_with_options(request, runtime)

    async def modify_cen_route_map_async(
        self,
        request: cbn_20170912_models.ModifyCenRouteMapRequest,
    ) -> cbn_20170912_models.ModifyCenRouteMapResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_cen_route_map_with_options_async(request, runtime)

    def modify_flow_log_attribute_with_options(
        self,
        request: cbn_20170912_models.ModifyFlowLogAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ModifyFlowLogAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not UtilClient.is_unset(request.flow_log_name):
            query['FlowLogName'] = request.flow_log_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyFlowLogAttribute',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ModifyFlowLogAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_flow_log_attribute_with_options_async(
        self,
        request: cbn_20170912_models.ModifyFlowLogAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ModifyFlowLogAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not UtilClient.is_unset(request.flow_log_name):
            query['FlowLogName'] = request.flow_log_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyFlowLogAttribute',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ModifyFlowLogAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_flow_log_attribute(
        self,
        request: cbn_20170912_models.ModifyFlowLogAttributeRequest,
    ) -> cbn_20170912_models.ModifyFlowLogAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_flow_log_attribute_with_options(request, runtime)

    async def modify_flow_log_attribute_async(
        self,
        request: cbn_20170912_models.ModifyFlowLogAttributeRequest,
    ) -> cbn_20170912_models.ModifyFlowLogAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_flow_log_attribute_with_options_async(request, runtime)

    def modify_transit_router_cidr_with_options(
        self,
        request: cbn_20170912_models.ModifyTransitRouterCidrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ModifyTransitRouterCidrResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cidr):
            query['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.publish_cidr_route):
            query['PublishCidrRoute'] = request.publish_cidr_route
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_cidr_id):
            query['TransitRouterCidrId'] = request.transit_router_cidr_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTransitRouterCidr',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ModifyTransitRouterCidrResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_transit_router_cidr_with_options_async(
        self,
        request: cbn_20170912_models.ModifyTransitRouterCidrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ModifyTransitRouterCidrResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cidr):
            query['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.publish_cidr_route):
            query['PublishCidrRoute'] = request.publish_cidr_route
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_cidr_id):
            query['TransitRouterCidrId'] = request.transit_router_cidr_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTransitRouterCidr',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ModifyTransitRouterCidrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_transit_router_cidr(
        self,
        request: cbn_20170912_models.ModifyTransitRouterCidrRequest,
    ) -> cbn_20170912_models.ModifyTransitRouterCidrResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_transit_router_cidr_with_options(request, runtime)

    async def modify_transit_router_cidr_async(
        self,
        request: cbn_20170912_models.ModifyTransitRouterCidrRequest,
    ) -> cbn_20170912_models.ModifyTransitRouterCidrResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_transit_router_cidr_with_options_async(request, runtime)

    def modify_transit_router_multicast_domain_with_options(
        self,
        request: cbn_20170912_models.ModifyTransitRouterMulticastDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ModifyTransitRouterMulticastDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_multicast_domain_description):
            query['TransitRouterMulticastDomainDescription'] = request.transit_router_multicast_domain_description
        if not UtilClient.is_unset(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        if not UtilClient.is_unset(request.transit_router_multicast_domain_name):
            query['TransitRouterMulticastDomainName'] = request.transit_router_multicast_domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTransitRouterMulticastDomain',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ModifyTransitRouterMulticastDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_transit_router_multicast_domain_with_options_async(
        self,
        request: cbn_20170912_models.ModifyTransitRouterMulticastDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ModifyTransitRouterMulticastDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_multicast_domain_description):
            query['TransitRouterMulticastDomainDescription'] = request.transit_router_multicast_domain_description
        if not UtilClient.is_unset(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        if not UtilClient.is_unset(request.transit_router_multicast_domain_name):
            query['TransitRouterMulticastDomainName'] = request.transit_router_multicast_domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTransitRouterMulticastDomain',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ModifyTransitRouterMulticastDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_transit_router_multicast_domain(
        self,
        request: cbn_20170912_models.ModifyTransitRouterMulticastDomainRequest,
    ) -> cbn_20170912_models.ModifyTransitRouterMulticastDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_transit_router_multicast_domain_with_options(request, runtime)

    async def modify_transit_router_multicast_domain_async(
        self,
        request: cbn_20170912_models.ModifyTransitRouterMulticastDomainRequest,
    ) -> cbn_20170912_models.ModifyTransitRouterMulticastDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_transit_router_multicast_domain_with_options_async(request, runtime)

    def move_resource_group_with_options(
        self,
        request: cbn_20170912_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.MoveResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveResourceGroup',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.MoveResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_resource_group_with_options_async(
        self,
        request: cbn_20170912_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.MoveResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveResourceGroup',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.MoveResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_resource_group(
        self,
        request: cbn_20170912_models.MoveResourceGroupRequest,
    ) -> cbn_20170912_models.MoveResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    async def move_resource_group_async(
        self,
        request: cbn_20170912_models.MoveResourceGroupRequest,
    ) -> cbn_20170912_models.MoveResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.move_resource_group_with_options_async(request, runtime)

    def open_transit_router_service_with_options(
        self,
        request: cbn_20170912_models.OpenTransitRouterServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.OpenTransitRouterServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenTransitRouterService',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.OpenTransitRouterServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_transit_router_service_with_options_async(
        self,
        request: cbn_20170912_models.OpenTransitRouterServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.OpenTransitRouterServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenTransitRouterService',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.OpenTransitRouterServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_transit_router_service(
        self,
        request: cbn_20170912_models.OpenTransitRouterServiceRequest,
    ) -> cbn_20170912_models.OpenTransitRouterServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_transit_router_service_with_options(request, runtime)

    async def open_transit_router_service_async(
        self,
        request: cbn_20170912_models.OpenTransitRouterServiceRequest,
    ) -> cbn_20170912_models.OpenTransitRouterServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_transit_router_service_with_options_async(request, runtime)

    def publish_route_entries_with_options(
        self,
        request: cbn_20170912_models.PublishRouteEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.PublishRouteEntriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not UtilClient.is_unset(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not UtilClient.is_unset(request.child_instance_route_table_id):
            query['ChildInstanceRouteTableId'] = request.child_instance_route_table_id
        if not UtilClient.is_unset(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not UtilClient.is_unset(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishRouteEntries',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.PublishRouteEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_route_entries_with_options_async(
        self,
        request: cbn_20170912_models.PublishRouteEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.PublishRouteEntriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not UtilClient.is_unset(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not UtilClient.is_unset(request.child_instance_route_table_id):
            query['ChildInstanceRouteTableId'] = request.child_instance_route_table_id
        if not UtilClient.is_unset(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not UtilClient.is_unset(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishRouteEntries',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.PublishRouteEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_route_entries(
        self,
        request: cbn_20170912_models.PublishRouteEntriesRequest,
    ) -> cbn_20170912_models.PublishRouteEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.publish_route_entries_with_options(request, runtime)

    async def publish_route_entries_async(
        self,
        request: cbn_20170912_models.PublishRouteEntriesRequest,
    ) -> cbn_20170912_models.PublishRouteEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.publish_route_entries_with_options_async(request, runtime)

    def register_transit_router_multicast_group_members_with_options(
        self,
        request: cbn_20170912_models.RegisterTransitRouterMulticastGroupMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.RegisterTransitRouterMulticastGroupMembersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.group_ip_address):
            query['GroupIpAddress'] = request.group_ip_address
        if not UtilClient.is_unset(request.network_interface_ids):
            query['NetworkInterfaceIds'] = request.network_interface_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.peer_transit_router_multicast_domains):
            query['PeerTransitRouterMulticastDomains'] = request.peer_transit_router_multicast_domains
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterTransitRouterMulticastGroupMembers',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.RegisterTransitRouterMulticastGroupMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_transit_router_multicast_group_members_with_options_async(
        self,
        request: cbn_20170912_models.RegisterTransitRouterMulticastGroupMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.RegisterTransitRouterMulticastGroupMembersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.group_ip_address):
            query['GroupIpAddress'] = request.group_ip_address
        if not UtilClient.is_unset(request.network_interface_ids):
            query['NetworkInterfaceIds'] = request.network_interface_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.peer_transit_router_multicast_domains):
            query['PeerTransitRouterMulticastDomains'] = request.peer_transit_router_multicast_domains
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterTransitRouterMulticastGroupMembers',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.RegisterTransitRouterMulticastGroupMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_transit_router_multicast_group_members(
        self,
        request: cbn_20170912_models.RegisterTransitRouterMulticastGroupMembersRequest,
    ) -> cbn_20170912_models.RegisterTransitRouterMulticastGroupMembersResponse:
        runtime = util_models.RuntimeOptions()
        return self.register_transit_router_multicast_group_members_with_options(request, runtime)

    async def register_transit_router_multicast_group_members_async(
        self,
        request: cbn_20170912_models.RegisterTransitRouterMulticastGroupMembersRequest,
    ) -> cbn_20170912_models.RegisterTransitRouterMulticastGroupMembersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.register_transit_router_multicast_group_members_with_options_async(request, runtime)

    def register_transit_router_multicast_group_sources_with_options(
        self,
        request: cbn_20170912_models.RegisterTransitRouterMulticastGroupSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.RegisterTransitRouterMulticastGroupSourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.group_ip_address):
            query['GroupIpAddress'] = request.group_ip_address
        if not UtilClient.is_unset(request.network_interface_ids):
            query['NetworkInterfaceIds'] = request.network_interface_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterTransitRouterMulticastGroupSources',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.RegisterTransitRouterMulticastGroupSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_transit_router_multicast_group_sources_with_options_async(
        self,
        request: cbn_20170912_models.RegisterTransitRouterMulticastGroupSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.RegisterTransitRouterMulticastGroupSourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.group_ip_address):
            query['GroupIpAddress'] = request.group_ip_address
        if not UtilClient.is_unset(request.network_interface_ids):
            query['NetworkInterfaceIds'] = request.network_interface_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterTransitRouterMulticastGroupSources',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.RegisterTransitRouterMulticastGroupSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_transit_router_multicast_group_sources(
        self,
        request: cbn_20170912_models.RegisterTransitRouterMulticastGroupSourcesRequest,
    ) -> cbn_20170912_models.RegisterTransitRouterMulticastGroupSourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.register_transit_router_multicast_group_sources_with_options(request, runtime)

    async def register_transit_router_multicast_group_sources_async(
        self,
        request: cbn_20170912_models.RegisterTransitRouterMulticastGroupSourcesRequest,
    ) -> cbn_20170912_models.RegisterTransitRouterMulticastGroupSourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.register_transit_router_multicast_group_sources_with_options_async(request, runtime)

    def remove_traffic_match_rule_from_traffic_marking_policy_with_options(
        self,
        request: cbn_20170912_models.RemoveTrafficMatchRuleFromTrafficMarkingPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.RemoveTrafficMatchRuleFromTrafficMarkingPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.traffic_mark_rule_ids):
            query['TrafficMarkRuleIds'] = request.traffic_mark_rule_ids
        if not UtilClient.is_unset(request.traffic_marking_policy_id):
            query['TrafficMarkingPolicyId'] = request.traffic_marking_policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveTrafficMatchRuleFromTrafficMarkingPolicy',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.RemoveTrafficMatchRuleFromTrafficMarkingPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_traffic_match_rule_from_traffic_marking_policy_with_options_async(
        self,
        request: cbn_20170912_models.RemoveTrafficMatchRuleFromTrafficMarkingPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.RemoveTrafficMatchRuleFromTrafficMarkingPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.traffic_mark_rule_ids):
            query['TrafficMarkRuleIds'] = request.traffic_mark_rule_ids
        if not UtilClient.is_unset(request.traffic_marking_policy_id):
            query['TrafficMarkingPolicyId'] = request.traffic_marking_policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveTrafficMatchRuleFromTrafficMarkingPolicy',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.RemoveTrafficMatchRuleFromTrafficMarkingPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_traffic_match_rule_from_traffic_marking_policy(
        self,
        request: cbn_20170912_models.RemoveTrafficMatchRuleFromTrafficMarkingPolicyRequest,
    ) -> cbn_20170912_models.RemoveTrafficMatchRuleFromTrafficMarkingPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_traffic_match_rule_from_traffic_marking_policy_with_options(request, runtime)

    async def remove_traffic_match_rule_from_traffic_marking_policy_async(
        self,
        request: cbn_20170912_models.RemoveTrafficMatchRuleFromTrafficMarkingPolicyRequest,
    ) -> cbn_20170912_models.RemoveTrafficMatchRuleFromTrafficMarkingPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_traffic_match_rule_from_traffic_marking_policy_with_options_async(request, runtime)

    def remove_trafic_match_rule_from_traffic_marking_policy_with_options(
        self,
        request: cbn_20170912_models.RemoveTraficMatchRuleFromTrafficMarkingPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.RemoveTraficMatchRuleFromTrafficMarkingPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.traffic_mark_rule_ids):
            query['TrafficMarkRuleIds'] = request.traffic_mark_rule_ids
        if not UtilClient.is_unset(request.traffic_marking_policy_id):
            query['TrafficMarkingPolicyId'] = request.traffic_marking_policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveTraficMatchRuleFromTrafficMarkingPolicy',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.RemoveTraficMatchRuleFromTrafficMarkingPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_trafic_match_rule_from_traffic_marking_policy_with_options_async(
        self,
        request: cbn_20170912_models.RemoveTraficMatchRuleFromTrafficMarkingPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.RemoveTraficMatchRuleFromTrafficMarkingPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.traffic_mark_rule_ids):
            query['TrafficMarkRuleIds'] = request.traffic_mark_rule_ids
        if not UtilClient.is_unset(request.traffic_marking_policy_id):
            query['TrafficMarkingPolicyId'] = request.traffic_marking_policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveTraficMatchRuleFromTrafficMarkingPolicy',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.RemoveTraficMatchRuleFromTrafficMarkingPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_trafic_match_rule_from_traffic_marking_policy(
        self,
        request: cbn_20170912_models.RemoveTraficMatchRuleFromTrafficMarkingPolicyRequest,
    ) -> cbn_20170912_models.RemoveTraficMatchRuleFromTrafficMarkingPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_trafic_match_rule_from_traffic_marking_policy_with_options(request, runtime)

    async def remove_trafic_match_rule_from_traffic_marking_policy_async(
        self,
        request: cbn_20170912_models.RemoveTraficMatchRuleFromTrafficMarkingPolicyRequest,
    ) -> cbn_20170912_models.RemoveTraficMatchRuleFromTrafficMarkingPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_trafic_match_rule_from_traffic_marking_policy_with_options_async(request, runtime)

    def replace_transit_router_route_table_association_with_options(
        self,
        request: cbn_20170912_models.ReplaceTransitRouterRouteTableAssociationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ReplaceTransitRouterRouteTableAssociationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReplaceTransitRouterRouteTableAssociation',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ReplaceTransitRouterRouteTableAssociationResponse(),
            self.call_api(params, req, runtime)
        )

    async def replace_transit_router_route_table_association_with_options_async(
        self,
        request: cbn_20170912_models.ReplaceTransitRouterRouteTableAssociationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ReplaceTransitRouterRouteTableAssociationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReplaceTransitRouterRouteTableAssociation',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ReplaceTransitRouterRouteTableAssociationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def replace_transit_router_route_table_association(
        self,
        request: cbn_20170912_models.ReplaceTransitRouterRouteTableAssociationRequest,
    ) -> cbn_20170912_models.ReplaceTransitRouterRouteTableAssociationResponse:
        runtime = util_models.RuntimeOptions()
        return self.replace_transit_router_route_table_association_with_options(request, runtime)

    async def replace_transit_router_route_table_association_async(
        self,
        request: cbn_20170912_models.ReplaceTransitRouterRouteTableAssociationRequest,
    ) -> cbn_20170912_models.ReplaceTransitRouterRouteTableAssociationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.replace_transit_router_route_table_association_with_options_async(request, runtime)

    def resolve_and_route_service_in_cen_with_options(
        self,
        request: cbn_20170912_models.ResolveAndRouteServiceInCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ResolveAndRouteServiceInCenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_region_ids):
            query['AccessRegionIds'] = request.access_region_ids
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.host):
            query['Host'] = request.host
        if not UtilClient.is_unset(request.host_region_id):
            query['HostRegionId'] = request.host_region_id
        if not UtilClient.is_unset(request.host_vpc_id):
            query['HostVpcId'] = request.host_vpc_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResolveAndRouteServiceInCen',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ResolveAndRouteServiceInCenResponse(),
            self.call_api(params, req, runtime)
        )

    async def resolve_and_route_service_in_cen_with_options_async(
        self,
        request: cbn_20170912_models.ResolveAndRouteServiceInCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ResolveAndRouteServiceInCenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_region_ids):
            query['AccessRegionIds'] = request.access_region_ids
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.host):
            query['Host'] = request.host
        if not UtilClient.is_unset(request.host_region_id):
            query['HostRegionId'] = request.host_region_id
        if not UtilClient.is_unset(request.host_vpc_id):
            query['HostVpcId'] = request.host_vpc_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResolveAndRouteServiceInCen',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ResolveAndRouteServiceInCenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resolve_and_route_service_in_cen(
        self,
        request: cbn_20170912_models.ResolveAndRouteServiceInCenRequest,
    ) -> cbn_20170912_models.ResolveAndRouteServiceInCenResponse:
        runtime = util_models.RuntimeOptions()
        return self.resolve_and_route_service_in_cen_with_options(request, runtime)

    async def resolve_and_route_service_in_cen_async(
        self,
        request: cbn_20170912_models.ResolveAndRouteServiceInCenRequest,
    ) -> cbn_20170912_models.ResolveAndRouteServiceInCenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resolve_and_route_service_in_cen_with_options_async(request, runtime)

    def revoke_instance_from_transit_router_with_options(
        self,
        request: cbn_20170912_models.RevokeInstanceFromTransitRouterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.RevokeInstanceFromTransitRouterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.cen_owner_id):
            query['CenOwnerId'] = request.cen_owner_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeInstanceFromTransitRouter',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.RevokeInstanceFromTransitRouterResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_instance_from_transit_router_with_options_async(
        self,
        request: cbn_20170912_models.RevokeInstanceFromTransitRouterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.RevokeInstanceFromTransitRouterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.cen_owner_id):
            query['CenOwnerId'] = request.cen_owner_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeInstanceFromTransitRouter',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.RevokeInstanceFromTransitRouterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_instance_from_transit_router(
        self,
        request: cbn_20170912_models.RevokeInstanceFromTransitRouterRequest,
    ) -> cbn_20170912_models.RevokeInstanceFromTransitRouterResponse:
        runtime = util_models.RuntimeOptions()
        return self.revoke_instance_from_transit_router_with_options(request, runtime)

    async def revoke_instance_from_transit_router_async(
        self,
        request: cbn_20170912_models.RevokeInstanceFromTransitRouterRequest,
    ) -> cbn_20170912_models.RevokeInstanceFromTransitRouterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.revoke_instance_from_transit_router_with_options_async(request, runtime)

    def route_private_zone_in_cen_to_vpc_with_options(
        self,
        request: cbn_20170912_models.RoutePrivateZoneInCenToVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.RoutePrivateZoneInCenToVpcResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_region_id):
            query['AccessRegionId'] = request.access_region_id
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.host_region_id):
            query['HostRegionId'] = request.host_region_id
        if not UtilClient.is_unset(request.host_vpc_id):
            query['HostVpcId'] = request.host_vpc_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RoutePrivateZoneInCenToVpc',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.RoutePrivateZoneInCenToVpcResponse(),
            self.call_api(params, req, runtime)
        )

    async def route_private_zone_in_cen_to_vpc_with_options_async(
        self,
        request: cbn_20170912_models.RoutePrivateZoneInCenToVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.RoutePrivateZoneInCenToVpcResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_region_id):
            query['AccessRegionId'] = request.access_region_id
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.host_region_id):
            query['HostRegionId'] = request.host_region_id
        if not UtilClient.is_unset(request.host_vpc_id):
            query['HostVpcId'] = request.host_vpc_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RoutePrivateZoneInCenToVpc',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.RoutePrivateZoneInCenToVpcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def route_private_zone_in_cen_to_vpc(
        self,
        request: cbn_20170912_models.RoutePrivateZoneInCenToVpcRequest,
    ) -> cbn_20170912_models.RoutePrivateZoneInCenToVpcResponse:
        runtime = util_models.RuntimeOptions()
        return self.route_private_zone_in_cen_to_vpc_with_options(request, runtime)

    async def route_private_zone_in_cen_to_vpc_async(
        self,
        request: cbn_20170912_models.RoutePrivateZoneInCenToVpcRequest,
    ) -> cbn_20170912_models.RoutePrivateZoneInCenToVpcResponse:
        runtime = util_models.RuntimeOptions()
        return await self.route_private_zone_in_cen_to_vpc_with_options_async(request, runtime)

    def set_cen_inter_region_bandwidth_limit_with_options(
        self,
        request: cbn_20170912_models.SetCenInterRegionBandwidthLimitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.SetCenInterRegionBandwidthLimitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth_limit):
            query['BandwidthLimit'] = request.bandwidth_limit
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.local_region_id):
            query['LocalRegionId'] = request.local_region_id
        if not UtilClient.is_unset(request.opposite_region_id):
            query['OppositeRegionId'] = request.opposite_region_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetCenInterRegionBandwidthLimit',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.SetCenInterRegionBandwidthLimitResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_cen_inter_region_bandwidth_limit_with_options_async(
        self,
        request: cbn_20170912_models.SetCenInterRegionBandwidthLimitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.SetCenInterRegionBandwidthLimitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth_limit):
            query['BandwidthLimit'] = request.bandwidth_limit
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.local_region_id):
            query['LocalRegionId'] = request.local_region_id
        if not UtilClient.is_unset(request.opposite_region_id):
            query['OppositeRegionId'] = request.opposite_region_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetCenInterRegionBandwidthLimit',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.SetCenInterRegionBandwidthLimitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_cen_inter_region_bandwidth_limit(
        self,
        request: cbn_20170912_models.SetCenInterRegionBandwidthLimitRequest,
    ) -> cbn_20170912_models.SetCenInterRegionBandwidthLimitResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_cen_inter_region_bandwidth_limit_with_options(request, runtime)

    async def set_cen_inter_region_bandwidth_limit_async(
        self,
        request: cbn_20170912_models.SetCenInterRegionBandwidthLimitRequest,
    ) -> cbn_20170912_models.SetCenInterRegionBandwidthLimitResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_cen_inter_region_bandwidth_limit_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: cbn_20170912_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: cbn_20170912_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: cbn_20170912_models.TagResourcesRequest,
    ) -> cbn_20170912_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: cbn_20170912_models.TagResourcesRequest,
    ) -> cbn_20170912_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def temp_upgrade_cen_bandwidth_package_spec_with_options(
        self,
        request: cbn_20170912_models.TempUpgradeCenBandwidthPackageSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.TempUpgradeCenBandwidthPackageSpecResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.cen_bandwidth_package_id):
            query['CenBandwidthPackageId'] = request.cen_bandwidth_package_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TempUpgradeCenBandwidthPackageSpec',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.TempUpgradeCenBandwidthPackageSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def temp_upgrade_cen_bandwidth_package_spec_with_options_async(
        self,
        request: cbn_20170912_models.TempUpgradeCenBandwidthPackageSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.TempUpgradeCenBandwidthPackageSpecResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.cen_bandwidth_package_id):
            query['CenBandwidthPackageId'] = request.cen_bandwidth_package_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TempUpgradeCenBandwidthPackageSpec',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.TempUpgradeCenBandwidthPackageSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def temp_upgrade_cen_bandwidth_package_spec(
        self,
        request: cbn_20170912_models.TempUpgradeCenBandwidthPackageSpecRequest,
    ) -> cbn_20170912_models.TempUpgradeCenBandwidthPackageSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.temp_upgrade_cen_bandwidth_package_spec_with_options(request, runtime)

    async def temp_upgrade_cen_bandwidth_package_spec_async(
        self,
        request: cbn_20170912_models.TempUpgradeCenBandwidthPackageSpecRequest,
    ) -> cbn_20170912_models.TempUpgradeCenBandwidthPackageSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.temp_upgrade_cen_bandwidth_package_spec_with_options_async(request, runtime)

    def unassociate_cen_bandwidth_package_with_options(
        self,
        request: cbn_20170912_models.UnassociateCenBandwidthPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.UnassociateCenBandwidthPackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_bandwidth_package_id):
            query['CenBandwidthPackageId'] = request.cen_bandwidth_package_id
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnassociateCenBandwidthPackage',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UnassociateCenBandwidthPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def unassociate_cen_bandwidth_package_with_options_async(
        self,
        request: cbn_20170912_models.UnassociateCenBandwidthPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.UnassociateCenBandwidthPackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_bandwidth_package_id):
            query['CenBandwidthPackageId'] = request.cen_bandwidth_package_id
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnassociateCenBandwidthPackage',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UnassociateCenBandwidthPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unassociate_cen_bandwidth_package(
        self,
        request: cbn_20170912_models.UnassociateCenBandwidthPackageRequest,
    ) -> cbn_20170912_models.UnassociateCenBandwidthPackageResponse:
        runtime = util_models.RuntimeOptions()
        return self.unassociate_cen_bandwidth_package_with_options(request, runtime)

    async def unassociate_cen_bandwidth_package_async(
        self,
        request: cbn_20170912_models.UnassociateCenBandwidthPackageRequest,
    ) -> cbn_20170912_models.UnassociateCenBandwidthPackageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unassociate_cen_bandwidth_package_with_options_async(request, runtime)

    def unroute_private_zone_in_cen_to_vpc_with_options(
        self,
        request: cbn_20170912_models.UnroutePrivateZoneInCenToVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.UnroutePrivateZoneInCenToVpcResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_region_id):
            query['AccessRegionId'] = request.access_region_id
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnroutePrivateZoneInCenToVpc',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UnroutePrivateZoneInCenToVpcResponse(),
            self.call_api(params, req, runtime)
        )

    async def unroute_private_zone_in_cen_to_vpc_with_options_async(
        self,
        request: cbn_20170912_models.UnroutePrivateZoneInCenToVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.UnroutePrivateZoneInCenToVpcResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_region_id):
            query['AccessRegionId'] = request.access_region_id
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnroutePrivateZoneInCenToVpc',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UnroutePrivateZoneInCenToVpcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unroute_private_zone_in_cen_to_vpc(
        self,
        request: cbn_20170912_models.UnroutePrivateZoneInCenToVpcRequest,
    ) -> cbn_20170912_models.UnroutePrivateZoneInCenToVpcResponse:
        runtime = util_models.RuntimeOptions()
        return self.unroute_private_zone_in_cen_to_vpc_with_options(request, runtime)

    async def unroute_private_zone_in_cen_to_vpc_async(
        self,
        request: cbn_20170912_models.UnroutePrivateZoneInCenToVpcRequest,
    ) -> cbn_20170912_models.UnroutePrivateZoneInCenToVpcResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unroute_private_zone_in_cen_to_vpc_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: cbn_20170912_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: cbn_20170912_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: cbn_20170912_models.UntagResourcesRequest,
    ) -> cbn_20170912_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: cbn_20170912_models.UntagResourcesRequest,
    ) -> cbn_20170912_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_cen_inter_region_traffic_qos_policy_attribute_with_options(
        self,
        request: cbn_20170912_models.UpdateCenInterRegionTrafficQosPolicyAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.UpdateCenInterRegionTrafficQosPolicyAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.traffic_qos_policy_description):
            query['TrafficQosPolicyDescription'] = request.traffic_qos_policy_description
        if not UtilClient.is_unset(request.traffic_qos_policy_id):
            query['TrafficQosPolicyId'] = request.traffic_qos_policy_id
        if not UtilClient.is_unset(request.traffic_qos_policy_name):
            query['TrafficQosPolicyName'] = request.traffic_qos_policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCenInterRegionTrafficQosPolicyAttribute',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UpdateCenInterRegionTrafficQosPolicyAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cen_inter_region_traffic_qos_policy_attribute_with_options_async(
        self,
        request: cbn_20170912_models.UpdateCenInterRegionTrafficQosPolicyAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.UpdateCenInterRegionTrafficQosPolicyAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.traffic_qos_policy_description):
            query['TrafficQosPolicyDescription'] = request.traffic_qos_policy_description
        if not UtilClient.is_unset(request.traffic_qos_policy_id):
            query['TrafficQosPolicyId'] = request.traffic_qos_policy_id
        if not UtilClient.is_unset(request.traffic_qos_policy_name):
            query['TrafficQosPolicyName'] = request.traffic_qos_policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCenInterRegionTrafficQosPolicyAttribute',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UpdateCenInterRegionTrafficQosPolicyAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cen_inter_region_traffic_qos_policy_attribute(
        self,
        request: cbn_20170912_models.UpdateCenInterRegionTrafficQosPolicyAttributeRequest,
    ) -> cbn_20170912_models.UpdateCenInterRegionTrafficQosPolicyAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_cen_inter_region_traffic_qos_policy_attribute_with_options(request, runtime)

    async def update_cen_inter_region_traffic_qos_policy_attribute_async(
        self,
        request: cbn_20170912_models.UpdateCenInterRegionTrafficQosPolicyAttributeRequest,
    ) -> cbn_20170912_models.UpdateCenInterRegionTrafficQosPolicyAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_cen_inter_region_traffic_qos_policy_attribute_with_options_async(request, runtime)

    def update_cen_inter_region_traffic_qos_queue_attribute_with_options(
        self,
        request: cbn_20170912_models.UpdateCenInterRegionTrafficQosQueueAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.UpdateCenInterRegionTrafficQosQueueAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.dscps):
            query['Dscps'] = request.dscps
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qos_queue_description):
            query['QosQueueDescription'] = request.qos_queue_description
        if not UtilClient.is_unset(request.qos_queue_id):
            query['QosQueueId'] = request.qos_queue_id
        if not UtilClient.is_unset(request.qos_queue_name):
            query['QosQueueName'] = request.qos_queue_name
        if not UtilClient.is_unset(request.remain_bandwidth_percent):
            query['RemainBandwidthPercent'] = request.remain_bandwidth_percent
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCenInterRegionTrafficQosQueueAttribute',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UpdateCenInterRegionTrafficQosQueueAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cen_inter_region_traffic_qos_queue_attribute_with_options_async(
        self,
        request: cbn_20170912_models.UpdateCenInterRegionTrafficQosQueueAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.UpdateCenInterRegionTrafficQosQueueAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.dscps):
            query['Dscps'] = request.dscps
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qos_queue_description):
            query['QosQueueDescription'] = request.qos_queue_description
        if not UtilClient.is_unset(request.qos_queue_id):
            query['QosQueueId'] = request.qos_queue_id
        if not UtilClient.is_unset(request.qos_queue_name):
            query['QosQueueName'] = request.qos_queue_name
        if not UtilClient.is_unset(request.remain_bandwidth_percent):
            query['RemainBandwidthPercent'] = request.remain_bandwidth_percent
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCenInterRegionTrafficQosQueueAttribute',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UpdateCenInterRegionTrafficQosQueueAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cen_inter_region_traffic_qos_queue_attribute(
        self,
        request: cbn_20170912_models.UpdateCenInterRegionTrafficQosQueueAttributeRequest,
    ) -> cbn_20170912_models.UpdateCenInterRegionTrafficQosQueueAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_cen_inter_region_traffic_qos_queue_attribute_with_options(request, runtime)

    async def update_cen_inter_region_traffic_qos_queue_attribute_async(
        self,
        request: cbn_20170912_models.UpdateCenInterRegionTrafficQosQueueAttributeRequest,
    ) -> cbn_20170912_models.UpdateCenInterRegionTrafficQosQueueAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_cen_inter_region_traffic_qos_queue_attribute_with_options_async(request, runtime)

    def update_traffic_marking_policy_attribute_with_options(
        self,
        request: cbn_20170912_models.UpdateTrafficMarkingPolicyAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.UpdateTrafficMarkingPolicyAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.traffic_marking_policy_description):
            query['TrafficMarkingPolicyDescription'] = request.traffic_marking_policy_description
        if not UtilClient.is_unset(request.traffic_marking_policy_id):
            query['TrafficMarkingPolicyId'] = request.traffic_marking_policy_id
        if not UtilClient.is_unset(request.traffic_marking_policy_name):
            query['TrafficMarkingPolicyName'] = request.traffic_marking_policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTrafficMarkingPolicyAttribute',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UpdateTrafficMarkingPolicyAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_traffic_marking_policy_attribute_with_options_async(
        self,
        request: cbn_20170912_models.UpdateTrafficMarkingPolicyAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.UpdateTrafficMarkingPolicyAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.traffic_marking_policy_description):
            query['TrafficMarkingPolicyDescription'] = request.traffic_marking_policy_description
        if not UtilClient.is_unset(request.traffic_marking_policy_id):
            query['TrafficMarkingPolicyId'] = request.traffic_marking_policy_id
        if not UtilClient.is_unset(request.traffic_marking_policy_name):
            query['TrafficMarkingPolicyName'] = request.traffic_marking_policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTrafficMarkingPolicyAttribute',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UpdateTrafficMarkingPolicyAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_traffic_marking_policy_attribute(
        self,
        request: cbn_20170912_models.UpdateTrafficMarkingPolicyAttributeRequest,
    ) -> cbn_20170912_models.UpdateTrafficMarkingPolicyAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_traffic_marking_policy_attribute_with_options(request, runtime)

    async def update_traffic_marking_policy_attribute_async(
        self,
        request: cbn_20170912_models.UpdateTrafficMarkingPolicyAttributeRequest,
    ) -> cbn_20170912_models.UpdateTrafficMarkingPolicyAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_traffic_marking_policy_attribute_with_options_async(request, runtime)

    def update_transit_router_with_options(
        self,
        request: cbn_20170912_models.UpdateTransitRouterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.UpdateTransitRouterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_description):
            query['TransitRouterDescription'] = request.transit_router_description
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not UtilClient.is_unset(request.transit_router_name):
            query['TransitRouterName'] = request.transit_router_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTransitRouter',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UpdateTransitRouterResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_transit_router_with_options_async(
        self,
        request: cbn_20170912_models.UpdateTransitRouterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.UpdateTransitRouterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_description):
            query['TransitRouterDescription'] = request.transit_router_description
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not UtilClient.is_unset(request.transit_router_name):
            query['TransitRouterName'] = request.transit_router_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTransitRouter',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UpdateTransitRouterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_transit_router(
        self,
        request: cbn_20170912_models.UpdateTransitRouterRequest,
    ) -> cbn_20170912_models.UpdateTransitRouterResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_transit_router_with_options(request, runtime)

    async def update_transit_router_async(
        self,
        request: cbn_20170912_models.UpdateTransitRouterRequest,
    ) -> cbn_20170912_models.UpdateTransitRouterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_transit_router_with_options_async(request, runtime)

    def update_transit_router_peer_attachment_attribute_with_options(
        self,
        request: cbn_20170912_models.UpdateTransitRouterPeerAttachmentAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.UpdateTransitRouterPeerAttachmentAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_publish_route_enabled):
            query['AutoPublishRouteEnabled'] = request.auto_publish_route_enabled
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.bandwidth_type):
            query['BandwidthType'] = request.bandwidth_type
        if not UtilClient.is_unset(request.cen_bandwidth_package_id):
            query['CenBandwidthPackageId'] = request.cen_bandwidth_package_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTransitRouterPeerAttachmentAttribute',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UpdateTransitRouterPeerAttachmentAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_transit_router_peer_attachment_attribute_with_options_async(
        self,
        request: cbn_20170912_models.UpdateTransitRouterPeerAttachmentAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.UpdateTransitRouterPeerAttachmentAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_publish_route_enabled):
            query['AutoPublishRouteEnabled'] = request.auto_publish_route_enabled
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.bandwidth_type):
            query['BandwidthType'] = request.bandwidth_type
        if not UtilClient.is_unset(request.cen_bandwidth_package_id):
            query['CenBandwidthPackageId'] = request.cen_bandwidth_package_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTransitRouterPeerAttachmentAttribute',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UpdateTransitRouterPeerAttachmentAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_transit_router_peer_attachment_attribute(
        self,
        request: cbn_20170912_models.UpdateTransitRouterPeerAttachmentAttributeRequest,
    ) -> cbn_20170912_models.UpdateTransitRouterPeerAttachmentAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_transit_router_peer_attachment_attribute_with_options(request, runtime)

    async def update_transit_router_peer_attachment_attribute_async(
        self,
        request: cbn_20170912_models.UpdateTransitRouterPeerAttachmentAttributeRequest,
    ) -> cbn_20170912_models.UpdateTransitRouterPeerAttachmentAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_transit_router_peer_attachment_attribute_with_options_async(request, runtime)

    def update_transit_router_route_entry_with_options(
        self,
        request: cbn_20170912_models.UpdateTransitRouterRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.UpdateTransitRouterRouteEntryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_route_entry_description):
            query['TransitRouterRouteEntryDescription'] = request.transit_router_route_entry_description
        if not UtilClient.is_unset(request.transit_router_route_entry_id):
            query['TransitRouterRouteEntryId'] = request.transit_router_route_entry_id
        if not UtilClient.is_unset(request.transit_router_route_entry_name):
            query['TransitRouterRouteEntryName'] = request.transit_router_route_entry_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTransitRouterRouteEntry',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UpdateTransitRouterRouteEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_transit_router_route_entry_with_options_async(
        self,
        request: cbn_20170912_models.UpdateTransitRouterRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.UpdateTransitRouterRouteEntryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_route_entry_description):
            query['TransitRouterRouteEntryDescription'] = request.transit_router_route_entry_description
        if not UtilClient.is_unset(request.transit_router_route_entry_id):
            query['TransitRouterRouteEntryId'] = request.transit_router_route_entry_id
        if not UtilClient.is_unset(request.transit_router_route_entry_name):
            query['TransitRouterRouteEntryName'] = request.transit_router_route_entry_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTransitRouterRouteEntry',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UpdateTransitRouterRouteEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_transit_router_route_entry(
        self,
        request: cbn_20170912_models.UpdateTransitRouterRouteEntryRequest,
    ) -> cbn_20170912_models.UpdateTransitRouterRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_transit_router_route_entry_with_options(request, runtime)

    async def update_transit_router_route_entry_async(
        self,
        request: cbn_20170912_models.UpdateTransitRouterRouteEntryRequest,
    ) -> cbn_20170912_models.UpdateTransitRouterRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_transit_router_route_entry_with_options_async(request, runtime)

    def update_transit_router_route_table_with_options(
        self,
        request: cbn_20170912_models.UpdateTransitRouterRouteTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.UpdateTransitRouterRouteTableResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_route_table_description):
            query['TransitRouterRouteTableDescription'] = request.transit_router_route_table_description
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        if not UtilClient.is_unset(request.transit_router_route_table_name):
            query['TransitRouterRouteTableName'] = request.transit_router_route_table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTransitRouterRouteTable',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UpdateTransitRouterRouteTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_transit_router_route_table_with_options_async(
        self,
        request: cbn_20170912_models.UpdateTransitRouterRouteTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.UpdateTransitRouterRouteTableResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_route_table_description):
            query['TransitRouterRouteTableDescription'] = request.transit_router_route_table_description
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        if not UtilClient.is_unset(request.transit_router_route_table_name):
            query['TransitRouterRouteTableName'] = request.transit_router_route_table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTransitRouterRouteTable',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UpdateTransitRouterRouteTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_transit_router_route_table(
        self,
        request: cbn_20170912_models.UpdateTransitRouterRouteTableRequest,
    ) -> cbn_20170912_models.UpdateTransitRouterRouteTableResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_transit_router_route_table_with_options(request, runtime)

    async def update_transit_router_route_table_async(
        self,
        request: cbn_20170912_models.UpdateTransitRouterRouteTableRequest,
    ) -> cbn_20170912_models.UpdateTransitRouterRouteTableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_transit_router_route_table_with_options_async(request, runtime)

    def update_transit_router_vbr_attachment_attribute_with_options(
        self,
        request: cbn_20170912_models.UpdateTransitRouterVbrAttachmentAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.UpdateTransitRouterVbrAttachmentAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_publish_route_enabled):
            query['AutoPublishRouteEnabled'] = request.auto_publish_route_enabled
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTransitRouterVbrAttachmentAttribute',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UpdateTransitRouterVbrAttachmentAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_transit_router_vbr_attachment_attribute_with_options_async(
        self,
        request: cbn_20170912_models.UpdateTransitRouterVbrAttachmentAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.UpdateTransitRouterVbrAttachmentAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_publish_route_enabled):
            query['AutoPublishRouteEnabled'] = request.auto_publish_route_enabled
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTransitRouterVbrAttachmentAttribute',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UpdateTransitRouterVbrAttachmentAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_transit_router_vbr_attachment_attribute(
        self,
        request: cbn_20170912_models.UpdateTransitRouterVbrAttachmentAttributeRequest,
    ) -> cbn_20170912_models.UpdateTransitRouterVbrAttachmentAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_transit_router_vbr_attachment_attribute_with_options(request, runtime)

    async def update_transit_router_vbr_attachment_attribute_async(
        self,
        request: cbn_20170912_models.UpdateTransitRouterVbrAttachmentAttributeRequest,
    ) -> cbn_20170912_models.UpdateTransitRouterVbrAttachmentAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_transit_router_vbr_attachment_attribute_with_options_async(request, runtime)

    def update_transit_router_vpc_attachment_attribute_with_options(
        self,
        request: cbn_20170912_models.UpdateTransitRouterVpcAttachmentAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.UpdateTransitRouterVpcAttachmentAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTransitRouterVpcAttachmentAttribute',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UpdateTransitRouterVpcAttachmentAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_transit_router_vpc_attachment_attribute_with_options_async(
        self,
        request: cbn_20170912_models.UpdateTransitRouterVpcAttachmentAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.UpdateTransitRouterVpcAttachmentAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTransitRouterVpcAttachmentAttribute',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UpdateTransitRouterVpcAttachmentAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_transit_router_vpc_attachment_attribute(
        self,
        request: cbn_20170912_models.UpdateTransitRouterVpcAttachmentAttributeRequest,
    ) -> cbn_20170912_models.UpdateTransitRouterVpcAttachmentAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_transit_router_vpc_attachment_attribute_with_options(request, runtime)

    async def update_transit_router_vpc_attachment_attribute_async(
        self,
        request: cbn_20170912_models.UpdateTransitRouterVpcAttachmentAttributeRequest,
    ) -> cbn_20170912_models.UpdateTransitRouterVpcAttachmentAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_transit_router_vpc_attachment_attribute_with_options_async(request, runtime)

    def update_transit_router_vpc_attachment_zones_with_options(
        self,
        request: cbn_20170912_models.UpdateTransitRouterVpcAttachmentZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.UpdateTransitRouterVpcAttachmentZonesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_zone_mappings):
            query['AddZoneMappings'] = request.add_zone_mappings
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remove_zone_mappings):
            query['RemoveZoneMappings'] = request.remove_zone_mappings
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTransitRouterVpcAttachmentZones',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UpdateTransitRouterVpcAttachmentZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_transit_router_vpc_attachment_zones_with_options_async(
        self,
        request: cbn_20170912_models.UpdateTransitRouterVpcAttachmentZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.UpdateTransitRouterVpcAttachmentZonesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_zone_mappings):
            query['AddZoneMappings'] = request.add_zone_mappings
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remove_zone_mappings):
            query['RemoveZoneMappings'] = request.remove_zone_mappings
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTransitRouterVpcAttachmentZones',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UpdateTransitRouterVpcAttachmentZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_transit_router_vpc_attachment_zones(
        self,
        request: cbn_20170912_models.UpdateTransitRouterVpcAttachmentZonesRequest,
    ) -> cbn_20170912_models.UpdateTransitRouterVpcAttachmentZonesResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_transit_router_vpc_attachment_zones_with_options(request, runtime)

    async def update_transit_router_vpc_attachment_zones_async(
        self,
        request: cbn_20170912_models.UpdateTransitRouterVpcAttachmentZonesRequest,
    ) -> cbn_20170912_models.UpdateTransitRouterVpcAttachmentZonesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_transit_router_vpc_attachment_zones_with_options_async(request, runtime)

    def update_transit_router_vpn_attachment_attribute_with_options(
        self,
        request: cbn_20170912_models.UpdateTransitRouterVpnAttachmentAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.UpdateTransitRouterVpnAttachmentAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_publish_route_enabled):
            query['AutoPublishRouteEnabled'] = request.auto_publish_route_enabled
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTransitRouterVpnAttachmentAttribute',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UpdateTransitRouterVpnAttachmentAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_transit_router_vpn_attachment_attribute_with_options_async(
        self,
        request: cbn_20170912_models.UpdateTransitRouterVpnAttachmentAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.UpdateTransitRouterVpnAttachmentAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_publish_route_enabled):
            query['AutoPublishRouteEnabled'] = request.auto_publish_route_enabled
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTransitRouterVpnAttachmentAttribute',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UpdateTransitRouterVpnAttachmentAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_transit_router_vpn_attachment_attribute(
        self,
        request: cbn_20170912_models.UpdateTransitRouterVpnAttachmentAttributeRequest,
    ) -> cbn_20170912_models.UpdateTransitRouterVpnAttachmentAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_transit_router_vpn_attachment_attribute_with_options(request, runtime)

    async def update_transit_router_vpn_attachment_attribute_async(
        self,
        request: cbn_20170912_models.UpdateTransitRouterVpnAttachmentAttributeRequest,
    ) -> cbn_20170912_models.UpdateTransitRouterVpnAttachmentAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_transit_router_vpn_attachment_attribute_with_options_async(request, runtime)

    def withdraw_published_route_entries_with_options(
        self,
        request: cbn_20170912_models.WithdrawPublishedRouteEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.WithdrawPublishedRouteEntriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not UtilClient.is_unset(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not UtilClient.is_unset(request.child_instance_route_table_id):
            query['ChildInstanceRouteTableId'] = request.child_instance_route_table_id
        if not UtilClient.is_unset(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not UtilClient.is_unset(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='WithdrawPublishedRouteEntries',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.WithdrawPublishedRouteEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def withdraw_published_route_entries_with_options_async(
        self,
        request: cbn_20170912_models.WithdrawPublishedRouteEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.WithdrawPublishedRouteEntriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not UtilClient.is_unset(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not UtilClient.is_unset(request.child_instance_route_table_id):
            query['ChildInstanceRouteTableId'] = request.child_instance_route_table_id
        if not UtilClient.is_unset(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not UtilClient.is_unset(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='WithdrawPublishedRouteEntries',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.WithdrawPublishedRouteEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def withdraw_published_route_entries(
        self,
        request: cbn_20170912_models.WithdrawPublishedRouteEntriesRequest,
    ) -> cbn_20170912_models.WithdrawPublishedRouteEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.withdraw_published_route_entries_with_options(request, runtime)

    async def withdraw_published_route_entries_async(
        self,
        request: cbn_20170912_models.WithdrawPublishedRouteEntriesRequest,
    ) -> cbn_20170912_models.WithdrawPublishedRouteEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.withdraw_published_route_entries_with_options_async(request, runtime)
