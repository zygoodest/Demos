# 文件释义：
    build_protos.sh         用来编译proto文件的脚本
    client                  客户端示例文件
    run.py                  服务端示例文件
    protos                  存放.proto文件
    interface               存放.proto文件编译后的文件

# 使用流程：
    ## 1.在protos文件里编写.proto文件
    ## 2.运行build_protos.sh脚本，将.proto文件编译到interface目录
    ## 3.编写run.py文件(实现服务器，实现定义好的服务接口)
    ## 4.编写client.py实现客户端
    
