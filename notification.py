# こちらは色んな媒体にプログラム終了時などに簡単にメッセージを送るためのモジュールです。

#以下の1,2のどちらかの方法でインポート出来ます(1を推奨)
# 1.githubからインポートする場合
"""
!git clone https://github.com/rimikoro/notification.git
from notification.notification import LINE, DISCORD, SLACK
"""

# 2.google driveを用いる場合
"""
まず、このファイルをgoogle driveにMy_Moduleというフォルダを作り、そこにこのファイルを格納してください。
その後、google colabなどで以下のプログラムをコピペすることでインストールできます。
----------------program---------------
# GoogleDriveのマウント
from google.colab import drive
drive.mount('/content/drive')
# notificationのそれぞれのクラスをインポート
from drive.MyDrive.My_Module.notification import LINE, DISCORD, SLACK
----------------program---------------
"""

# google colab内で使う際は次のように記述します。
"""
LINEに送る為のコマンド
LINE().send()

Slackに送るためのコマンド
SLACK().send()

Discordに送るためのコマンド
DISCORD().send()

デフォルトだとそれぞれの__init__内に記述した文章を送信します
google colabなどで使用する際 ~.send()の引数であるtext=に文章を書くとその文章を送ることができます
さらに、files=に画像の名前を指定すると画像も送れます
(google colab内の変数などを送りたいときに使用を想定)
"""

# Lineに送信するクラス
class LINE():
    def __init__(self):
        
        # self.TOKENに自分のline-notifyのトークンを入力
        # TOKENの取得はこちらからできます。→　https://notify-bot.line.me/ja/
        self.TOKEN = "AlQdD2L5NlrPkJOoNMDP3eMG8zth0u8kaPYhtzY0CUU"
        # self.api_urlは何も変更しないでください
        self.api_url = 'https://notify-api.line.me/api/notify'
        
        # self.send_contentsに送りたい文章を入力
        self.send_contents = "AIのプログラムが終了しました。"
        
        # requestsで送るために辞書化
        self.TOKEN_dic = {'Authorization': 'Bearer' + ' ' + self.TOKEN}
        self.send_dic = {'message': self.send_contents}

    def send(self, text = None, files = None):
        if text is not None:
            self.send_contents = text
            self.send_dic = {'message': self.send_contents}
        try:
            if files is None:
                requests.post(self.api_url, headers=self.TOKEN_dic, data=self.send_dic)
            else:
                requests.post(self.api_url, headers=self.TOKEN_dic, data=self.send_dic, files = {"imageFile": open(files, "rb")})
        except:
            import requests
            if files is None:
                requests.post(self.api_url, headers=self.TOKEN_dic, data=self.send_dic)
            else:
                requests.post(self.api_url, headers=self.TOKEN_dic, data=self.send_dic, files = {"imageFile": open(files, "rb")})
        print("LINEにメッセージを送信しました。")

# Slackに送信するクラス
class SLACK():
    def __init__(self):
        # self.webhook_urlに送りたい場所のwebhook urlを入力
        # urlの取得はこちらからできます。→　https://slack.com/services/new/incoming-webhook
        self.webhook_url = "https://hooks.slack.com/services/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"
        
        # self.textに送りたい文章を入力
        self.text = "AIのプログラムが終了しました。"
        
        # requestsで送るために辞書化
        self.text_dic = {"text":self.text}
    
    def send(self, text = None):
        if text is not None:
            self.text = text
            self.text_dic = {"text":self.text}
        try:
            requests.post(self.webhook_url, data = json.dumps(self.text_dic))
        except:
            import requests, json
            requests.post(self.webhook_url, data = json.dumps(self.text_dic))
        print("SLACKにメッセージを送信しました。")

# Discordに送信するクラス
class DISCORD():
    def __init__(self):
        # self.webhook_urlに送りたい場所のwebhook urlを入力
        # urlの取得はこちらを参照してください。→　https://qiita.com/otuhs_d/items/41f018ec3762db93a740
        # 現在webhookは送りたいテキストチャンネルの設定内の連携サービスの中で設定ができます。
        self.webhook_url = "https://discordapp.com/api/webhooks/1179833652411117649/oa9RhdD2u8r-TaF8ce5jPsCkuAiNgcumzFUVoSxyBORps15J0MkL0yMMkHt9UZKrPcnf"
        
        # self.contntに送りたい文章を入力
        self.content = "AIのプログラムが終了しました。"
        
        # requestsで送るために辞書化
        self.content_dic = {"content": self.content}
        self.headers = {"Content-Type": "application/json"}
    
    def send(self, text = None, files = None):
        if text is not None:
            self.content = text
            self.content_dic = {"content": self.content}
        elif files is not None:
            with open(files, "rb") as f:
                file_bin = f.read()
                file = {"favicon":(files,file_bin),}
        try:
            if files is None:
                requests.post(self.webhook_url, json.dumps(self.content_dic), headers = self.headers)
                print("Discordにメッセージを送信しました。")
            else:
                requests.post(self.webhook_url, files = file)
                print("Discordに画像を送信しました。")
        except:
            import requests, json
            if files is None:
                requests.post(self.webhook_url, json.dumps(self.content_dic), headers = self.headers)
                print("Discordにメッセージを送信しました。")
            else:
                requests.post(self.webhook_url, files = file)
                print("Discordに画像を送信しました。")

LINE().send()