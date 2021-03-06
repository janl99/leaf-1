"""
AccessToken 获取插件错误类定义
"""

from ...core import modules
from ...core import error as _oerror

Error = _oerror.Error


class AConnectionError(Error):
    """获取过程中的网络错误"""
    code = 20101
    description = "在获取过程中遇到网络错误"


class InvalidResponse(Error):
    """当收到了非法的响应时给出"""
    code = 20202
    description = "获取到了不正确的响应 - 留意中间人攻击"


class ReachedMaxRetries(Error):
    """当达到了最大的重试次数时"""
    code = 20203
    description = "经过多次重试后仍无法正常更新 AccessToken - 插件将停止运行"


class NoCachedAccessToken(Error):
    """暂时没有缓存的 AccessToken"""
    code = 20204
    description = "暂时没有缓存的 AccessToken"


class InvalidAppID(Error):
    """不正确的 APPID"""
    code = 40013
    description = "不正确的 APPID"


class InvalidAppSecret(Error):
    """不正确的 AppSecret"""
    code = 40125
    description = "不正确的 AppSecret"


class IPLimited(Error):
    """IP 地址被限制"""
    code = 40164
    description = "请在公众平台添加当前 IP 到白名单"


class AccessTokenStatusError(Error):
    """当前的 AccessToken 状态不正常时抛出"""
    code = 20205
    description = "缓存的 AccessToken 状态异常"


messenger: _oerror.Messenger = modules.error.messenger
messenger.register(AConnectionError)
messenger.register(InvalidResponse)
messenger.register(ReachedMaxRetries)
messenger.register(NoCachedAccessToken)
messenger.register(AccessTokenStatusError)
messenger.register(InvalidAppID)
messenger.register(InvalidAppSecret)
messenger.register(IPLimited)
