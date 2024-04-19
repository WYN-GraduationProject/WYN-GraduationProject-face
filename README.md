# 王亚宁毕业设计-人脸检测微服务

> 项目为王亚宁本科毕业设计中的视频人脸检测微服务部分

## 项目架构

> 采用 DDD 领域驱动设计架构
> - 应用层（Application Layer）：face_server.py
> - 领域层（Domain
    Layer）: [python_common/](https://github.com/WYN-GraduationProject/WYN-GraduationProject-common/tree/main/python_common)
> - 基础设施层（Infrastructure Layer）：infrastructure_layer/

## 技术栈

> - openCV
>- gRPC
>- Nacos
>- Docker
>- GitHub actions

## 功能

> - 通过 gRPC 暴露预处理微服务的服务端
>- 通过 openCV 实现预处理微服务的人脸检测功能
>- 通过 Nacos 实现服务注册与发现
>- 通过 Docker 实现容器化部署
>- 通过 GitHub actions 实现 CI/CD