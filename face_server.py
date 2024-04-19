import asyncio
import logging

import grpc

from concurrent import futures
from infrastructure_layer.servicer.video_facedetect import VideoFaceDetect
from proto.video_service.video_service_pb2_grpc import add_VideoServiceServicer_to_server
from utils.tools.LoggingFormatter import LoggerManager
from utils.tools.gRPCManager import GrpcManager
from utils.tools.NacosManager import NacosManager

logger = LoggerManager(logger_name="gRPC").get_logger()
# 获取nacos.client模块的日志器，并设置其日志级别为WARNING
nacos_logger = logging.getLogger('nacos.client')
nacos_logger.setLevel(logging.WARNING)


async def serve():
    port = GrpcManager().get_service_config('face_detect_service')[1]
    server = grpc.aio.server(futures.ThreadPoolExecutor(max_workers=10))
    add_VideoServiceServicer_to_server(VideoFaceDetect(), server)
    server.add_insecure_port('[::]:' + str(port))
    nacos_serverutils = NacosManager().get_server_utils("face-detect-service-gRPC", "0.0.0.0", port)
    # 注册服务
    await nacos_serverutils.register_service()
    # 启动心跳发送任务
    asyncio.create_task(nacos_serverutils.beat(10))
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    logger.info("face_detect_service-gRPC服务启动...")
    asyncio.run(serve())
