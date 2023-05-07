# 喷嚏图卦微信推送

使用Github Actions实现每天定时爬取《喷嚏图卦》，借助企业微信API推送到微信。

## 配置方法

1. Fork本项目
2. 配置Github Actions Secrets
    | 参数名 | 备注 |
    | ---- | ----- |
    | WECOM_CORP_ID | 你的企业微信ID |
    | WECOM_CORP_SECRET | 你的应用凭证密钥 |
    | WECOM_AGENT_ID | 你的应用ID |
3. 北京时间每天下午5点半左右推送到微信

## 企业微信部署方法

https://github.com/easychen/wecomchan/blob/main/README.md