import hmac # 一个进行加salt加密算法的模块
raw_message = b"Hello, world!"
key = b"secret" # 需要注意的是传入的key和message都是bytes类型的
encrypted_message = hmac.new(key, raw_message, digestmod='MD5')
print(encrypted_message.hexdigest())
# a small change