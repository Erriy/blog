#!/usr/bin/env python3.7
# -*- encoding:utf-8 -*-
from mitmproxy import ctx, http


class fake_response:

    def request(self, flow: http.HTTPFlow):
        # ctx.log.info("host = %s"%str(flow.request.headers["host"]))
        html = """
        <!DOCTYPE html>
        <html>
            <head>
                <title>我是{0}</title>
            </head>
            <body>
                <h1 style="text-align: center;">伪装{0}网站 from Err1y</h1>
                <h1 style="text-align: center;">... i'm watching u</h1>
            </body>
        </html>
        """
        if flow.request.path != "/":
            return
        d = {
            "taobao.com":"淘宝",
            "jd.com":"京东",
            "baidu.com":"百度",
            "163.com":"163",
            "12306.cn":"12306"
        }
        for k,v in d.items():
            if k not in flow.request.headers["host"]:
                continue
            flow.response = http.HTTPResponse.make(200, "", {"Content-Type":"text/html"})
            flow.response.set_text(html.format(v))
            return


addons = [
    fake_response(),
]

