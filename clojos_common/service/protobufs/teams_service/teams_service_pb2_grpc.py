# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from clojos_common.service.protobufs.teams_service import teams_service_pb2 as clojos__common_dot_service_dot_protobufs_dot_teams__service_dot_teams__service__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class TeamsServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTeams = channel.unary_unary(
                '/teams.TeamsService/GetTeams',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=clojos__common_dot_service_dot_protobufs_dot_teams__service_dot_teams__service__pb2.TeamsResponse.FromString,
                )


class TeamsServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetTeams(self, request, context):
        """A simple RPC.

        Obtains the MessageResponse at a given position.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TeamsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTeams': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTeams,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=clojos__common_dot_service_dot_protobufs_dot_teams__service_dot_teams__service__pb2.TeamsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'teams.TeamsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TeamsService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetTeams(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/teams.TeamsService/GetTeams',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            clojos__common_dot_service_dot_protobufs_dot_teams__service_dot_teams__service__pb2.TeamsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
