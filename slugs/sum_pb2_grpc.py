# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import server_pb2 as server__pb2
from . import sum_pb2 as sum__pb2


class ManySumStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.sumToTarget = channel.unary_stream(
                '/ManySum/sumToTarget',
                request_serializer=sum__pb2.SumRequest.SerializeToString,
                response_deserializer=sum__pb2.SumResponse.FromString,
                )
        self.exactSum = channel.unary_unary(
                '/ManySum/exactSum',
                request_serializer=sum__pb2.ExactSumReqeust.SerializeToString,
                response_deserializer=sum__pb2.ExactSumResponse.FromString,
                )
        self.testOneOf = channel.stream_stream(
                '/ManySum/testOneOf',
                request_serializer=server__pb2.HelloRequest.SerializeToString,
                response_deserializer=sum__pb2.OneOfResepone.FromString,
                )


class ManySumServicer(object):
    """Missing associated documentation comment in .proto file."""

    def sumToTarget(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def exactSum(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def testOneOf(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ManySumServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'sumToTarget': grpc.unary_stream_rpc_method_handler(
                    servicer.sumToTarget,
                    request_deserializer=sum__pb2.SumRequest.FromString,
                    response_serializer=sum__pb2.SumResponse.SerializeToString,
            ),
            'exactSum': grpc.unary_unary_rpc_method_handler(
                    servicer.exactSum,
                    request_deserializer=sum__pb2.ExactSumReqeust.FromString,
                    response_serializer=sum__pb2.ExactSumResponse.SerializeToString,
            ),
            'testOneOf': grpc.stream_stream_rpc_method_handler(
                    servicer.testOneOf,
                    request_deserializer=server__pb2.HelloRequest.FromString,
                    response_serializer=sum__pb2.OneOfResepone.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ManySum', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ManySum(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def sumToTarget(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/ManySum/sumToTarget',
            sum__pb2.SumRequest.SerializeToString,
            sum__pb2.SumResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def exactSum(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ManySum/exactSum',
            sum__pb2.ExactSumReqeust.SerializeToString,
            sum__pb2.ExactSumResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def testOneOf(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/ManySum/testOneOf',
            server__pb2.HelloRequest.SerializeToString,
            sum__pb2.OneOfResepone.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
