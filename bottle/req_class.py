class RequestData:
    def __init__(self, request):
        self.request = request
        self.body_bytes = request.body.read()
        
    def dump_body(self):
        count = 1
        for i in self.body_bytes:
            if count % 16 == 0:
                print('%02x \n' % i, end = '')
            else:
                print('%02x ' % i, end = '')
            if len(self.body_bytes) == count:
                print('\n')
            count += 1

    def display_info(self):
        
        print('<リクエストを受信しました>')
        print('フォームパラメータ : {}'.format(self.request.params))
        print('HTTPメソッド : {}'.format(self.request.method))
        print('リクエスト本文 :')
        self.dump_body()
        print('アスセスされたURL : {}'.format(self.request.url))
        print('Content-Type : {}'.format(self.request.content_type))
        print('Content-Length : {}'.format(self.request.content_length))
        print('User-Agent : {}'.format(self.request.get_header('User-Agent')))
        print('Date : {}'.format(self.request.get_header('Date')))
        print('Content-Encoding : {}'.format(self.request.get_header('Content-Encoding')))
