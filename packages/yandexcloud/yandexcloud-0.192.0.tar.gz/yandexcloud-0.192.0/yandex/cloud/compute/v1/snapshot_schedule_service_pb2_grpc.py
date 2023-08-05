# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.compute.v1 import snapshot_schedule_pb2 as yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__pb2
from yandex.cloud.compute.v1 import snapshot_schedule_service_pb2 as yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


class SnapshotScheduleServiceStub(object):
    """A set of methods for managing snapshot schedules.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.compute.v1.SnapshotScheduleService/Get',
                request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.GetSnapshotScheduleRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__pb2.SnapshotSchedule.FromString,
                )
        self.List = channel.unary_unary(
                '/yandex.cloud.compute.v1.SnapshotScheduleService/List',
                request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.ListSnapshotSchedulesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.ListSnapshotSchedulesResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/yandex.cloud.compute.v1.SnapshotScheduleService/Create',
                request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.CreateSnapshotScheduleRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Update = channel.unary_unary(
                '/yandex.cloud.compute.v1.SnapshotScheduleService/Update',
                request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.UpdateSnapshotScheduleRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Delete = channel.unary_unary(
                '/yandex.cloud.compute.v1.SnapshotScheduleService/Delete',
                request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.DeleteSnapshotScheduleRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.UpdateDisks = channel.unary_unary(
                '/yandex.cloud.compute.v1.SnapshotScheduleService/UpdateDisks',
                request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.UpdateSnapshotScheduleDisksRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Disable = channel.unary_unary(
                '/yandex.cloud.compute.v1.SnapshotScheduleService/Disable',
                request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.DisableSnapshotScheduleRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Enable = channel.unary_unary(
                '/yandex.cloud.compute.v1.SnapshotScheduleService/Enable',
                request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.EnableSnapshotScheduleRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.ListOperations = channel.unary_unary(
                '/yandex.cloud.compute.v1.SnapshotScheduleService/ListOperations',
                request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.ListSnapshotScheduleOperationsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.ListSnapshotScheduleOperationsResponse.FromString,
                )
        self.ListSnapshots = channel.unary_unary(
                '/yandex.cloud.compute.v1.SnapshotScheduleService/ListSnapshots',
                request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.ListSnapshotScheduleSnapshotsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.ListSnapshotScheduleSnapshotsResponse.FromString,
                )
        self.ListDisks = channel.unary_unary(
                '/yandex.cloud.compute.v1.SnapshotScheduleService/ListDisks',
                request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.ListSnapshotScheduleDisksRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.ListSnapshotScheduleDisksResponse.FromString,
                )


class SnapshotScheduleServiceServicer(object):
    """A set of methods for managing snapshot schedules.
    """

    def Get(self, request, context):
        """Returns the specified snapshot schedule.

        To get the list of available snapshot schedules, make a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves the list of snapshot schedules in the specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Creates a snapshot schedule in the specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Updates the specified snapshot schedule.

        The schedule is updated only after all snapshot creations and deletions triggered by the schedule are completed.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes the specified snapshot schedule.

        Deleting a snapshot schedule removes its data permanently and is irreversible. However, deleting a schedule
        does not delete any snapshots created by the schedule. You must delete snapshots separately.

        The schedule is deleted only after all snapshot creations and deletions triggered by the schedule are completed.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateDisks(self, request, context):
        """Updates the list of disks attached to the specified schedule.

        The schedule is updated only after all snapshot creations and deletions triggered by the schedule are completed.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Disable(self, request, context):
        """Disables the specified snapshot schedule.

        The [SnapshotSchedule.status] is changed to `INACTIVE`: the schedule is interrupted, snapshots won't be created
        or deleted.

        The schedule is disabled only after all snapshot creations and deletions triggered by the schedule are completed.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Enable(self, request, context):
        """Enables the specified snapshot schedule.

        The [SnapshotSchedule.status] is changed to `ACTIVE`: new disk snapshots will be created, old ones deleted
        (if [SnapshotSchedule.retention_policy] is specified).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOperations(self, request, context):
        """Lists operations for the specified snapshot schedule.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListSnapshots(self, request, context):
        """Retrieves the list of snapshots created by the specified snapshot schedule.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListDisks(self, request, context):
        """Retrieves the list of disks attached to the specified snapshot schedule.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SnapshotScheduleServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.GetSnapshotScheduleRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__pb2.SnapshotSchedule.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.ListSnapshotSchedulesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.ListSnapshotSchedulesResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.CreateSnapshotScheduleRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.UpdateSnapshotScheduleRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.DeleteSnapshotScheduleRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'UpdateDisks': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateDisks,
                    request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.UpdateSnapshotScheduleDisksRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Disable': grpc.unary_unary_rpc_method_handler(
                    servicer.Disable,
                    request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.DisableSnapshotScheduleRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Enable': grpc.unary_unary_rpc_method_handler(
                    servicer.Enable,
                    request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.EnableSnapshotScheduleRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListOperations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOperations,
                    request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.ListSnapshotScheduleOperationsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.ListSnapshotScheduleOperationsResponse.SerializeToString,
            ),
            'ListSnapshots': grpc.unary_unary_rpc_method_handler(
                    servicer.ListSnapshots,
                    request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.ListSnapshotScheduleSnapshotsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.ListSnapshotScheduleSnapshotsResponse.SerializeToString,
            ),
            'ListDisks': grpc.unary_unary_rpc_method_handler(
                    servicer.ListDisks,
                    request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.ListSnapshotScheduleDisksRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.ListSnapshotScheduleDisksResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.compute.v1.SnapshotScheduleService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SnapshotScheduleService(object):
    """A set of methods for managing snapshot schedules.
    """

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.compute.v1.SnapshotScheduleService/Get',
            yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.GetSnapshotScheduleRequest.SerializeToString,
            yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__pb2.SnapshotSchedule.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.compute.v1.SnapshotScheduleService/List',
            yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.ListSnapshotSchedulesRequest.SerializeToString,
            yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.ListSnapshotSchedulesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.compute.v1.SnapshotScheduleService/Create',
            yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.CreateSnapshotScheduleRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.compute.v1.SnapshotScheduleService/Update',
            yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.UpdateSnapshotScheduleRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.compute.v1.SnapshotScheduleService/Delete',
            yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.DeleteSnapshotScheduleRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateDisks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.compute.v1.SnapshotScheduleService/UpdateDisks',
            yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.UpdateSnapshotScheduleDisksRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Disable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.compute.v1.SnapshotScheduleService/Disable',
            yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.DisableSnapshotScheduleRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Enable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.compute.v1.SnapshotScheduleService/Enable',
            yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.EnableSnapshotScheduleRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListOperations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.compute.v1.SnapshotScheduleService/ListOperations',
            yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.ListSnapshotScheduleOperationsRequest.SerializeToString,
            yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.ListSnapshotScheduleOperationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListSnapshots(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.compute.v1.SnapshotScheduleService/ListSnapshots',
            yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.ListSnapshotScheduleSnapshotsRequest.SerializeToString,
            yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.ListSnapshotScheduleSnapshotsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListDisks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.compute.v1.SnapshotScheduleService/ListDisks',
            yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.ListSnapshotScheduleDisksRequest.SerializeToString,
            yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__service__pb2.ListSnapshotScheduleDisksResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
