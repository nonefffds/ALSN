#!/bin/bash

#检测网络链接畅通
function network()
{
    #超时时间
    local timeout=1

    #目标网站
    local target=www.baidu.com

    #获取响应状态码
    local ret_code=`curl -I -s --connect-timeout ${timeout} ${target} -w %{http_code} | tail -n1`

    if [ "x$ret_code" = "x200" ]; then
        #网络畅通
        return 1
    else
        #网络不畅通
        return 0
    fi

    return 0
}

network
if [ $? -eq 0 ];then
    exec python3 ./autologin.py
    exit -1
fi

echo "Connected"

exit 0